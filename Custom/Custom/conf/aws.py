# -*-encoding:utf-8 -*-
import boto3

from Custom.conf import AWS


class Aws(object):
	
	def __init__(self):
		
		self.s3 = boto3.client('s3')
		self.bucket  = AWS['bucket']
		self.bucket_path = AWS['bucket_path']
	
	def upload_file(self,path,file_name,date):
		
		date = '/'.join(date.split('-'))
		self.s3.upload_file(path, self.bucket, '{0}/{1}/{2}.json'.format(self.bucket_path,date,file_name))
	
	
	

	
