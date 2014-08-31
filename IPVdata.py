# -*- coding: utf-8 -*-

import pandas as pd
import os
import zipfile

class IPVdata():
	"""docstring for IPVdata"""
	def __init__(self, folderPath):
		self.folderPath = folderPath
		self.ipv_data = pd.DataFrame()
		if self.folderAnalysis(self.folderPath):
			print 'Read Data Files Successfully.'
		else:
			print 'Read Data Files Failed.'



	def folderAnalysis(self, folderPath):
		try:
			for filetuple in os.walk(folderPath):
				for datafile in filetuple[2]:
					data_ipv = pd.DataFrame()
					if datafile.endswith(".csv"):
						data_ipv = pd.read_csv(filetuple[0]+"\\"+datafile, skiprows = 6)
						data_ipv = data_ipv[:-1]
					elif datafile.endswith(".zip"):
						zf = zipfile.ZipFile(filetuple[0]+"\\"+datafile, "r")
						pf = zf.open(zf.filelist[0].filename, "r")
						data_ipv = pd.read_csv(pf, skiprows = 6)
						data_ipv = data_ipv[:-1]
					self.ipv_data = self.ipv_data.append(data_ipv)
					self.ipv_data = self.ipv_data.drop_duplicates()

			return True
		except Exception, e:
			raise e

	def returneNBList(self):
		if not self.ipv_data.empty:
			return list(self.ipv_data["eNodeB Name"].drop_duplicates().dropna())

	def filterDate(self, siteName):
		timeRange = self.ipv_data[self.ipv_data["eNodeB Name"]==siteName].Time.drop_duplicates()
		return timeRange

	def processData(self, startDate, endDate, hour, sitename, flt_cell):
		#self.ipv_data.index = pd.to_datetime(self.ipv_data, format="%Y-%m-%d %H:%M", coerce=True)
		rgn = pd.DatetimeIndex(start=startDate, end=endDate,freq="D")
		str_time = list()
		for pd_time in rgn:
			for x in range(24):
				if (hour/(2**x))%2:
					str_time.append(str(pd_time).split()[0]+str(" %02d:00" %x))
		tmp_data = self.ipv_data
		tmp_data = tmp_data[tmp_data["eNodeB Name"]==sitename]
		tmp_data = tmp_data[tmp_data["Time"].isin(str_time)]
		if flt_cell == "1.8GHz Only":
			tmp_data = self.ipv_data[self.ipv_data["Cell Name"].apply(lambda x: 'L18' in str(x))]
		elif flt_cell == "2.6GHz Only":
			tmp_data = self.ipv_data[self.ipv_data["Cell Name"].apply(lambda x: 'L26' in str(x))]
		tmp_count = tmp_data["Integrity"].count()
		try:
			rrc_sr = tmp_data["L.RRC.ConnReq.Succ"].sum()/tmp_data["L.RRC.ConnReq.Att"].sum()*100.0
			erab_sr = tmp_data["L.E-RAB.SuccEst"].sum()/tmp_data["L.E-RAB.AttEst"].sum()*100.0
			s1_sr = tmp_data["L.S1Sig.ConnEst.Succ"].sum()/tmp_data["L.S1Sig.ConnEst.Att"].sum()*100.0
			all_sr = rrc_sr*erab_sr*s1_sr/10000.0
			all_sr = str(all_sr)[:str(all_sr).index('.')+3]
		except ZeroDivisionError:
			all_sr = '/0'
		try:
			call_drop = tmp_data["L.E-RAB.AbnormRel"].sum()/tmp_data["L.E-RAB.SuccEst"].sum()*100.0
			call_drop = str(call_drop)[:str(call_drop).index('.')+3]
		except ZeroDivisionError:
			call_drop = '/0'
		try:
			intrafreq_ho = (tmp_data["L.HHO.IntraeNB.IntraFreq.ExecSuccOut"].sum()+tmp_data["L.HHO.IntereNB.IntraFreq.ExecSuccOut"].sum())/\
					(tmp_data["L.HHO.IntraeNB.IntraFreq.PrepAttOut"].sum()+tmp_data["L.HHO.IntereNB.IntraFreq.PrepAttOut"].sum())*100.0
			intrafreq_ho = str(intrafreq_ho)[:str(intrafreq_ho).index('.')+3]
		except ZeroDivisionError:
			intrafreq_ho = '/0'
		try:
			interfreq_ho = (tmp_data["L.HHO.IntraeNB.InterFreq.ExecSuccOut"].sum()+tmp_data["L.HHO.IntereNB.InterFreq.ExecSuccOut"].sum())/\
					(tmp_data["L.HHO.IntraeNB.InterFreq.PrepAttOut"].sum()+tmp_data["L.HHO.IntereNB.InterFreq.PrepAttOut"].sum())*100.0
			interfreq_ho = str(interfreq_ho)[:str(interfreq_ho).index('.')+3]
		except ZeroDivisionError:
			interfreq_ho = '/0'
		try:
			irat_ho = tmp_data["L.IRATHO.E2W.ExecSuccOut"].sum()/tmp_data["L.IRATHO.E2W.PrepAttOut"].sum()*100.0
			irat_ho = str(irat_ho)[:str(irat_ho).index('.')+3]
		except ZeroDivisionError:
			irat_ho = '/0'
		radio_avail = 100 - tmp_data["L.Cell.Unavail.Dur.Sys(s)"].sum()/tmp_count/60.0
		radio_avail = str(radio_avail)[:str(radio_avail).index('.')+3]
		pkt_loss = 0
		pkt_tol = 0
		for i in range(9):
			pkt_loss += tmp_data[str("L.Traffic.DL.PktUuLoss.Loss.QCI.%d(packet)"%(i+1))].sum()
			pkt_tol += tmp_data[str("L.Traffic.DL.PktUuLoss.Tot.QCI.%d(packet)"%(i+1))].sum()
		try:
			pkt_rate = pkt_loss/pkt_tol*100.0
			pkt_rate = str(pkt_rate)[:str(pkt_rate).index('.')+3]
		except ZeroDivisionError:
			pkt_rate = '/0'
		return [all_sr,all_sr>'99',call_drop,call_drop<'0.4',intrafreq_ho,intrafreq_ho>'95',interfreq_ho,interfreq_ho>'95',irat_ho,irat_ho>'95',radio_avail,radio_avail>'99',pkt_rate,pkt_rate<'5']

if __name__ == '__main__':
	test = IPVdata("C:\\Users\\x00235379\\Desktop\\IPV")
	#print list(test.returneNBList().dropna())
	print list 
	#for test in os.walk("C:\\Users\\x00235379\\Desktop\\IPV"):



                
