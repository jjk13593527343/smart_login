import MySQLdb


class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.db = MySQLdb.connect(user='root',password='123456',host='127.0.0.1',db='jd',charset='utf8')
		self.cur = self.db.cursor()
	def select_shoop_name(self):
		select = 'select * from shoop_name'
		self.cur.execute(select)
		for i in self.cur.fetchall():
			print(i)
	def select_shoop(self,name):
		select = 'select u.shoop_name,a.shoop_title,a.shoop_url,a.shoop_id,a.shoop_price from shoop_name as u join shoop_info a on u.shoop_name=a.shoop_name where a.shoop_name="%s"'%name
		self.cur.execute(select)
		for i in self.cur.fetchall():
			print('商品类型:',i[0],'商品名称:',i[1],'商品链接:',i[2],'商品ID:',i[3],'商品价格:',i[4])
	def select_comment(self,shoop_id):
		select = 'select u.shoop_title,u.shoop_url,a.nike_name,a.createDate,a.content from shoop_info as u join shoop_comment a on u.shoop_id=a.shoop_id where a.shoop_id="%s"'%shoop_id
		self.cur.execute(select)
		for i in self.cur.fetchall():
			print('商品名称:',i[0],'商品链接:',i[1],'用户名:',i[2],'评论时间:',i[3])
			print('--------------------------[评论信息]------------------------------------')
			print(i[4])
			print('------------------------------------------------------------------------')

	def __del__(self):
		self.db.close()

if __name__ == '__main__':
	# shoop = ClassName()
	# shoop.select_shoop_name()
	# shoop.select_shoop('小辣椒')
	# shoop.select_comment('3901175')






















