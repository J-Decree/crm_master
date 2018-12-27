import string

FAMILY_NAME_LIST = ['曹', '赵', '关', '张', '赵', '刘', '诸葛', '司马', '郑', '韩',
                    '孙', '吴', '陈', '郭', '崔', '钟', '吕', '贾', '杨', '邓']

NAME_WORD = '''
陶万艳陶万雪陶三蓉陶专英陶世妹
陶世媛陶世莹陶丛玥陶之玥陶乐冉陶习茹陶习
莉陶习莹陶书玥陶二蓉陶云婵陶云莹陶亦娟陶亦
琴陶亦萍陶亿英陶仔怡陶仙婧陶仙文陶仙琳陶仙萍
陶仙雪陶仟倩陶仟茹陶以霞陶仪娜陶仲雪陶优美陶
传莹陶佐萍陶余悦陶佩雪陶依娟陶侦媛陶俏玉陶俐
冉陶俣倩陶俪婧陶俪颖陶倩宏陶倩沁陶倩洳陶倩璐
陶倩芯陶倩菱陶儒玉陶克燕陶其倩陶其燕陶其蓉陶冉
玲陶军倩陶冼妹陶净芳陶刘英陶初霞陶制燕陶加媛陶
卉倩陶厚丽陶厚琴陶原红陶原霞陶发美陶叔丽陶名冉
陶名琳陶君嫣陶吟莹陶含艳陶启蓉陶咨妍陶啊玉陶喜
妍陶喜玉陶喜美陶喻霞陶四蓉陶园莉陶垭萍陶基娜陶
墨丽陶墨莹陶太玉陶妍光陶妍同陶妍忮陶妍枝陶妍榛
陶妍缈陶妍翘陶妙燕陶妲倩陶妹润竦布欣乐天璞玉流
逸昕雨可琪仓艳紫杉秦峰驰涵一瑾宏伟高杰智宸楚洁
稽宏清悦珴子裕粼淙暄文忆雪彩玉河清忻愉文思旭辉
帝辉梦菲聪慧梓柔锐进姝莹白姜荣清馨盾墨歆然志诚
可然燕婉冠宇寅鑫黛娥忻欢宝华依秋松文田然兴昌宣
朗修齐良俊一帆红旭佩琳秉荃如冰霞姝可然秦剑鼎蓼
秀华真茹丽姿秀雅可俊英粟麓瀚海璧烨烨欣欣耘志柯
凡辰伟振博鸿禧曼容盈秀朕和悦翠茵鸿飞靖琪弼畴墉
绪颖萍运浩广琼岚飞语秀筠梦竹夏岚心远心桐昕妤怀
思晋荣彤贶宁鸿振飞龙维运楼之综骞尧唅唅珊宛儿智
纯伶伶昊乾桂帆依秋伟诚梓洁晨星艺菲晴丽哲兴学楚
洁黛妍和雼翔俊瑰玮宏儒亿阳曦牧歌玟希慕茂典天赋
萌阳浦泽文漪苍宇烨烨弘宥恭和品韵宗竹萱和蒲凡诗
怀凡羽冰枫苑涵涵晨达鹤轩韦柔德本墨夏萱泰华启颜
乐池驹乐怡贶宁清润悦乐慧巧阳煦宛妙涵畅曦之祺祥
问萍荣彬静涵易楠秀文子琳泽雨诗文弘济秀洁珺琦跃
升璞玉雪卉春雪高杰梓文伟茂程举存安楚楚胤文则蕊
雅洁楚洁玮泽惠职君寻芳颜琛米米慧婕欧仙仪皎洁鸿
晖寅祥越彬守仁高卓问筠欣怡驰鸿致远濡霈安妮承业
红英吉森海莹吉月浩思璞瑜俊慧建业帅红铭晨曦哲春
兰凌春文乐贶宁美偲嘉玉桐霏清心路遥亚楠慧美弓仑
'''

PASSWORD_WORD = string.ascii_letters + string.digits

CHAR_FIELD_WORD = '''
　第四封：现在就去做
　　格言：机会是靠机会得来的。
　　坏习惯能摆布我们，左右成败。它很容易养成，但却很难伺候。
　　成功地将一个好主意付诸实践，比在家空想出一千个好主意要
　　有价值得多。
　　（To conquer you have need to do，to do again，ever to do！And your
　　safety is insured。）
　　December24，1897
　　亲爱的约翰：
　　聪明人说的话总能让我记得很牢。有位聪明人说得好，“教育涵盖了许多方面，但是他本身不教你任何一面。”这位聪明人向我们展示了一条真理：如果你不采取行动，世界上最实用、最美丽、最可行的哲学也无法行得通。
　　我一直相信，机会是靠机会得来的。再好的构想都有缺陷，即使是很普通的计划，但如果确实执行并且继续发展，都会比半途而废的好计划要好得多，因为前者会贯彻始终，后者却前功尽弃。所以我说，成功没有秘诀，要在人生中取得正面结果，有过人的聪明智慧、特别的才艺当然好，没有也无可厚非，只要肯积极行动，你就会越来越接近成功。
　　遗憾的是，很多人并没有记取这个最大的教训，结果将自己沦为了平庸之辈。看看那些庸庸碌碌的普通人，你就会发现，他们都有在被动的活着，他们说的远比做的多，甚至只说不做。但他们几乎个个都是找借口的行家，他们会找各种借口来拖延，直到最后他们证明这件事不应该、没有能力去做或已经来不及了为止。
　　与这类人相比，我似乎聪明、狡猾了许多。盖茨先生吹捧我是个主动做事、自动自发的行动者。我很乐意这样的吹捧，因为我没有辜负它。积极行动是我身上的另一个标识，我从不喜欢纸上谈兵或流于空谈。因为我知道，没有行动就没有结果，世界上没有哪一件东西不是由一个个想法付诸实施所得来的。人只要活着，就必须考虑行动。
　　很多人都承认，没有智慧的基础的知识是没用的，但更令人沮丧的是即使空有知识和智慧，如果没有行动，一切仍属空谈。行动与充分准备其实可视为物体的两面。人生必须适可而止。做太多的准备却迟迟不去行动，最后只会徒然浪费时间。换句话说，事事必须有节制，我们不能落入不断演练、计划的圈套，而必须承认现实：不论计划有多周详，我们仍然不可能准确预测最后的解决方案。
　　我当然不否认计划非常重要，计划是获得有利结果的第一步，但计划并非行动，也无法代替行动。就如同打高尔夫球一样，如果没有打过第一洞，便无法到达第二洞。行动解决一切。没有行动，什么都不会发生。我们无论如何也买不到万无一失的保险，但我们可以做到的是下定决心去实行我们的计划。
　　缺乏行动的人，都有一个坏习惯：喜欢维持现状，拒绝改变。我认为这是一种深具欺骗和自我毁灭效果的坏习惯，因为一切都在变化之中，正如人会生死一样，没有不变的事物。但因内心的恐惧——对未知的恐惧，很多人抗拒改变，哪怕现状多么不令他满意，他都不敢向前跨出一步。看看那些本该事业有成，却一事无成的人，你就知道不同情他们是件很难的事。
　　是的，每个人在决定一件大事时，心里都会或多或少有些担心、恐惧，都会面对到底要不要做的困扰。但“行动派”会用决心燃起心灵的火花，想出各种办法来完成他们地心愿，更有勇气克服种种困难。
　　很多缺乏行动的人大都很天真，喜欢坐等事情自然发生。他们天真地以为，别人会关心他们的事。事实上，除了自己以外，别人对他们不大感兴趣，人们只对自己的事情感兴趣。例如一桩生意，我们获利比重越高，就要越主动采取行动，因为成败与别人的关系不大，他们不会在乎的。这时候，我们最好把它推一把，如果我们怠惰、退缩，坐等别人采取主动来推动事情的话，结果必定会令人失望。
　　一个人只有自己依靠自己，他才不会让自己失望，并能增加自己控制命运的机会。聪明人只会去促使事情发生。
　　人生中最令人感到挫折的，莫过于想做的事太多，结果不但没有足够的时间去做，反而想到每件事的步骤繁多，而被做不到的情绪所震慑，以致一事无成。我们必须承认，时间有限，任何人都无法做完所有的事情。聪明人知道，并非所有的行动都会产生好的结果，只有明智的行动才能带来有意义的结果，所以聪明人只会汲取做了以后获得正面效果的工作，做与完成最大目标有关的工作，而且专心致志，所以聪明人总能做出最有价值的贡献，并捞到很多好处。
　　要吃掉大象需要一口一口的吃，做事也是一样，想完成所有的事情，只会让机会溜掉。我的座右铭是：洛克菲勒对紧急事件采取不公平待遇。
　　很多人都是自己使自己变成一个被动者的，他们想等到所有的条件都十全十美，也就是时机对了以后才行动。人生随时都是机会，但是几乎没有十全十美的。那些被动的人平庸一辈子，恰恰是因为他们一定要等到每一件事情都百分之百的有利，万无一失以后才去做。这是傻瓜的做法。我们必须向生命妥协相信手上的正是目前需要的机会，才会将自己挡在陷入行动前永远痴痴等待的泥沼之外。
　　我们追求完美，但是人类的事情没有一件绝对完美，只有接近完美。等到所有条件都完美以后才去做，只能永远等下去，并将机会拱手让给他人。那些要等到所有事情都已经准备妥当才出发的人，将永远也离不开家。要想变成“我现在就去做”的那种人，就是停止一切白日梦，时时想到现在，从现在就开始做。诸如“明天”、“下礼拜”、“将来”之类的句子，跟“永远不可能做到”意义相同。
　　每个人都有失去自信，怀疑自己能力的时候，尤其是在逆境中的时候。但真正懂得行动艺术艺术的人，却可以用坚强的毅力克服它，会告诉自己每个人都有失败的时候，有失败得很惨的时候，会告诉自己不论事前做了多少准备、思考多久，真正着手做的时候，都有难免会犯错误。然而，被动的人，并不把失败视为学习和成长的机会，却总在告诫自己：或许我真的不行了，以致失去了积极参与未来的行动。
　　很多人都相信心想事成，但我却将其视为慌言。好主意一毛钱能买一打，最初的想法只是一连串行动的起步，接下来需要第二阶段的准备、计划和第三阶段的行动。在我们这个世界上从来不缺少有想法有主意的人，但懂得成功地将一个好主意付诸实现比在家空想出一千个好主意要有价值得多的人却很少。
　　人们用来判断你的能力的真正基础，不是你脑子里装了多少东西，而是你的行动。人们都信任脚踏实地的人，他们都会想：这个人敢说敢做，一定知道怎么做最好。我还没听过有人因为没有打扰别人、没有采取行动或要等别人下令才做事而受到赞扬的。那些在工商界、政府、军队中的领袖，都是很能干又肯干的人、百分之百主动的人。那些站在场外袖手旁观的人永远当不成领导人物。
　　不论是自动自发者还是被动的人，都是习惯使然。习惯有如绳索，我们每天纺织一根绳索，最后它粗大得无法折断。习惯的绳索不是带领我们到高峰就是引领我们到低谷，这主得看好习惯或坏习惯了。坏习惯能摆布我们、左右成败，它很容易养成，但却很难伺候。好习惯很难养成，但很容易维持下去。
　　要有现在就做的习惯，最重要的是要有积极主动的精神，戒除精神散漫的习惯，要决心做个主动的人，要勇于做事，不要等到万事俱备以后才去做，永远没有绝对完美的事。培养行动的习惯，不需要特殊的聪明智慧或专门的技巧，只需要努力耕耘，让好习惯在生活中开花结果即可。
　　儿子，人生就是一场伟大的战役，为了胜利，你需要行动，再行动，永远行动！这样，你的安全就能得到保障。
　　祝圣诞节快乐！我想没有比在此时送给你这封信，更好的圣诞礼物了。
　　爱你的父亲
　　第五封：要有竞争的决心
　　格言：我不迎接战争，我摧毁竞争者。
'''
TEXT_FIELD_WORD = '''
　爱你的父亲
　　第十五封：财富是勤奋的副产品
　　格言：我们的财富是对我们勤奋的嘉奖。
　　勤奋是为了自己，不是为了别人。
　　财富是意外之物，是勤奋工作的副产品。
　　（Let us go forward  ，firm in our faith  ，steadfast in  out purpose;butsustained by our confidence in the will of God.）
　　January 25， 1907
　　亲爱的约翰：
　　很高兴收到你的来信.在你的信中有两句话很是让我欣赏，一句是“你要不是赢家你就是在自暴自弃”，一句是 “勤奋出贵族”。这两句话是我不折不扣的人生座右铭，如果不自谦的话，我愿意说，它正是我人生的缩影。
　　那些不怀好意的报纸，在谈到我创造的巨额财富时，常比喻我是一架很有天赋的赚钱机器，其实他们对我几乎一无所知，更对历史缺乏洞见。
　　作为移民，满怀希望和勤奋努力是我们的天性。而我尚在孩童时期，母亲就将节俭、自立、勤奋、守信和不懈的创业精神等美德植入了我的骨髓。我真诚地笃信这些美德，将其视为伟大的成功信条，直到今天，在我的血液中依然流淌着这些伟大的信念。而所有的这一切结成了我向上攀爬的阶梯，将我送上了财富之山的顶端。
　　当然，那场改变美国人民命运与生活的战争，让我获益非浅，真诚地说，它将我造就成了令商界啧啧称奇而又望而生畏的商业巨人。是的，南北战争给予了民众前所未有的巨大商机，它把我提前变成了富人，为我在战后掀起的抢夺机会的竞技场上获胜，提供了资本支持，以至后来才能财源滚滚。
　　但是，机会如同时间一样是平等的，为什么我能抓住机会成为巨富，而很多人却与机会擦肩而过、不得不与贫困为伍呢？难道真的像诋毁我的人所说，是因为我贪得无厌吗？
　　不！是勤奋！机会只留给勤奋的人！自我年少时，我就笃信一条成功法则：财富是意外之物，是勤奋工作的副产品。每个目标的达成都来自于勤奋的思考与勤奋的行动，实现财富梦想也依然如此。
　　我极为推崇“勤奋出贵族”这句话，它是让我永生敬意的箴言。无论是过去还是现在，无论是在我们立足的北美还是在遥远的东方，那些享有地位、尊严、荣耀和财富的贵族，都有一颗永不停息的心，都有一双坚强有力的臂膀，在他们身上都凸显毅力也顽强意志的光芒。而正是这样的品质或称财富，让他们成就了事业，赢得了尊崇，成为了顶天立地的人物。
　　约翰，在这个无限变幻的世界中，没有永远的贵族，也没有永远的穷人。就像你所知道的那样，在我小的时候，我穿的是破衣烂衫，家境贫寒到要靠好心人来接济。但今天我已拥有一个庞大的财富帝国，已将巨额财富注入到慈善事业之中。如同万种盛衰起伏变幻如同沧海桑田，生生不息。出身卑贱和家境贫寒的人，通过自己的勤奋工作、执着的追求和智慧，同样能功成名就、出人头地，成为一人新贵族。
　　一切尊贵和荣誉都必须靠自己的创造去获取，这样的尊贵和荣誉才能长久。但在我们今天这个社会，富家子弟处在一种一种不进则退的情况之下。不幸的是，他们中的很多都缺乏进取精神，却好逸恶劳，挥霍无度，以至有很多人虽在富裕的环境中长大，却不免费在贫困中死去。
　　所以，你要教导你的孩子，要想在与人生风浪的博击中完善自己，成就自己，享受成功的喜悦，赢得社会的尊敬，高歌人生，只能凭自己的双手去创造；要让他们知道，荣誉的桂冠只会戴在那些勇于探索者的头上；告诉他们，勤奋是为了自己，不是为了别人，他们是勤奋的最大受益者。
　　我自孩提时代就坚信，没有辛勤的耕耘就不会有丰硕的确良收获，作为贫民之子，除去靠勤奋获得成功、赢得财富与尊严，别无他策。上学时，我不是一个教就会的学生，但我不甘人后，所以我只能勤恳地准备功课，并能持之以恒。在我十岁时我就知道要尽我所能地多干活，砍柴、挤奶、打水、耕种，我什么都干，而且从不惜力。正是农村艰苦而辛劳的岁月，磨练了我的意志，使我能够承受日后创业的艰辛；也让我变得更加坚忍不拔，产塑造了我坚强的自信心。
　　我知道，我之所以在以后身陷逆境时总能泰然处之，包括我的成功，在很大程度上都得益于我自小建立的自信心。
　　勤奋能修炼人的品质，更能培养人的能力。我受雇于休伊特-塔特尔公司时，我就获得了具备非同一般的能力和出众的年轻簿记员的名声。在那段日子里，我可谓是终日披星戴月、夜以继日。当时我的雇主就对我说，你一定会成功，以你这非凡的毅力。尽管我不明白将来会是什么样子，但有一点我相信，只要我用心去干一件事，我决不会失败。
　　今天，我尽管已年近七十，但我依然搏杀于商海之中，因为我知道，结束生命最快捷的方式就是什么也不做。人人都有权力选择把退休当作开始或结束。那种无所事事的生活态度会使人中毒。我始终将退休视为再次出发，我一天也没有停止过奋斗，因为我知道生命的真谛。
　　约翰，我今天的显赫地位，巨额财富不过是我付出比常人多得多的劳动和创造换来的。我原本是普普通通的常人，原本没有头上的桂冠，但我以坚强的毅力、顽强的耕耘，孜孜以求，终于功成名就。我的名誉不是虚名，是血汗浇铸的王冠，些许浅薄的嫉恨和无知的浅薄，都是对我的不公平。
　　我们的财富是对我们勤奋的嘉奖。让我们坚定信念，认定目标，凭着对上帝意志的信心，继续努力吧，我的儿子。
　　爱你的父亲
　　第十六封：不要找借口
　　格言：借口是制造失败的根源。
　　一个人越是成功，越不会找借口。
　　百分之九十九的失败都是因为人们惯于代寻借口。
　　（Ninety-nine percent of the failures come from people who have the habit ofmaking excuse.）
　　April 15，1906
　　亲爱的约翰：
　　斯科菲尔德船长又输了，他输得有些气急败坏，一怒之下把他那根漂亮的高尔夫球杆扔上了天，结果他只得再买一个新球杆了。
　　坦率地说，我比较喜欢船长的性格，人生奋斗的目标就是求胜，打球也是一样。所以，我准备买个新球杆送给他，但愿这不会被他认为是对他发脾气的奖赏，否则他一发不可收拾，我可就惨了。
　　斯科菲尔德船长还有一个令人称道的优点，尽管输球会令他不高兴，但他认为赢本身并不代表一切，而努力去赢的做法才是最重要的。所以在输球之后，他从不找借口。事实上，他可以以年龄太大、体力欠佳来解释他输球的理由，为自己讨回颜面，但他从来不这样做。
　　在我看来借口是一种思想病，而染有这种严重病症的人，无一例外的都是失败者，当然一般人也有一些轻微的症状。但是，一个人越是成功，越不会找借口，处处亨通的人，与那些没有什么作为的人之间最大的差异，就在于借口。
　　只要稍加留意你就会发现，那些没有任何作为，也不曾计划要有番作为的人，经常会有一箩筐的草帽来解释：为什么他没有做到，为什么他不做，为什么他不能做，为什么他不是那样的。失败者为自己料理“后事”的第一个举动，就是为自己的失败找出各种理由。
　　我鄙视那些善找借口的人，因为那是懦弱者的行为，我也同情那些善找借口的人，因为借口是制造失败的病源。
　　一旦一个失败者找出一种“好”的借口，他就会抓住不放，然后总是拿这个借口对他自己和他人解释：为什么他无法再做下去，为什么他无法成功。起初，他还能自知他的借口多少是在撒谎，但是在不断重复使用后，他就会越来越相信那完全是真的，相信这个借口就是他无法成功的真正原因，结果他的大脑就开始怠惰、僵化，让努力想方设法要赢的动力化为零。但他们从不愿意承认自己是个爱找借口的人。
　　偶尔，我见过有人站起来说：“我是靠自己的努力而成功的。”到目前为止，我还未见过任何男人或女人，敢于站起来说：“我是使自己失败的人。”失败者都有一套失败者的借口，他们将失败归咎于家庭、性格、年龄、环境、时间、肤色、宗教信仰、某个人乃至星象，而最坏的借口莫过于健康、才智以及运气。
　　最常见的借口，就是健康的借口，一句“我的身体不好”或“我有这样那样的病痛”，就成了不去做或失败的理由。事实上，没有一个人是完全健康的，每个人多少都会有生理上的毛病。
　　很多人会完全或部分屈服于这种借口，但是一心要成功的人则不然。盖茨先生曾为我引荐过一位大学教授，他在一次旅行中不幸失去了一条手臂，但就像我所认识的每一个乐观者一样，他还是经常微笑，经常帮助别人。那天在谈及他的残障问题时，他告诉我：“那只是一条手臂而已，当然，两个总比一个好。但是切除的只是我的手臂，我的心灵还是百分之百的完整也正常。我实在是要为此感谢。”

'''
INTEGER_RANGE = (1, 250)
FLOAT_RANGE = (100, 200)

EMAIL_POSTFIX = [
    '@163.com',
    '@sina.com',
    '@sohu.com',
    '@yahoo.com.cn',
    '@qq.com',
    '@56.com',
    '@sogou.com',
]

DATE_FILED_RANGE = {
    'year': (2015, 2018),
    'month': (1, 12),
    'day': (1, 21),
}

DATETIME_FILED_RANGE = {
    'year': (2015, 2018),
    'month': (1, 12),
    'day': (1, 21),
    'hour': (1, 23),
    'minute': (20, 50),
    'second': (1, 14),
}