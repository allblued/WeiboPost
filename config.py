# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:36:33 2018

@author: star
"""
TODAY_TARGET_COUNT=80 #今日目标帖子回复帖子数
#留言文字内容列表
MESSAGE=[
    r"#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 当世界从华丽到荒芜，请放心我还是你的粉丝@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html",
    r"#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 就算荧光棒成了拐杖，你也依旧是我的信仰@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html",
    r"#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 你在哪，心在哪。没想过如影随形，但想过永生不弃@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html",
    r"#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 心疼你的心疼，感受你的感受，你的微笑是我快乐的通行号@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html",
    r"#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 陪伴是最长情的告白，思念是最真心的等待@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html",
    r"#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 明天太阳依旧升起，转角我们能否相遇?@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html",
    r"#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 我承认我很花心，你的每个样子我都很喜欢@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html",
    r"#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 你一定不知道自己的微笑，可以拯救我的全世界@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html",
    r'#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 我喜欢春天的花夏天的树秋天的风冬天的雪和每天的你@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 世界有万千种脸孔，偏偏却对你的笑容情有独钟。@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 比起天黑和鬼,我更怕你心酸皱眉@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 路有多长我就陪你走多远毫无怨忿绝不皱一下眉头@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 我想你的存在就是为了证明我并不是三分钟热度@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 我想把世界上最好的都给你,世界上最好的就是你@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 感谢你如此耀眼，做我平淡岁月里的星辰。@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# @Dear-迪丽热巴 就算荧光棒成了拐杖，你也依旧是我的信仰。https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# @Dear-迪丽热巴 天若有情天亦老，为@Dear-迪丽热巴 打榜好不好？https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# @Dear-迪丽热巴老夫聊发少年狂，左安利，右打榜。一心一意，全力助@Dear-迪丽热巴 上榜。https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# @Dear-迪丽热巴 喜欢你的人很多，不缺我一个；但我爱的人很少，只有你@Dear-迪丽热巴 一个! https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# @Dear-迪丽热巴 我还是很喜欢你，像鲸沉于海底轻柔呼吸，痴极嗔极#迪丽热巴# https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# @Dear-迪丽热巴 时间，能暴露谎言，能改变距离，更能看清人心，我相信时间，也相信你@Dear-迪丽热巴https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'#迪丽热巴一千零一夜# #迪丽热巴凌凌七# 年年月月、日日夜夜、分分秒秒，为 @Dear-迪丽热巴 打call！最好的数据给最好的 #迪丽热巴# ！https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html',
    r'我喜欢一种朴实🌺叫李慧珍。[br]我喜欢一种痴情🌸叫白凤九。[br]我喜欢一种任性🌷叫高雯。[br]我喜欢一种强悍💐叫关小迪。[br]我喜欢一种勇敢🌹叫公孙丽🌷。[br]我喜欢一种绝世美，叫倾城。[br]我喜欢一种活泼🌺叫楼兰公主🌹；[br]喜欢一种真实😊叫迪丽热巴·迪力木拉提！！[br]热巴，我爱你！[br]6.25 一千零一夜@Dear-迪丽热巴 ',
    r"#迪丽热巴# #迪丽热巴一千零一夜# #迪丽热巴凌凌七# 爱上你不是因为你多好，只是因为某一天某一瞬间某一眼，命中注定我会爱上你@Dear-迪丽热巴 https://v.qq.com/x/cover/6qwt97k9auzlv48/e002611cg4z.html",
    r'吾心向迪，永不分离。[br]❥#迪丽热巴#&nbsp;[br]❥#迪丽热巴烈火如歌#&nbsp;[br]❥#迪丽热巴一千零一夜#&nbsp;[br]❥#迪丽热巴三生三世枕上书#&nbsp;[br]❥#迪丽热巴凌凌七#&nbsp;[br]❥#迪丽热巴白凤九#&nbsp;[br]❥#迪丽热巴刘佳音#&nbsp;[br]❥#迪丽热巴的贴吧粉绝不认输#&nbsp;[br]2018继续陪伴！@Dear-迪丽热巴'
]
#转发列表
MID_LIST=[
    '4252637912697109',
    '4249091351523845',
    '4248395486527432',
    '4246975836602682',
    '4246054025188645'
]