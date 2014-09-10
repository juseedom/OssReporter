# -*- coding: utf-8 -*-

import pandas as pd
import os
import zipfile

class IPVdata():
	"""docstring for IPVdata"""
	def __init__(self, folderPath):
		self.folderPath = folderPath
		self.ipv_data = pd.DataFrame()
		self.paths = list()
		self.eNB = list()
		self.DateRange = list()
		self.sitename = ""
		self.folderAnalysis(self.folderPath)

	def folderAnalysis(self, folderPath):
		try:
			self.paths = list()
			self.DateRange = list()
			for filetuple in os.walk(folderPath):
				for datafile in filetuple[2]:
					if datafile.endswith(".zip"):
						self.paths.append(filetuple[0]+"\\"+datafile)
						self.DateRange.append(datafile.split(".")[-2][-8:])
						print("Found Data file:" + datafile)
			self.DateRange.sort()
			rng_date = pd.DatetimeIndex(start=self.DateRange[0], end=self.DateRange[-1],freq="D")
			self.DateRange = [(ddate-1) for ddate in rng_date]
			
			self.paths.sort()
			data_ipv = self.readzipdata(self.paths[-1])
			self.eNB = list(data_ipv["eNodeB Name"].drop_duplicates().dropna())

		except Exception, e:
			raise e

	def readzipdata(self, filepath):
		try:
			zf = zipfile.ZipFile(filepath, "r")
			pf = zf.open(zf.filelist[0].filename, "r")
			data_ipv = pd.read_csv(pf, skiprows = 6, low_memory = False)
			data_ipv = data_ipv[:-1]
			zf.close()
			return data_ipv
		except Exception, e:
			print("Open %s failed..." %filepath)
			raise e



	def processData(self, startDate, endDate, hour, sitename, flt_cell):
		#self.ipv_data.index = pd.to_datetime(self.ipv_data, format="%Y-%m-%d %H:%M", coerce=True)
		self.ipv_data = pd.DataFrame()
		rgn = pd.DatetimeIndex(start=startDate, end=endDate,freq="D")
		str_time = list()
		for pd_time in rgn:
			for x in range(24):
				if (hour/(2**x))%2:
					str_time.append(str(pd_time).split()[0]+str(" %02d:00" %x))
			for a in self.paths:
				str_date = str(pd_time+1).split()[0].replace("-","")
				if a.split("\\")[-1].find(str_date) != -1:
					ipvdata = self.readzipdata(a)
					self.ipv_data = self.ipv_data.append(ipvdata)
					break
		tmp_data = self.ipv_data
		tmp_data = tmp_data[tmp_data["eNodeB Name"]==sitename]
		tmp_data = tmp_data[tmp_data["Time"].isin(str_time)]
		if flt_cell == "1.8GHz Only":
			tmp_data = tmp_data[tmp_data["Cell Name"].apply(lambda x: 'L18' in str(x))]
		if flt_cell == "2.6GHz Only":
			tmp_data = tmp_data[tmp_data["Cell Name"].apply(lambda x: 'L26' in str(x))]
		tmp_count = tmp_data["Integrity"].count()
		#print(tmp_data.groupby(["eNodeB Name","Time","Cell Name"])["L.RRC.ConnReq.Succ"].sum())
		try:
			rrc_sr = tmp_data["L.RRC.ConnReq.Succ"].sum()/tmp_data["L.RRC.ConnReq.Att"].sum()*100.0
			erab_sr = tmp_data["L.E-RAB.SuccEst"].sum()/tmp_data["L.E-RAB.AttEst"].sum()*100.0
			s1_sr = tmp_data["L.S1Sig.ConnEst.Succ"].sum()/tmp_data["L.S1Sig.ConnEst.Att"].sum()*100.0
			all_sr = rrc_sr*erab_sr*s1_sr/10000.0
			all_sr = "%0.2f" % all_sr
		except ZeroDivisionError:
			all_sr = '/0'
		try:
			call_drop = tmp_data["L.E-RAB.AbnormRel"].sum()/tmp_data["L.E-RAB.SuccEst"].sum()*100.0
			call_drop = "%0.2f" % call_drop
		except ZeroDivisionError:
			call_drop = '/0'
		try:
			intrafreq_ho = (tmp_data["L.HHO.IntraeNB.IntraFreq.ExecSuccOut"].sum()+tmp_data["L.HHO.IntereNB.IntraFreq.ExecSuccOut"].sum())/\
					(tmp_data["L.HHO.IntraeNB.IntraFreq.PrepAttOut"].sum()+tmp_data["L.HHO.IntereNB.IntraFreq.PrepAttOut"].sum())*100.0
			intrafreq_ho = "%0.2f" % intrafreq_ho
		except ZeroDivisionError:
			intrafreq_ho = '/0'
		try:
			interfreq_ho = (tmp_data["L.HHO.IntraeNB.InterFreq.ExecSuccOut"].sum()+tmp_data["L.HHO.IntereNB.InterFreq.ExecSuccOut"].sum())/\
					(tmp_data["L.HHO.IntraeNB.InterFreq.PrepAttOut"].sum()+tmp_data["L.HHO.IntereNB.InterFreq.PrepAttOut"].sum())*100.0
			interfreq_ho = "%.02f" %interfreq_ho
		except ZeroDivisionError:
			interfreq_ho = '/0'
		try:
			irat_ho = tmp_data["L.IRATHO.E2W.ExecSuccOut"].sum()/tmp_data["L.IRATHO.E2W.PrepAttOut"].sum()*100.0
			irat_ho = "%0.2f" % irat_ho
		except ZeroDivisionError:
			irat_ho = '/0'
		radio_avail = 100.0 - tmp_data["L.Cell.Unavail.Dur.Sys(s)"].sum()/tmp_count/60.0
		radio_avail = "%.02f" %radio_avail
		pkt_loss = 0.0
		pkt_tol = 0.0
		for i in range(9):
			pkt_loss += tmp_data[str("L.Traffic.DL.PktUuLoss.Loss.QCI.%d(packet)"%(i+1))].sum()
			pkt_tol += tmp_data[str("L.Traffic.DL.PktUuLoss.Tot.QCI.%d(packet)"%(i+1))].sum()
		try:
			pkt_rate = 100.0*pkt_loss/pkt_tol
			pkt_rate = "%.02f" %pkt_rate
		except ZeroDivisionError:
			pkt_rate = '/0'
		return [all_sr,float(all_sr.split('/')[-1])>99.0,call_drop,float(call_drop.split('/')[-1])<0.4,intrafreq_ho,float(intrafreq_ho.split('/')[-1])>95.0,interfreq_ho,float(interfreq_ho.split('/')[-1])>95.0,irat_ho,float(irat_ho.split('/')[-1])>95.0,radio_avail,float(radio_avail.split('/')[-1])>99.0,pkt_rate,float(pkt_rate.split('/')[-1])<5.0]
if __name__ == '__main__':
	test = IPVdata("C:\\Users\\x00235379\\Desktop\\IPV")
	#print list(test.returneNBList().dropna())
	#print list 
	#for test in os.walk("C:\\Users\\x00235379\\Desktop\\IPV"):
