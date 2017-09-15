# -*- encoding:utf-8 -*-



SETTINGS = {

    'url':'http://beijing.customs.gov.cn/publish/portal159/tab70929/',
    'next_page':'http://beijing.customs.gov.cn/publish/portal159/tab70929/module193706/page{}.htm',
    'domain_name':'beijing.customs.gov.cn',

    'css':{
        'domain_name':'http://beijing.customs.gov.cn',
        'next_page':'#ess_ctr193706_ListC_Info_AspNetPager .Normal',
        'index_urls':'#ess_ctr193706_ModuleContent ul li a::attr(href)',
        'title':'h1 strong::text ',
        'date':'.xl_Out1 .detailTime::text',
        'pdf_file':'#zoom > a::attr(href)',
        'Punishment_doc':'h1 strong',
        'Punishment_com':'h1 strong',
        'content_type':'pdf文件',
        'base64_type':'b64encode',
        'party':'pdf文件中',
        'url':'',
    }
}