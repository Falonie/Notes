text=r"""
<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head>
    
<title>
    创投数据库_因果树
</title>
<meta name="Keywords" content="InnoTREE因果树创新创业双创平台，InnoTREE因果树，InnoTREE，因果树，创新创业双创平台，创新创业双创，滕放，帮主，创客帮，中国创新创业双创平台，北京创新创业双创平台，融资机构，投资机构，投融资机构，创业，创业项目，好项目，创业导师，商业计划书" />
<meta name="description" content="因果树创新创业双创服务,InnoTREE因果树,InnoTREE,因果树,创新创业双创,滕放,帮主,创投大数据,融资机构,投资机构,创业,创业项目,创业导师,商业计划书" />
<meta charset="UTF-8" />
<meta name="baidu-site-verification" content="Za91L6pSoj" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta name="renderer" content="webkit" />
<link rel="shortcut icon" href="/static/images/favicon.ico" type="image/x-icon" />
<link rel="icon" href="/static/images/favicon.ico" type="image/x-icon" />

    <link href="/static/inno/css/global.css?v=dfaa8c82" rel="stylesheet" type="text/css" /><link href="/static/inno/css/header.css?v=43c05ea6" rel="stylesheet" type="text/css" /><link href="/static/inno/css/footer.css?v=d497a909" rel="stylesheet" type="text/css" /><link href="/static/inno/css/iconfonts.css?v=8bf9f9c6" rel="stylesheet" type="text/css" /><link href="/static/inno/css/pagination.css?v=460f8c45" rel="stylesheet" type="text/css" /><link href="/static/inno/css/tooltips.css?v=85270a94" rel="stylesheet" type="text/css" /><link href="/static/inno/css/register.css?v=207ec98f" rel="stylesheet" type="text/css" /><link href="/static/inno/css/force.css?v=22f3dc00" rel="stylesheet" type="text/css" /><link href="/static/inno/css/quanju_170922.css?v=ec924e2e" rel="stylesheet" type="text/css" /><link href="/static/inno/css/screen_170913_02.css?v=25d3ffa8" rel="stylesheet" type="text/css" /><link href="/static/inno/css/index_170912.css?v=1c331288" rel="stylesheet" type="text/css" />
    <!--搜索框-->
    <link href="/static/inno/css/sousuokuang_171010_3.css?v=9a8be98c" rel="stylesheet" type="text/css" />
    <!--行业过滤-->
    <link href="/static/inno/css/list_02.css?v=16563e04" rel="stylesheet" type="text/css" />
    <!--表格-->
    <link href="/static/inno/css/table_03.css?v=8ee00d74" rel="stylesheet" type="text/css" />
    <!--翻页-->
    <link href="/static/inno/css/fanye.css?v=a814563f" rel="stylesheet" type="text/css" /><link href="/static/inno/css/disan_171010.css?v=2e3ca39a" rel="stylesheet" type="text/css" /><link href="/static/inno/css/financeNoResultCss.css?v=e023356f" rel="stylesheet" type="text/css" /><link href="/static/inno/css/screeningTags.css?v=b28528a6" rel="stylesheet" type="text/css" /><link href="/static/inno/css/list_01.css?v=5f526c10" rel="stylesheet" type="text/css" /><script src="https://hm.baidu.com/hm.js?ddf0d99bc06024e29662071b7fc5044f"></script><script src="//push.zhanzhang.baidu.com/push.js"></script><script src="//hm.baidu.com/hm.js?37854ae85b75cf05012d4d71db2a355a"></script><script type="text/javascript" src="/static/inno/js/common/jquery-3.2.1.min.js?v=c9f5aeec" charset="utf-8"></script><script type="text/javascript" src="/static/js/commonUtil.js?v=0f581905" charset="utf-8"></script><script type="text/javascript" src="/static/js/sea-modules/clipbord/ZeroClipboard.js?v=a50cf200" charset="utf-8"></script><script type="text/javascript" src="/static/js/inc/innotree_tongji.js?v=64735808" charset="utf-8"></script>
<script>
    if (typeof(console) == 'undefined') {
        window.console = {
            log: function () {
            }
        };
    };
    ;var _hmt = _hmt || [];
(function (document) {
    var config = {'www.innotree.cn':'37854ae85b75cf05012d4d71db2a355a','m.innotree.cn':'958bf338c97019fc0e383ddf1cb626a4'};
    var hm = document.createElement("script");
    var host = window.location.hostname;
    hm.src = "//hm.baidu.com/hm.js?" + (host in config?config[host]:'d68c884b445858a8e6b47bb982809cfc');
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(hm, s);

    var bp = document.createElement('script');
    bp.src = '//push.zhanzhang.baidu.com/push.js';
    s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})(document);
    //InnoTREE 统计 js (function (document) {})(document);

//========================util S=================================
Date.prototype.Format = function (fmt) {
    var o = {
        "M+": this.getMonth() + 1, //月份
        "d+": this.getDate(), //日
        "h+": this.getHours(), //小时
        "m+": this.getMinutes(), //分
        "s+": this.getSeconds(), //秒
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度
        "S": this.getMilliseconds() //毫秒
    };
    if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
}
//========================util E=================================


//========================collect S=================================

//ajax 上报日志
var _pushCollectLog = function () {
    var json = JSON.stringify(_paramLogs);
    _paramLogs.collect_word = '';
    _paramLogs.collect_id = '';
    _paramLogs.collect_type = 'click';
    $.ajax({
        url: '/collectlog/info.ajax',
        data: {json: json},
        type: 'post',
        dataType: 'json'
    }).then(function (ret) {
        console.log('ajax 上报日志 结果 :' + JSON.stringify(ret));
    });
};

//获取RequestUrl
var _requestUrl = function () {
    return window.location.href;
};

//获取RefererUrl
var _refererUrl = function () {
    var referrer = '';

    try {
        referrer = window.top.document.referrer;
    } catch (e) {
        if (window.parent) {
            try {
                referrer = window.parent.document.referrer;
            } catch (e2) {
                referrer = '';
            }
        }
    }
    if (referrer === '') {
        referrer = document.referrer;
    }
    return referrer;
};

// json 参数
var _paramLogs = {
    "source_type": "pc",
    "collect_type": 'click',
    "collect_key": '',
    "collect_word": '',
    "collect_id": '',
    "u_request_url": _requestUrl(),
    "u_referer_url": _refererUrl(),
    "u_agent": navigator.userAgent,
    "gen_time": (new Date()).Format("yyyy-MM-dd hh:mm:ss")
};


//========================collect E=================================


</script>
<script type="text/javascript" src="/static/js/sea-modules/jquery/1.11.3/jquery.js?v=d5aebfc6" charset="utf-8"></script>
<!--[if lt IE 9]>
<script>(function(tags){for(var i=0; i<tags.length; i++)document.createElement(tags[i]);})(["article","aside","details","figcaption","figure","footer","header","hgroup","nav","section","menu","video"]);</script>
<![endif]-->


    <script>
        var _hmt = _hmt || [];
        (function() {
            var hm = document.createElement("script");
            hm.src = "https://hm.baidu.com/hm.js?ddf0d99bc06024e29662071b7fc5044f";
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(hm, s);
        })();
    </script>
</head>
<body>
<div>
    <!--公共tab头部 s-->
    <!--王遥  头部导航 s-->
    <div class="header-9">
        <div class="header-inner-9">
            <div class="logo-9">
                <a href="#" class="innotree-logo">
                    <img src="/static/inno/img/innotree-logo.png" alt="因果树logo,因果树标识" />
                </a>
            </div>
            <div class="nav-9">
                <ol>
                    <li class=" snl"><a href="/">首页</a></li>
                    <li class="on snl" index="0"><a href="/inno/database/totalDatabase">创投数据库</a></li>
                    <li class=" snl" index="1"><a href="/inno/insight/newChain">数据洞察</a></li>
                    <li class=" snl"><a href="/inno/report/">行业研报</a></li>
                    <li class=" snl"><a href="/inno/static/solution">定制解决方案</a></li>
                    <li class=" snl"><a href="/inno/static/about_company">关于我们</a></li>
                </ol>
            </div>

            <input type="hidden" value="" />

            

            <div class="inno-h-us ">
                
                    <a href="/inno/static/about_member" class="ihus_links">试用会员</a>
                    <div class="ihus_tips">
                        试用会员剩余天数7天
                    </div>
                

            </div>
            <div class="log-h-9">
                
                    <div class="u_f_i_login">
                        <div class="u_f_i_lu">
                            <a href="/inno/user/message" class="u_f_i_name" style="top: 2px;">
                                
                                <img src="/static/inno/img/defloathead.png" alt="因果树用户" />
                            </a>
                            <nav class="u_f_i_nav">
                                <div class="u_photo_and_name">
                                    
                                    <img src="/static/inno/img/defloathead.png" alt="因果树用户" />
                                    <span class="i_uname">tree</span>
                                </div>
                                <a href="/inno/user/message">我的消息</a><br />
                                <a href="/inno/user/change.html?ref=%2Finno%2Fdatabase%2FtotalDatabase">修改密码</a><br />
                                <a href="javascript:void(0);" class="j_init_logout">退 出</a><br />
                            </nav>
                        </div>
                        <div class="u_f_i_ls">

                        </div>
                    </div>
                
            </div>
        </div>
    </div>
    <div class="sub-nav-9"></div>
    <!--王遥  头部导航 e-->
    <!--头部 e-->

    <!--内容部分 s-->
    <input id="areasName" type="hidden" value="" />
    <div class="blk20"></div>
    <div class="index_170912_con">
        <!--搜索框-->
        <div class="index_170912_d">
            <div class="blk50"></div>
            <!--搜索框-->
            <div class="list01_d houbu03">
                <!--搜索框-->
                <div class="ssk_1700915_d">
                    <a href="javascript:;" class="ssk_1700915_d_a ssk_1700915_d_a01"></a>
                    <input id="investDatabaseSearchInput" type="text" class="ssk_1700915_d_input" value="" placeholder="行业、公司、产品、投资机构、tag（多tag使用空格隔开）" />
                    <a href="javascript:;" class="ssk_1700915_d_a ssk_1700915_d_a4">搜索</a>
                </div>
            </div>
            <div class="blk10"></div>
            <!--大家都在搜-->
            <div id="hotKeysDiv" class="index_170912_d01_d03" style="padding-left:5px;"><span class="index_170912_d01_d03_s02">热搜：</span><a href="javascript:;" data_value="人工智能" data_name="人工智能">人工智能</a><a href="javascript:;" data_value="消费升级" data_name="消费升级">消费升级</a><a href="javascript:;" data_value="区块链" data_name="区块链">区块链</a></div>
        </div>
        <!--过滤-->
        <div class="list01_d01_ov02">
            <div class="blk15"></div>
            <!--地区-->
            <div class="list01_d01" id="areaDiv"><span class="list01_d01_s01">地区：</span><div class="list01_d01_cen"><table><tbody><tr><td><a href="javascript:;" data_value="" data_name="" class="list01_d01_cen_a list01_d01_cen_a01 list01_d01_cen_a_select">全部</a> </td><td><div class="list01_d01_cen_d list01_d01_cen_d_ov"><a href="javascript:;" class="list01_d01_cen_a" data_value="301" data_name="北京市">北京市</a><a href="javascript:;" class="list01_d01_cen_a" data_value="302" data_name="天津市">天津市</a><a href="javascript:;" class="list01_d01_cen_a" data_value="303" data_name="上海市">上海市</a><a href="javascript:;" class="list01_d01_cen_a" data_value="304" data_name="重庆市">重庆市</a><a href="javascript:;" class="list01_d01_cen_a" data_value="305" data_name="河北省">河北省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="306" data_name="山西省">山西省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="307" data_name="内蒙古自治区">内蒙古自治区</a><a href="javascript:;" class="list01_d01_cen_a" data_value="308" data_name="辽宁省">辽宁省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="309" data_name="吉林省">吉林省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="310" data_name="黑龙江省">黑龙江省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="311" data_name="江苏省">江苏省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="312" data_name="浙江省">浙江省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="313" data_name="安徽省">安徽省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="314" data_name="福建省">福建省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="315" data_name="江西省">江西省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="316" data_name="山东省">山东省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="317" data_name="河南省">河南省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="318" data_name="湖北省">湖北省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="319" data_name="湖南省">湖南省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="320" data_name="广东省">广东省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="321" data_name="广西壮族自治区">广西壮族自治区</a><a href="javascript:;" class="list01_d01_cen_a" data_value="322" data_name="海南省">海南省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="323" data_name="四川省">四川省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="324" data_name="贵州省">贵州省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="325" data_name="云南省">云南省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="326" data_name="西藏自治区">西藏自治区</a><a href="javascript:;" class="list01_d01_cen_a" data_value="327" data_name="陕西省">陕西省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="328" data_name="甘肃省">甘肃省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="329" data_name="青海省">青海省</a><a href="javascript:;" class="list01_d01_cen_a" data_value="330" data_name="宁夏回族自治区">宁夏回族自治区</a><a href="javascript:;" class="list01_d01_cen_a" data_value="331" data_name="新疆维吾尔自治区">新疆维吾尔自治区</a></div></td></tr></tbody></table></div><div class="list01_d01_right"><a href="javascript:;" class="list01_d01_right_a"></a></div></div>
            <!--轮次-->
            <div class="list01_d01" id="roundDiv"><span class="list01_d01_s01">轮次：</span><div class="list01_d01_cen"><table><tbody><tr><td><a href="javascript:;" data_value="" data_name="" class="list01_d01_cen_a list01_d01_cen_a01 list01_d01_cen_a_select">全部</a> </td><td><div><a href="javascript:;" class="list01_d01_cen_a" data_value="1-2" data_name="种子期">种子期<p class="list01_171115_p01"><span>种子期</span>包括种子轮、天使轮</p></a><a href="javascript:;" class="list01_d01_cen_a" data_value="3-4-5-6-7-8" data_name="早期">早期<p class="list01_171115_p01 list01_171115_p02"><span>早期</span>包括Pre-A轮、A轮、A+轮、Pre-B轮、B轮、B+轮</p></a><a href="javascript:;" class="list01_d01_cen_a" data_value="9-10-11-12-13-14" data_name="成长期">成长期<p class="list01_171115_p01"><span>成长期</span>包括Pre-C轮、C轮、C+轮、Pre-D轮、D轮、D+轮</p></a><a href="javascript:;" class="list01_d01_cen_a" data_value="15-16-17-18-19" data_name="成熟期">成熟期<p class="list01_171115_p01"><span>成熟期</span>包括E轮、F轮、G轮、H轮、Pre-IPO</p></a><a href="javascript:;" class="list01_d01_cen_a" data_value="20-21" data_name="新三板">新三板</a><a href="javascript:;" class="list01_d01_cen_a" data_value="40" data_name="IPO上市及以后">IPO上市及以后</a><a href="javascript:;" class="list01_d01_cen_a" data_value="50" data_name="战略并购">战略并购</a><a href="javascript:;" class="list01_d01_cen_a" data_value="60" data_name="战略投资">战略投资</a></div></td></tr></tbody></table></div><div class="list01_d01_right"></div></div>
        </div>

        <div class="houbu_170929_d01">
            <!--搜索结果-->
            <div class="disan_171010_d01" style="display: block;">
                <table>
                    <tbody><tr>
                        <td>
                            <span class="disan_171010_d01_s01">共搜索<span class="disan_171010_d01_s02" id="totalNumSpan">2000万+</span>条结果</span>
                        </td>
                        <td>
                            <span class="disan_171010_d01_s03" style="display: none;">当前条件:</span>
                        </td>
                        <td>
                            <span id="areaTagSpan"></span>
                            <span id="roundTagSpan"></span>
                            <span id="searchTagSpan"></span>
                        </td>
                    </tr>
                </tbody></table>
            </div>

            <div id="tableLoadingDiv" class="force_mb" style="text-align: center; position: inherit; display: none;">
                <div class="force_lording" style="margin: 150px 0;">
                    <table>
                        <tbody>
                        <tr>
                            <td></td>
                            <td></td>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!--页内导航-->
            <div class="disan_171010_d02" style="display: block;">
                <!--选中状态添加 CLASS = disan_171010_d02_a_select01-->
                <a id="companyTabAHref" href="javascript:;" class="disan_171010_d02_a01 disan_171010_d02_a_select01" onclick="doDrawTableForSeparate(1)">
                    <!--坚分隔线-->
                    <span class="disan_171010_d02_s01 "></span>
                    公司(<span id="companyNumSpan">2000万+</span>)
                </a>
                <!--选中状态添加 CLASS = disan_171010_d02_a_select02-->
                <a id="institutionTabAHref" href="javascript:;" class="" onclick="doDrawTableForSeparate(2)">
                    <!--坚分隔线-->
                    <span class="disan_171010_d02_s01 "></span>
                    机构(<span id="institutionNumSpan">2万+</span>)
                </a>
                <!--选中状态添加 CLASS = disan_171010_d02_a_select02-->
                <a id="searchTagTabAHref" href="javascript:;" class="" onclick="doDrawTableForSeparate(3,true)" style="display: none;">
                    细分行业(<span id="searchTagNumSpan">0</span>)
                </a>
            </div>
            <div id="compListDiv" style="">
                
<!--表格-->
<div class="houbu_170929_d02">
    <table>
        <tbody><tr class="houbu_171010_tr01" id="compTableTitleDiv">
            <td>
                <span>公司</span>
            </td>
            <td>
                <span id="sFdateCompSpan" style="cursor:pointer">最近融资时间</span>
                <div class="houbu_171010_d03_02" id="sFdateCompDiv">
                <!--上下翻页-->
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_top_select -->
                    <a href="javascript:;" class="houbu_171010_d03_top"></a>
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_down_select -->
                    <a href="javascript:;" class="houbu_171010_d03_down houbu_171010_d03_down_select"></a>
                </div>
            </td>
            <td>
                <span>所在地</span>
            </td>
            <td>
                <span id="sRoundCompSpan" style="cursor:pointer">轮次</span>
                <!--上下翻页-->
                <div class="houbu_171010_d03_01" id="sRoundCompDiv">
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_top_select -->
                    <a href="javascript:;" class="houbu_171010_d03_top"></a>
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_down_select -->
                    <a href="javascript:;" class="houbu_171010_d03_down"></a>
                </div>
            </td>
            <td>
                <span id="sEdateCompSpan" style="cursor:pointer">成立时间</span>
                <!--上下翻页-->
                <div class="houbu_171010_d03_03" id="sEdateCompDiv">
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_top_select -->
                    <a href="javascript:;" class="houbu_171010_d03_top"></a>
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_down_select -->
                    <a href="javascript:;" class="houbu_171010_d03_down"></a>
                </div>
            </td>
            <td>
                <span>融资金额</span>
            </td>
            <td>
                <span>投资者</span>
            </td>
        </tr>
        </tbody><tbody id="compTable"><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/company/4957871552628651946.html" class="company_detail_a"> <div class="houbu_170929_d02_img"> <img src="https://innotreelogo.qiniu.innotree.cn/Fk-5x2MdQm61XBMneKzGUVzrMmks" alt="" /> </div> </a><div class="houbu_170929_d02_d01"> <a href="javascript:;" xhref="/inno/company/4957871552628651946.html" class="houbu_171010_h3 company_detail_a">企加云</a> </div> </td><td> <span>2017/12/07</span> </td><td> <span class="houbu_170929_d02_s01">浙江省</span> </td><td> <span>A轮</span> </td><td> <span>2017/07/20</span> </td><td> <span>数千万人民币</span> </td><td><span style="color:#4a4a4a;display:block;">阿里巴巴（领投）</span><a href="javascript:;" xhref="/inno/institution/detail/4329168920910488212.html" class="houbu_170929_d02_a02 institution_detail_a">银杏谷资本</a><a href="javascript:;" xhref="/inno/institution/detail/7651192705518434119.html" class="houbu_170929_d02_a02 houbu_170929_d02_a02_01 institution_detail_a">元璟资本</a></td></tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/company/6354892653699219687.html" class="company_detail_a"> <div class="houbu_170929_d02_img"> <img src="https://innotreelogo.qiniu.innotree.cn/FqXPsWFyl-m9mUjZiv2zj6VRXFPo" alt="" /> </div> </a><div class="houbu_170929_d02_d01"> <a href="javascript:;" xhref="/inno/company/6354892653699219687.html" class="houbu_171010_h3 company_detail_a">富勒FLUX</a> </div> </td><td> <span>2017/12/07</span> </td><td> <span class="houbu_170929_d02_s01">上海市</span> </td><td> <span>战略投资</span> </td><td> <span>2004/12/21</span> </td><td> <span>未透露</span> </td><td><span style="color:#4a4a4a;display:block;">霍尼韦尔</span></td></tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/company/10548078748520937734.html" class="company_detail_a"> <div class="houbu_170929_d02_img"> <img src="https://innotreelogo.qiniu.innotree.cn/Fs8sk6PYMJ5U0jJwrgockE-mDJS1" alt="" /> </div> </a><div class="houbu_170929_d02_d01"> <a href="javascript:;" xhref="/inno/company/10548078748520937734.html" class="houbu_171010_h3 company_detail_a">唐人医药</a> </div> </td><td> <span>2017/12/07</span> </td><td> <span class="houbu_170929_d02_s01">河北省</span> </td><td> <span>战略投资</span> </td><td> <span>2003/04/01</span> </td><td> <span>亿元及以上人民币</span> </td><td><span style="color:#4a4a4a;display:block;">广发信德-广发证券</span><a href="javascript:;" xhref="/inno/institution/detail/3051956329191817401.html" class="houbu_170929_d02_a02 institution_detail_a">国创投资</a></td></tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/company/1183084103595171085.html" class="company_detail_a"> <div class="houbu_170929_d02_img"> <img src="https://innotreelogo.qiniu.innotree.cn/FnkkWORkkEG0fIF47mMxKNreX_fE" alt="" /> </div> </a><div class="houbu_170929_d02_d01"> <a href="javascript:;" xhref="/inno/company/1183084103595171085.html" class="houbu_171010_h3 company_detail_a">帛珑</a> </div> </td><td> <span>2017/12/07</span> </td><td> <span class="houbu_170929_d02_s01">广东省</span> </td><td> <span>A轮</span> </td><td> <span>2016/07/05</span> </td><td> <span>数百万人民币</span> </td><td><span style="color:#4a4a4a;display:block;">Michael Diekmann</span></td></tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/company/999980423478866118.html" class="company_detail_a"> <div class="houbu_170929_d02_img"> <img src="https://innotreelogo.qiniu.innotree.cn/FpkSIaay3OBeM91QkCO5riDn2GdE" alt="" /> </div> </a><div class="houbu_170929_d02_d01"> <a href="javascript:;" xhref="/inno/company/999980423478866118.html" class="houbu_171010_h3 company_detail_a">盟科医药</a> </div> </td><td> <span>2017/12/07</span> </td><td> <span class="houbu_170929_d02_s01">--</span> </td><td> <span>D轮</span> </td><td> <span>2007/07/30</span> </td><td> <span>1亿人民币</span> </td><td><span style="color:#4a4a4a;display:block;">德联资本（领投）</span><a href="javascript:;" xhref="/inno/institution/detail/15094401582630113851.html" class="houbu_170929_d02_a02 institution_detail_a">百奥财富</a></td></tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/company/10005682308130865808.html" class="company_detail_a"> <div class="houbu_170929_d02_img"> <img src="https://innotreelogo.qiniu.innotree.cn/FsR-qnw7jsNvW2pIIiTft-XUAm-3" alt="" /> </div> </a><div class="houbu_170929_d02_d01"> <a href="javascript:;" xhref="/inno/company/10005682308130865808.html" class="houbu_171010_h3 company_detail_a">云途腾</a> </div> </td><td> <span>2017/12/07</span> </td><td> <span class="houbu_170929_d02_s01">北京市</span> </td><td> <span>B+轮</span> </td><td> <span>2014/07/11</span> </td><td> <span>1.08亿人民币</span> </td><td><span style="color:#4a4a4a;display:block;">复星锐正资本（领投）</span><span style="color:#4a4a4a;display:block;">前海母基金</span></td></tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/company/7609729055695446200.html" class="company_detail_a"> <div class="houbu_170929_d02_img"> <img src="https://innotreelogo.qiniu.innotree.cn/FhrYl_FpoPSW0C0F9cI9CD3z4Njn" alt="" /> </div> </a><div class="houbu_170929_d02_d01"> <a href="javascript:;" xhref="/inno/company/7609729055695446200.html" class="houbu_171010_h3 company_detail_a">国大药房</a> </div> </td><td> <span>2017/12/07</span> </td><td> <span class="houbu_170929_d02_s01">上海市</span> </td><td> <span>战略投资</span> </td><td> <span>2004/03/23</span> </td><td> <span>4.18亿美元</span> </td><td><span style="color:#4a4a4a;display:block;">Walgreens</span></td></tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/company/12044156300577152751.html" class="company_detail_a"> <div class="houbu_170929_d02_img"> <img src="https://innotreelogo.qiniu.innotree.cn/FuhBlsv64JhgDjYu-FsF3KCOFJjB" alt="" /> </div> </a><div class="houbu_170929_d02_d01"> <a href="javascript:;" xhref="/inno/company/12044156300577152751.html" class="houbu_171010_h3 company_detail_a">盛开体育</a> </div> </td><td> <span>2017/12/07</span> </td><td> <span class="houbu_170929_d02_s01">北京市</span> </td><td> <span>B轮</span> </td><td> <span>2009/11/24</span> </td><td> <span>3亿人民币</span> </td><td><span style="color:#4a4a4a;display:block;">曜为资本（领投）</span></td></tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/company/4020570908260780691.html" class="company_detail_a"> <div class="houbu_170929_d02_img"> <img src="https://innotreelogo.qiniu.innotree.cn/FmHq3QMKqq8A7Hek-W-TeZavXdbd" alt="" /> </div> </a><div class="houbu_170929_d02_d01"> <a href="javascript:;" xhref="/inno/company/4020570908260780691.html" class="houbu_171010_h3 company_detail_a">TransferEasy</a> </div> </td><td> <span>2017/12/07</span> </td><td> <span class="houbu_170929_d02_s01">北京市</span> </td><td> <span>A轮</span> </td><td> <span>2014/03/14</span> </td><td> <span>数千万人民币</span> </td><td><a href="javascript:;" xhref="/inno/institution/detail/13836158857061946547.html" class="houbu_170929_d02_a02 institution_detail_a">真格基金</a></td></tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/company/10151547046756713819.html" class="company_detail_a"> <div class="houbu_170929_d02_img"> <img src="https://innotreelogo.qiniu.innotree.cn/FlpnPzR4dkjqn_JlohHf9g99P-V5" alt="" /> </div> </a><div class="houbu_170929_d02_d01"> <a href="javascript:;" xhref="/inno/company/10151547046756713819.html" class="houbu_171010_h3 company_detail_a">青芒果旅行网</a> </div> </td><td> <span>2017/12/07</span> </td><td> <span class="houbu_170929_d02_s01">广东省</span> </td><td> <span>Pre-C轮</span> </td><td> <span>2012/10/17</span> </td><td> <span>未透露</span> </td><td><span style="color:#4a4a4a;display:block;">逍遥资本</span></td></tr></tbody>
    </table>
</div>
<!--翻页-->
<div id="pagebas1">
    <div class="blk40"></div>
    <div class="fanye_170829_d" id="compPageDiv"><a href="javascript:;" data-page="1" class="fanye_170829_d_a_ho">首页</a><a href="javascript:;" data-page="0" class=""> &lt; </a><a href="javascript:;" data-page="1" class="fanye_170829_d_a_ho">1</a><a href="javascript:;" data-page="2" class="">2</a><a href="javascript:;" data-page="3" class="">3</a><a href="javascript:;" data-page="4" class="">4</a><a href="javascript:;" data-page="5" class="">5</a><a href="javascript:;" data-page="2" class=""> &gt; </a><a href="javascript:;" data-page="999" class="">尾页</a></div>
    <div class="blk60"></div>
</div>


<div id="companyEmptyResultDiv" style="display:none;position:relative;width:100%;box-sizing:border-box;color:#4a4a4a;background-color:#f6f6f6;">
    
        <div class="null_cyl" style="background-color: white;min-height: 176px;">
            <img src="/static/turing_app/photos/null_picture.png" alt="查询结果为空" class="null_cyl_p" style="width: 34px;height: 38px;margin: 54px 533px auto 533px;" />
            <p style="color: #666666;margin-bottom: 61px;font-size: 13px;">暂无数据</p>
        </div>
</div>

            </div>
            <div id="instListDiv" style="display:none">
                

<!--表格-->
<div class="screen_170913_02_d">
    <table>
        <tbody><tr class="houbu_171010_tr01" id="instTableTitleDiv" style="border-bottom:1px solid #eaeaea;">
            <td>
                <span>机构简称</span>
            </td>
            <td>
                <span id="sInumInstSpan" style="cursor:pointer">投资笔数</span>
                <!--上下翻页-->
                <div class="houbu_171010_d03_04" id="sInumInstDiv">
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_top_select -->
                    <a href="javascript:;" class="houbu_171010_d03_top"></a>
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_down_select -->
                    <a href="javascript:;" class="houbu_171010_d03_down houbu_171010_d03_down_select"></a>
                </div>
            </td>
            <td>
                <span id="sEnumInstSpan" style="cursor:pointer">退出笔数</span>
                <!--上下翻页-->
                <div class="houbu_171010_d03_04" id="sEnumInstDiv">
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_top_select -->
                    <a href="javascript:;" class="houbu_171010_d03_top"></a>
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_down_select -->
                    <a href="javascript:;" class="houbu_171010_d03_down"></a>
                </div>
            </td>
            <td>
                <span>投资类型</span>
            </td>
            <td>
                <span id="sEdateInstSpan" style="cursor:pointer">成立时间</span>
                <!--上下翻页-->
                <div class="houbu_171010_d03_04" id="sEdateInstDiv">
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_top_select -->
                    <a href="javascript:;" class="houbu_171010_d03_top"></a>
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_down_select -->
                    <a href="javascript:;" class="houbu_171010_d03_down"></a>
                </div>
            </td>
            <td>
                <span>管理基金</span>
            </td>
        </tr>
        </tbody><tbody id="instTable"><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/institution/detail/17619418719641586365.html" class="institution_detail_a"><div class="screen_170913_02_d_img"> <img src="https://innotreelogo.qiniu.innotree.cn/FvAklv7qXVjkjKyLRnDVD_nqZfpR" alt="" /> </div> <h3 class="screen_170929_h3_01 screen_170913_02_ov">红杉中国</h3> </a> </td><td> <span>622</span> </td><td> <span>72</span> </td><td> <span>VC</span> </td><td> <span>2005-09-01</span> </td><td> <span class="screen_170913_02_d_s screen_170913_02_ov">中国医疗科技创投基金</span> </td> </tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/institution/detail/4394508030407856536.html" class="institution_detail_a"><div class="screen_170913_02_d_img"> <img src="https://innotreelogo.qiniu.innotree.cn/FqFudW2gmLr_FtMgGja6GcuW6VxQ" alt="" /> </div> <h3 class="screen_170929_h3_01 screen_170913_02_ov">深创投</h3> </a> </td><td> <span>596</span> </td><td> <span>135</span> </td><td> <span>VC</span> </td><td> <span>1999-08-26</span> </td><td> <span class="screen_170913_02_d_s screen_170913_02_ov">康沃基金</span> </td> </tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/institution/detail/3035809194443808176.html" class="institution_detail_a"><div class="screen_170913_02_d_img"> <img src="http://7xnnx4.com2.z0.glb.qiniucdn.com/d858f2776d3a7a3cccdd7173b296b3ce" alt="" /> </div> <h3 class="screen_170929_h3_01 screen_170913_02_ov">IDG资本</h3> </a> </td><td> <span>591</span> </td><td> <span>83</span> </td><td> <span>VC</span> </td><td> <span>1992-01-01</span> </td><td> <span class="screen_170913_02_d_s screen_170913_02_ov">和谐成长二期基金</span> </td> </tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/institution/detail/10791777916155909447.html" class="institution_detail_a"><div class="screen_170913_02_d_img"> <img src="http://7xnnx4.com2.z0.glb.qiniucdn.com/b1e0e03cd2b978d91aadfe93d37a8909" alt="" /> </div> <h3 class="screen_170929_h3_01 screen_170913_02_ov">经纬中国</h3> </a> </td><td> <span>544</span> </td><td> <span>19</span> </td><td> <span>VC</span> </td><td> <span>2008-01-01</span> </td><td> <span class="screen_170913_02_d_s screen_170913_02_ov">经纬创达创投</span> </td> </tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/institution/detail/13836158857061946547.html" class="institution_detail_a"><div class="screen_170913_02_d_img"> <img src="https://innotreelogo.qiniu.innotree.cn/Fuw6FGcp2yDwjhzoWMiKFqz08ftk" alt="" /> </div> <h3 class="screen_170929_h3_01 screen_170913_02_ov">真格基金</h3> </a> </td><td> <span>478</span> </td><td> <span>6</span> </td><td> <span>早期机构</span> </td><td> <span>2012-06-04</span> </td><td> <span class="screen_170913_02_d_s screen_170913_02_ov">北京真格天创基金</span> </td> </tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/institution/detail/12136245768670158022.html" class="institution_detail_a"><div class="screen_170913_02_d_img"> <img src="/static/inno/img/bmw_05.png" alt="" /> </div> <h3 class="screen_170929_h3_01 screen_170913_02_ov">腾讯投资</h3> </a> </td><td> <span>352</span> </td><td> <span>5</span> </td><td> <span>PE</span> </td><td> <span>2011-01-01</span> </td><td> <span class="screen_170913_02_d_s screen_170913_02_ov">腾讯投资</span> </td> </tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/institution/detail/14642215689158570646.html" class="institution_detail_a"><div class="screen_170913_02_d_img"> <img src="https://innotreelogo.qiniu.innotree.cn/Fse-lgWxUIan_5quEoiXMWmEW-HL" alt="" /> </div> <h3 class="screen_170929_h3_01 screen_170913_02_ov">达晨创投</h3> </a> </td><td> <span>331</span> </td><td> <span>72</span> </td><td> <span>VC</span> </td><td> <span>2000-04-19</span> </td><td> <span class="screen_170913_02_d_s screen_170913_02_ov">达晨财信</span> </td> </tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/institution/detail/11766709392304221526.html" class="institution_detail_a"><div class="screen_170913_02_d_img"> <img src="https://innotreelogo.qiniu.innotree.cn/FpXRIlNcWQBU2-upcRSmq--1ggrH" alt="" /> </div> <h3 class="screen_170929_h3_01 screen_170913_02_ov">创新工场</h3> </a> </td><td> <span>330</span> </td><td> <span>6</span> </td><td> <span>早期机构</span> </td><td> <span>2009-09-01</span> </td><td> <span class="screen_170913_02_d_s screen_170913_02_ov">创新工场美元基金 I</span> </td> </tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/institution/detail/5755892258059912058.html" class="institution_detail_a"><div class="screen_170913_02_d_img"> <img src="https://innotreelogo.qiniu.innotree.cn/Ft55JNB9IL2Zgzwegj-hsLycmTsU" alt="" /> </div> <h3 class="screen_170929_h3_01 screen_170913_02_ov">君联资本</h3> </a> </td><td> <span>322</span> </td><td> <span>54</span> </td><td> <span>VC</span> </td><td> <span>2003-11-19</span> </td><td> <span class="screen_170913_02_d_s screen_170913_02_ov">君联致茹</span> </td> </tr><tr></tr> <tr> <td> <a href="javascript:;" xhref="/inno/institution/detail/11246582797714639477.html" class="institution_detail_a"><div class="screen_170913_02_d_img"> <img src="https://innotreelogo.qiniu.innotree.cn/FvM357wIcVOeXy3dDArXgZMJXGaJ" alt="" /> </div> <h3 class="screen_170929_h3_01 screen_170913_02_ov">险峰长青</h3> </a> </td><td> <span>293</span> </td><td> <span>2</span> </td><td> <span>天使投资</span> </td><td> <span>2010-01-01</span> </td><td> <span class="screen_170913_02_d_s screen_170913_02_ov">杭州险峰三号投资合伙企业（有限合伙）</span> </td> </tr></tbody>
    </table>
</div>
<!--翻页-->
<div id="pagebas2">
    <div class="blk40"></div>
    <div class="fanye_170829_d" id="instPageDiv"><a href="javascript:;" data-page="1" class="fanye_170829_d_a_ho">首页</a><a href="javascript:;" data-page="0" class=""> &lt; </a><a href="javascript:;" data-page="1" class="fanye_170829_d_a_ho">1</a><a href="javascript:;" data-page="2" class="">2</a><a href="javascript:;" data-page="3" class="">3</a><a href="javascript:;" data-page="4" class="">4</a><a href="javascript:;" data-page="5" class="">5</a><a href="javascript:;" data-page="2" class=""> &gt; </a><a href="javascript:;" data-page="999" class="">尾页</a></div>
    <div class="blk60"></div>
</div>

<div id="institutionEmptyResultDiv" style="display:none;position:relative;width:100%;box-sizing:border-box;color:#4a4a4a;background-color:#f6f6f6;">
    
        <div class="null_cyl" style="background-color: white;min-height: 176px;">
            <img src="/static/turing_app/photos/null_picture.png" alt="查询结果为空" class="null_cyl_p" style="width: 34px;height: 38px;margin: 54px 533px auto 533px;" />
            <p style="color: #666666;margin-bottom: 61px;font-size: 14px;">暂无数据</p>
        </div>
</div>
            </div>
            <div id="tagListDiv" style="display:none">
                

<!--tag-->

<!--表格-->
<div class="houbu_170929_d02">
    <table>
        <tbody><tr class="houbu_171010_tr01" id="tagsTableTitleDiv">
            <td>
                <span>公司</span>
            </td>
            <td>
                <span id="sFdateTagsSpan" style="cursor:pointer">最近融资时间</span>
                <!--上下翻页-->
                <div class="houbu_171010_d03_02" id="sFdateTagsDiv">
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_top_select -->
                    <a href="javascript:;" class="houbu_171010_d03_top"></a>
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_down_select -->
                    <a href="javascript:;" class="houbu_171010_d03_down"></a>
                </div>
            </td>
            <td>
                <span>所在地</span>
            </td>
            <td>
                <span id="sRoundTagsSpan" style="cursor:pointer">轮次</span>
                <!--上下翻页-->
                <div class="houbu_171010_d03_01" id="sRoundTagsDiv">
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_top_select -->
                    <a href="javascript:;" class="houbu_171010_d03_top"></a>
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_down_select -->
                    <a href="javascript:;" class="houbu_171010_d03_down"></a>
                </div>
            </td>
            <td>
                <span id="sEdateTagsSpan" style="cursor:pointer">成立时间</span>
                <!--上下翻页-->
                <div class="houbu_171010_d03_03" id="sEdateTagsDiv">
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_top_select -->
                    <a href="javascript:;" class="houbu_171010_d03_top"></a>
                    <!--如果需要选中状态， 添加CLASS =houbu_171010_d03_down_select -->
                    <a href="javascript:;" class="houbu_171010_d03_down houbu_171010_d03_down_select"></a>
                </div>
            </td>
            <td>
                <span>融资金额</span>
            </td>
            <td>
                <span>投资者</span>
            </td>
        </tr>
        </tbody><tbody id="tagsTable"></tbody>
    </table>
</div>
<!--翻页-->
<div class="fanye_170829_d" id="pagebas3" style="display: none;">
    <div class="blk40"></div>
    <div class="fanye_170829_d" id="tagsPageDiv"></div>
    <div class="blk60"></div>
</div>


<div id="tagEmptyResultDiv" style="position: relative; width: 100%; box-sizing: border-box; color: rgb(74, 74, 74); background-color: rgb(246, 246, 246);">
    
        <div class="null_cyl" style="background-color: white;min-height: 176px;">
            <img src="/static/turing_app/photos/null_picture.png" alt="查询结果为空" class="null_cyl_p" style="width: 34px;height: 38px;margin: 54px 533px auto 533px;" />
            <p style="color: #666666;margin-bottom: 61px;font-size: 14px;">暂无数据</p>
        </div>
</div>
            </div>

        </div>

    </div>
    <div style="height: 4px;"></div>
    <!--内容部分 e-->

    <!--页脚 s-->
    <div style="height:214px;clear:both;"></div>
    <div class="footer-9">
        <div class="ft-cont-9">
            <ul>
                <li><a href="/inno/static/about_company">关于InnoTREE</a></li>
                <li><a href="/inno/join_us">加入我们</a></li>
                <li><a href="/inno/static/about_member">会员体系</a></li>
                <li><a href="/inno/static/about_contact">联系我们</a></li>
                <li><a href="/inno/static/about_cooperative">合作伙伴</a></li>
            </ul>
            <p class="copyright-9">
                Copyright ©2017 InnoTREE Network Tech Co.,Ltd.
                <br />
                京ICP备 15009775号
            </p>
        </div>
    </div>
    <!--机器人 e-->
    <div class="inno_feedback">
        <a class="nomal wx" href="javascript:void(0);">
            <span class="if_icons icon-nwico_weibo2"></span> <br />
            <span class="if_wan">在 线<br />答 疑</span>
            <div class="ewm show_div o_hidden"><img src="/static/inno/photos/ewm_gzh.jpg" alt="" /></div>
        </a><br />
        <a class="nomal fx" href="javascript:void(0);" id="_fx_btn">
            <span class="if_icons icon-nwico_fenxiang"></span> <br />
            <span class="if_wan">分 享<br />本 页</span>
        </a><br />
        <a class="nomal tel" href="javascript:void(0);">
            <span class="if_icons icon-nwico_telphone"></span> <br />
            <span class="if_wan">客 服<br />电 话</span>
            <div class="tel show_div o_hidden"><span>010-53342595</span></div>
        </a><br />
        <a class="nomal fb" href="/feedback" target="_blank">
            <span class="if_icons icon-nwico_edit2"></span> <br />
            <span class="if_wan">问 题<br />反 馈</span>
        </a><br />
        <a class="nomal top" href="javascript:void(0);">
            <span class="if_icons icon-nwico_totop2"></span> <br />
            <span class="if_wan">回 到<br />顶 部</span> </a><br />
        <a class="if_main nomal rabit" href="javascript:void(0);">
            <!--<span class="if_icons icon-wico_jqr"></span> <br>-->
            <div class="c4_logo_w"></div>
            <img src="/static/inno/img/inno_feedback_jqr.gif" alt="" class="icons_jqr" />
        </a>


        <!--分享部分代码 s-->
        <div class="fx_wrap show_div hidden o_hidden">
            <div class="fx ">
                <a href="javascript:void(0)" class="close">
                    +
                </a>
                <div class="cont">
                    本页地址已复制到剪贴版，您可以粘贴到QQ/微博上 <br />
                    分享给您的好友！
                    <br class="clear" />
                    <input type="text" id="inno_fb_fx" disabled="disabled" value="http://www.innotree.cn" />
                    <br class="clear" />
                    <a href="javascript:void(0)" class="fx_btn_ok _fx_close_btn">确定</a>
                    <a href="javascript:void(0)" class="fx_btn_cancel">取消</a>
                </div>
            </div>
        </div>
    </div>

    <!--登录提示框-->
    <div class="quanju_zhezhao" style="display:none;">
        <!--提示框-->
        <div class="quanju_tc" style="position:fixed;">
            <p class="quanju_tc_title">提示:</p>
            <p class="quanju_tc_content">
                今日搜索次数达上限4次<br />
                登录后方可查看更多!<br />
            </p>
        </div>
    </div>

    <script>
        /**浮动窗 hover效果 s**/
        $("body").delegate( ".inno_feedback a", "mouseover", function(event){
            var show_div="";
            if($(this).hasClass("wx"))
                show_div=$(".inno_feedback div.ewm");
            if($(this).hasClass("tel"))
                show_div=$(".inno_feedback div.tel");
            if(show_div!=""){
                $(".inno_feedback&gt;div").addClass("o_hidden");
                show_div.removeClass("o_hidden").addClass("ani_show222");
            }
        });
        /**浮动窗 hover效果 s**/
        $("body").delegate( ".inno_feedback a", "mouseout", function(event){
            var _div=$(".inno_feedback .show_div");

            _div.each(function() {
                if($(this).hasClass("fx_wrap"))
                    return false;
                else
                    $(this).addClass("o_hidden").removeClass("ani_show222");
            });

        });
        /**浮动窗 hover效果 e**/

        /**浮动窗 点击效果 s**/
        $("body").delegate( ".inno_feedback a", "click", function(event){
            var show_div="";
            if($(this).hasClass("top")) {
                $('html,body').animate({scrollTop: '0px'}, 200);
                $('.gototop').animate({scrollTop:'0px'},200);
            }
            if($(this).hasClass("wx"))
                show_div=$(".inno_feedback div.ewm");
            if($(this).hasClass("tel"))
                show_div=$(".inno_feedback div.tel");
            if($(this).hasClass("fx")){
                var _url=window.location.href,
                    _input=$("#inno_fb_fx");
                //这里写url
                _input.val(_url);

                show_div=$(".inno_feedback div.fx_wrap");
            }
            if(show_div!=""){
                //$("#fullpage").show();
                $(".inno_feedback&gt;div").addClass("o_hidden");
                show_div.removeClass("o_hidden").removeClass("hidden");

            }
        });
        /**浮动窗 点击效果 e**/


        $("body").delegate( ".inno_feedback div.fx a", "click", function(event){
            event.preventDefault();
            var _self=$(this),
                _div=_self.parent().parent().parent();

            if(_self.hasClass("close")){
                _div=_self.parent().parent();
            }
            _div.addClass("hidden");
        });

        !function(){
            var client = new ZeroClipboard(document.getElementsByClassName("_fx_close_btn"));

            client.on("ready", function(readyEvent) {
                client.on("copy", function(event) {
                    var clipboard = event.clipboardData;
                    var copyText = window.location.href;
                    clipboard.setData("text/plain", copyText); // 将内容添加到剪切板
                });
            });
        }();
    </script>
    <script language="JavaScript">
        var submitInnoHeadBarSearch = function () {
            var query = $.trim($('#innoHeadSearchBarInput').val());
            if (!query) {
                return false;
            }
            checkSearchPop('/inno/search/toMiddleSearch?query=' + encodeURIComponent(query));

        }
        var enterSubmitInnoHeadBarSearch=function (event) {
            if (event.keyCode == 13) {
                submitInnoHeadBarSearch();
            }
        }

        $(document).on("click", ".srh-submit-9", function () {
            submitInnoHeadBarSearch();
        });
        //搜索输入的回车keyup事件
        $(document).on("keyup", "#innoHeadSearchBarInput", function (event) {
            if (event.keyCode == 13) {
                submitInnoHeadBarSearch();
            }
        });

    </script>
    <script>
        $(function(){
            var api_logout = '/ajax/uc/logout';
            $(document).on('click', ".j_init_logout", function(){
                $.post(api_logout, function (data){
                    if(data.code=="0"){
                        window.location.href = '/';
                    }else{
                        alert(data.msg);
                    }
                },"json");
            });
        });
    </script>
    <script>
        /**
         * 检查翻页权限
         */
        var checkPageNumPop = function(pageNum){
            var rid = 4;
            if (rid == 1 &amp;&amp; pageNum &gt; 1) {
                $('.quanju_zhezhao').find('.quanju_tc_content').html('未登录用户最多可查看1页&lt;br/&gt;登录后方可查看更多!&lt;br/&gt;');
                $('.quanju_zhezhao').show();
                setTimeout(function(){
                    $('.quanju_zhezhao').hide();
                    location.href = '/inno/user/login.html?ref='+'%2Finno%2Fdatabase%2FtotalDatabase';
                }, 3000);
                return false;
            }
            return true;
        };
        /**
         * 检查搜索权限（用于头部搜索框弹窗）
         */
        var checkSearchPop = function (targetUrl) {
            var rid = 4;
            if (targetUrl !== null || targetUrl !== undefined || targetUrl !== '') {
                var check = '/inno/user/preCheck';
                $.ajax({
                    url: check,
                    data: {
                        targetUrl: targetUrl
                    },
                    dataType: 'json',
                    success: function (ret) {
                        if (ret.code == 0 &amp;&amp; ret.data) {
                            var data = ret.data;
                            if (data.checked) {
                                location.href = targetUrl;
                            } else {
                                if (rid == 1) {
                                    $('.quanju_zhezhao').find('.quanju_tc_content').html('今日搜索已达上限'+data.times+'条&lt;br/&gt;登录后方可查看更多!&lt;br/&gt;');
                                    $('.quanju_zhezhao').show();
                                    setTimeout(function(){
                                        $('.quanju_zhezhao').hide();
                                        location.href = '/inno/user/login.html?ref='+'%2Finno%2Fdatabase%2FtotalDatabase';
                                    }, 3000);
                                } else {
                                    $('.quanju_zhezhao').find('.quanju_tc_content').html('今日搜索已达上限'+data.times+'条&lt;br/&gt;升级会员后方可查看更多!&lt;br/&gt;');
                                    $('.quanju_zhezhao').show();
                                    setTimeout(function(){
                                        $('.quanju_zhezhao').hide();
                                        location.href = '/inno/static/about_member';
                                    }, 3000);
                                }
                            }
                        }
                    },
                    error: function (errData) {
                        console.error(errData);
                    }
                })
            }
        }
        /**
         * 检查页内搜索权限（用于列表页搜索弹窗）
         */
        var checkAjaxSearchPop = function (targetUrl, fn) {
            var rid = 4;
            if (targetUrl !== null || targetUrl !== undefined || targetUrl !== '') {
                var check = '/inno/user/preCheck';
                $.ajax({
                    url: check,
                    data: {
                        targetUrl: targetUrl
                    },
                    dataType: 'json',
                    async: false,
                    success: function (ret) {
                        if (ret.code == 0 &amp;&amp; ret.data) {
                            var data = ret.data;
                            if (data.checked) {
                                fn();
                            } else {
                                if (rid == 1) {
                                    $('.quanju_zhezhao').find('.quanju_tc_content').html('今日搜索已达上限'+data.times+'条&lt;br/&gt;登录后方可查看更多!&lt;br/&gt;');
                                    $('.quanju_zhezhao').show();
                                    setTimeout(function(){
                                        $('.quanju_zhezhao').hide();
                                        location.href = '/inno/user/login.html?ref='+'%2Finno%2Fdatabase%2FtotalDatabase';
                                    }, 3000);
                                } else {
                                    $('.quanju_zhezhao').find('.quanju_tc_content').html('今日搜索已达上限'+data.times+'条&lt;br/&gt;升级会员后方可查看更多!&lt;br/&gt;');
                                    $('.quanju_zhezhao').show();
                                    setTimeout(function(){
                                        $('.quanju_zhezhao').hide();
                                        location.href = '/inno/static/about_member';
                                    }, 3000);
                                }
                            }
                        }
                    },
                    error: function (errData) {
                        console.error(errData);
                    }
                })
            }
        }

        /**
         * 检查公司/机构详情页访问权限（用于访问公司详情前弹窗）
         */
        var checkDetailPop = function (targetUrl) {
            var rid = 4;
            if (targetUrl !== null || targetUrl !== undefined || targetUrl !== '') {
                var check = '/inno/user/preCheck';
                $.ajax({
                    url: check,
                    data: {
                        targetUrl: targetUrl
                    },
                    dataType: 'json',
                    async: false,
                    success: function (ret) {
                        if (ret.code == 0 &amp;&amp; ret.data) {
                            var data = ret.data;
                            if (data.checked) {
                                openwin(targetUrl);
                            } else {
                                if (rid == 1) {
                                    $('.quanju_zhezhao').find('.quanju_tc_content').html('未登录用户最多可查看'+data.times+'条&lt;br/&gt;登录后方可查看更多!&lt;br/&gt;');
                                    $('.quanju_zhezhao').show();
                                    setTimeout(function(){
                                        $('.quanju_zhezhao').hide();
                                        location.href = '/inno/user/login.html?ref='+'%2Finno%2Fdatabase%2FtotalDatabase';
                                    }, 3000);
                                } else {
                                    $('.quanju_zhezhao').find('.quanju_tc_content').html('普通用户最多可查看'+data.times+'条&lt;br/&gt;升级会员后方可查看更多!&lt;br/&gt;');
                                    $('.quanju_zhezhao').show();
                                    setTimeout(function(){
                                        $('.quanju_zhezhao').hide();
                                        location.href = '/inno/static/about_member';
                                    }, 3000);
                                }
                            }
                        }
                    },
                    error: function (errData) {
                        console.error(errData);
                    }
                })
            }
        }
        /**
         * 弹窗
         * @param  {string} url 跳转链接
         */
        function gotoUrl(url){
            var a = $('&lt;a href="'+ url +'" target="_blank"&gt;链接&lt;/a&gt;');  //生成一个临时链接对象
            var d = a.get(0);
            var e = document.createEvent('MouseEvents');
            e.initEvent( 'click', true, true );  //模拟点击操作
            d.dispatchEvent(e);
            a.remove();   // 点击后移除该对象
        }
        function openwin(url) {
            var a = document.createElement("a");
            a.setAttribute("href", url);
            a.setAttribute("target", "_blank");
            a.setAttribute("id", "camnpr");
            document.body.appendChild(a);
            a.click();
        }

    </script>

    <script type="text/javascript" src="/static/js/lib/underscore-min.js?v=543feb1e" charset="utf-8"></script><script type="text/javascript" src="/static/inno/js/common/pagination.js?v=4e94509a" charset="utf-8"></script><script type="text/javascript" src="/static/inno/js/common/printScreenings.js?v=d41c5cca" charset="utf-8"></script><script type="text/javascript" src="/static/inno/js/common/mapUtil.js?v=29d643d2" charset="utf-8"></script><script type="text/javascript" src="/static/inno/js/common/constantMap.js?v=4051bda7" charset="utf-8"></script><script type="text/javascript" src="/static/inno/js/common/roundsTable.js?v=5a97226f" charset="utf-8"></script><script type="text/javascript" src="/static/inno/js/databasesearch/companySearchResult.js?v=ff3755dc" charset="utf-8"></script><script type="text/javascript" src="/static/inno/js/databasesearch/institutionSearchResult.js?v=b3225ec2" charset="utf-8"></script><script type="text/javascript" src="/static/inno/js/databasesearch/tagsSearchResult.js?v=5fcb8750" charset="utf-8"></script><script type="text/javascript" src="/static/inno/js/databasesearch/totalDatabaseV3.js?v=2fbd1272" charset="utf-8"></script>
    <script language="JavaScript">
        $(document).ready(function () {
            var initFun = function () {
                //初始化热搜词
                ajaxDrawHotKeys();
                //初始化筛选条
                ajaxDrawScreenings();
                //绑定筛选条事件
                bindScreeningClick();
                //绑定搜索框事件
                bindInvestDBSearchBtn();
                //绑定分页点击事件
                bindPaginationClick();
                //绑定排序点击事件
                bindSortClick();
                //绑定列表点击事件
                bindDetailClick();
                //
                bindHotKeys();
                // 画筛选条件
                query = $(".ssk_1700915_d_input").val();
                
                var chainName="";
                if(!isEmptyValue(chainName)){
                    fchain=1;
                }
                var tagObj = {tagName: query, tagValue: query};
                //有query时判断权限
                if (!isEmptyValue(query)) {
                    checkAjaxSearchPop('/inno/search/ajax/getAllSearchResult', function(){
                        addScreeningTag(tagObj, 3);
                        doDrawTableForTotal();
                    });
                } else {
                    if(areasName != ""){
                        tagObj.tagName = areasName;
                        tagObj.tagValue = areasName;
                        addScreeningTag(tagObj, 1);
                        doDrawTableForSeparate(1);
                    }else{
                        addScreeningTag(tagObj, 3);
                        doDrawTableForTotal();
                    }
                }
            }
            initFun();
        });
    </script>

<script>
    "use strict";
    var ops={
        "_html" : [
           // ' &lt;ul&gt; &lt;li&gt; &lt;a href="/inno/database/companyList"&gt; &lt;img src="/static/inno/img/comdb.png" alt="公司数据库"&gt; &lt;br&gt; &lt;span&gt;公司数据库&lt;/span&gt; &lt;/a&gt; &lt;/li&gt; &lt;li&gt; &lt;a href="/inno/database/investDeliveryList"&gt; &lt;img src="/static/inno/img/dban.png" alt="投资速递"&gt; &lt;br&gt; &lt;span&gt;投资速递&lt;/span&gt; &lt;/a&gt; &lt;/li&gt; &lt;li&gt; &lt;a href="/inno/database/superStarList"&gt; &lt;img src="/static/inno/img/supsta.png" alt="超新星"&gt; &lt;br&gt; &lt;span&gt;超新星&lt;/span&gt; &lt;/a&gt; &lt;/li&gt; &lt;li&gt; &lt;a href="/inno/database/institutionList"&gt; &lt;img src="/static/inno/img/orgdb.png" alt="机构数据库"&gt; &lt;br&gt; &lt;span&gt;机构数据库&lt;/span&gt; &lt;/a&gt; &lt;/li&gt; &lt;/ul&gt; ',
            ' &lt;ul&gt; &lt;li&gt; &lt;a href="/inno/database/companyList"&gt; &lt;img src="/static/inno/img/comdb.png" alt="公司数据库"&gt; &lt;br&gt; &lt;span&gt;公司数据库&lt;/span&gt; &lt;/a&gt; &lt;/li&gt; &lt;li&gt; &lt;a href="/inno/database/investDeliveryList"&gt; &lt;img src="/static/inno/img/dban.png" alt="投资速递"&gt; &lt;br&gt; &lt;span&gt;投资速递&lt;/span&gt; &lt;/a&gt; &lt;/li&gt;  &lt;li&gt; &lt;a href="/inno/database/institutionList"&gt; &lt;img src="/static/inno/img/orgdb.png" alt="机构数据库"&gt; &lt;br&gt; &lt;span&gt;机构数据库&lt;/span&gt; &lt;/a&gt; &lt;/li&gt; &lt;/ul&gt; ',
            ' &lt;ul&gt; &lt;li&gt; &lt;a href="/inno/insight/newChain"&gt; &lt;img src="/static/inno/img/innochain.png" alt="产业链"&gt; &lt;br&gt; &lt;span&gt;产业链&lt;/span&gt; &lt;/a&gt; &lt;/li&gt;  &lt;li&gt; &lt;a href="/inno/insight/cloudmap"&gt; &lt;img src="/static/inno/img/innocmap.png" alt="云地图"&gt; &lt;br&gt; &lt;span&gt;云地图&lt;/span&gt; &lt;/a&gt; &lt;/li&gt; &lt;li&gt; &lt;a href="/inno/insight/bigdata/industry_matrix.html"&gt; &lt;img src="/static/inno/img/innobdata.png" alt="行业大数据"&gt; &lt;br&gt; &lt;span&gt;行业大数据&lt;/span&gt; &lt;/a&gt; &lt;/li&gt; &lt;/ul&gt; '
        ],
        "$nav" : $('.sub-nav-9'),
        "$li": $('.nav-9 ol li.mul'),
        "$snl":$('.nav-9 ol li.snl')

    };

    wy88y();
    function wy88y() {
        ops.$li.mouseenter(
            function() {
                var e = $(this).addClass("hover"),
                    i = $(this).attr("index"),
                    o = ops.$nav;
                o .attr("index",i)
                    .html('')
                    .html(ops._html[i])
                    .addClass("anti-h");
            }).mouseleave(function() {
                ops.$li.removeClass("hover");
            }),
            ops.$snl.mouseenter(
                function() {
                    ops.$nav.removeClass("anti-h");
                }),
            ops.$nav.mouseenter(function() {
                var i = $(this).attr('index');
                $(this).addClass("anti-h");
                ops.$li.each(function(){
                    if(i===$(this).attr("index"))
                        $(this).addClass("hover");
                });
            }).mouseleave(function() {
                $(this).removeClass("anti-h");
                ops.$li.removeClass("hover");
            })
    }

    //密码睁眼闭眼效果
    $(".fw-epwd").click(function () {
        var _self = $(this);
        if(_self.hasClass("close")){
            _self.removeClass("close")
        }
        else{
            _self.addClass("close")
        }
    });

</script>


</div></body></html>
"""