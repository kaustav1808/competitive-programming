__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# Problem statement

#Sol - write down the solution in formal language

class solution:
    def sortedArray(self,a: [int], b: [int]) -> [int]:
        temp = [float("-inf")]
        i = 0
        j = 0
        t = 0

        while i<len(a) and j < len(b):
            if (a[i]<b[j]):
                if a[i] != temp[t]:
                    temp.append(a[i])
                    t +=1
                i+=1
            elif b[j] < a[i]:
                if b[j] != temp[t]:
                    temp.append(b[j])
                    t +=1
                j +=1
            else:
                if a[i] != temp[t]:
                    temp.append(a[i])
                    t +=1
                i+=1

        while i< len(a):
            if(temp[t] != a[i]) : 
                temp.append(a[i])
                t +=1
            i +=1

        while j< len(b):
            if(temp[t] != b[j]) : 
                temp.append(b[j])
                t +=1
            j +=1

        del temp[0]     

        return temp
        


def main():
    sol = solution()
    arra = [-999705662,-999579417,-993969222,-992720144,-992545835,-992432265,-989006427,-983651308,-983514564,-983373636,-981328178,-980207847,-977541677,-976069657,-974322336,-972528667,-972406484,-967638950,-967347409,-966539525,-964082156,-963178544,-961145603,-960947747,-960236004,-958275317,-957397986,-950309356,-947876464,-944575700,-941628232,-939615443,-933105359,-931236708,-931222801,-930287518,-928055296,-926662635,-918084517,-918080293,-917160177,-916965991,-916003602,-912937829,-912312057,-911820869,-909144236,-907489328,-904458999,-903008367,-900365292,-899660766,-899648953,-898425600,-893514425,-890718701,-887004997,-886792699,-886008495,-881363622,-878978887,-876313229,-875927941,-871626623,-867695305,-863408405,-860512815,-860288638,-859104025,-856977708,-852315394,-848967714,-848684492,-847953718,-846550324,-840876294,-840861605,-839999923,-839778984,-834580501,-830720755,-830605220,-827712514,-826820128,-826421262,-824562135,-823334907,-820954518,-820953824,-820125669,-817929615,-817856731,-817227052,-810915806,-808295670,-800811476,-800790527,-798465887,-796760109,-796191200,-795363030,-795213732,-791457047,-787446764,-783298972,-774240509,-772884272,-772793501,-771387433,-770362814,-770054463,-766810536,-766193381,-755000513,-754058658,-754039537,-751070455,-750170334,-740428770,-738693885,-734829886,-734490711,-729731916,-729092083,-727589880,-726550197,-725784500,-720447821,-716853959,-716703467,-715971030,-715912321,-714753288,-714620766,-711970270,-710964450,-709244316,-708219936,-707918471,-707832396,-700010451,-697410185,-696450790,-696205511,-695967451,-693608392,-692053885,-691133339,-690579699,-677790138,-671239121,-670339639,-669480725,-667627695,-666659532,-666464870,-662482830,-658780705,-658648440,-653188669,-653133618,-651865852,-651705728,-650652693,-650563884,-648529939,-646096844,-638650958,-636898172,-636202974,-633558997,-633042003,-629447658,-617892221,-604782896,-603012370,-601653599,-600269987,-598712368,-597224940,-594333183,-592665868,-586770874,-584429182,-580376882,-575992972,-571661023,-565082117,-558549248,-558042434,-557348926,-556473604,-554126197,-553718640,-550824916,-550626237,-549587937,-549105426,-549001646,-547801479,-542112023,-532795165,-532608432,-532093213,-529589441,-528779070,-528674028,-528525446,-528057906,-526998198,-522098721,-520738033,-520438094,-519066083,-513639694,-511758837,-510276177,-509671622,-508771676,-508275367,-507972868,-507807076,-505335476,-504933482,-501398774,-499935547,-498055227,-493525177,-488644790,-488043033,-483798453,-479256154,-477651841,-476774140,-467562737,-464949443,-464400457,-461735117,-458354397,-455296874,-455251690,-452534890,-450698039,-449380630,-447388370,-442282025,-440967564,-439062430,-436016369,-435830904,-435656448,-432670885,-431481293,-430736949,-427968093,-425151994,-419954844,-419582700,-419065980,-415128822,-409116060,-406197148,-396961501,-396584882,-394405690,-393008504,-392310039,-387260084,-385859413,-385371192,-384540973,-377141441,-376863813,-374236188,-372370391,-371988387,-363673034,-363135808,-356392680,-355694816,-354284149,-350203076,-350135336,-349090322,-348405400,-344688695,-343650985,-339469343,-333717110,-333157233,-332748011,-332550730,-330345709,-329278574,-328345817,-327996234,-325988957,-324598415,-322892808,-322515534,-319608403,-317919425,-315025788,-313437374,-312760207,-312169769,-304485175,-304197636,-297308104,-296956009,-296003424,-293817167,-293510603,-293496591,-292280004,-291302933,-290062870,-289796492,-274723002,-272704300,-270534983,-269533744,-268319531,-267118365,-265584172,-264931245,-264597770,-258651781,-258178902,-256921791,-250036792,-246520996,-246194373,-246107740,-238859789,-234269676,-231223846,-230781692,-230095182,-228329484,-227696512,-225774613,-222209781,-221027136,-219887170,-218000518,-216335294,-213414926,-212422966,-207310811,-206932574,-203849195,-203722946,-196097326,-194139371,-192401066,-190733884,-189463168,-189241480,-187355302,-180915241,-177920313,-177598790,-177242336,-168358997,-162579151,-152942523,-149003346,-148434008,-145643258,-145502008,-144735562,-144211282,-144096401,-142891512,-142377806,-142349099,-141894694,-139893430,-139827930,-138667818,-137484020,-135521741,-129254120,-124007568,-123849973,-116782820,-115883971,-111471546,-110868472,-109676885,-101525324,-99405195,-96962090,-95571111,-95117389,-92995781,-89667178,-88234583,-88166668,-87731593,-87582977,-87307495,-83886062,-76282111,-74408667,-73953189,-71457818,-69461700,-66024721,-64663638,-64067432,-58963693,-56317819,-56027899,-54901302,-54604152,-54135384,-54073581,-50840111,-49697210,-49341241,-44730367,-42975939,-42194853,-41342499,-40933177,-40349265,-40189103,-38647687,-38315848,-34489752,-33965149,-31380787,-28893280,-27392383,-20598480,-17783693,-17179592,-15113816,-7835625,-3806904,-1573157,-1307341,84782,2210900,4689885,5714241,8438090,8938925,19384917,19896401,23148539,23326834,28581756,30045325,39423999,44850084,47582643,49884777,51325438,52349599,52472712,52677019,57831382,64368901,66846907,67915540,70958168,72111525,74700442,75346544,79240715,79829961,87165682,94883375,99373203,101451408,103727663,110174462,112218473,113530225,118447065,119228373,122062753,127255110,130107500,130998878,133078836,136351108,136620668,139037315,139756145,142666146,152468345,155282361,155323615,156286409,157654155,161434406,161529302,165263611,168664465,169088661,170953330,173987901,181208021,186132309,186657702,189761159,193241359,194732578,197398770,198280166,198315099,200019553,201325316,203266798,205598234,211047994,213845259,219044991,222895677,226685986,229782014,231006464,232286927,232531130,234480358,235293706,235974949,236444622,242056536,247793543,253769268,255401171,264792151,268465931,270201632,271666649,277423001,278596452,280928877,281441889,282494731,283320595,287838873,296942904,301193102,301698152,304282504,306249308,306420635,308100711,308345273,308483377,309538870,309739004,312065915,313658005,316203312,317380328,318014578,327629879,328371955,329365334,334887065,335752977,337080651,337453658,337488023,338941164,339645672,343673286,347196174,350041158,354757704,355764671,356943330,359761701,367850240,371873983,372085834,373801314,376236271,378471762,379527336,381280038,385827920,386499975,388495952,402798203,405145793,407878681,411183214,414666820,415248019,416665641,417773854,418261045,418354088,421694256,425968189,429566988,430250661,431390493,435523799,436323767,436697027,445444998,446247752,446289055,447276048,447704106,449366118,454661887,456299808,457631513,462145290,462286469,464360179,465420262,467396819,467405182,468711463,473078559,474679639,476456357,478792528,480823719,481720081,483557622,485816419,487106304,491835309,493516327,496140923,500599111,500781638,503597980,503994018,504877891,508849116,515619118,517083358,520202506,520265961,525785925,526964264,529304889,534387320,534995446,537510124,541748118,543630531,544362960,551983331,552977794,557377686,561299561,566489112,568859311,572195987,573131130,577142742,582687942,583384470,585777664,585930442,589431805,590134673,594326836,594633637,596603775,600522525,601669086,602617849,609049723,610134642,610928320,611627474,611847520,614284469,615375442,618203622,618439668,620164123,621385332,622496525,626380775,632681913,633380458,633428482,635433365,640501112,644180360,644558462,647628829,648407370,649385989,649805627,650724740,654604739,656047816,658038220,659678987,660126412,664083631,666542793,667756354,671803970,678713746,681291498,684551193,690065788,692958511,697049557,699618896,700200141,700541259,700548143,700933260,703096474,707475767,711327966,714642839,717141825,718698916,720768051,722138575,722585435,722793921,723533554,724180817,727485456,728097689,729136245,731437851,731972444,733646038,734476386,734659313,736224561,738033729,738777997,739047777,739062845,739139322,741392231,741561755,742231115,742633175,743201104,750287429,750312160,750531206,751616812,753655281,756143427,758405313,759232155,763876649,767146780,767447166,770584222,770643887,770753067,772376793,773642218,779001494,779357022,780314866,784762328,785918781,787134065,790005371,790514769,790742482,791558105,791771049,796785129,796861220,797156075,801847139,803379519,805246986,806486097,810989965,820531417,822191292,822648245,827753980,832857192,832978259,833020494,834908553,835715527,837440322,837949132,839408643,842007399,842872351,843648243,845321518,848799634,849190773,849506652,849815151,850400074,852741381,853429103,853685050,854038639,858255408,858510417,863140931,866030819,866949269,867173963,868170656,870653955,871141468,872449271,872810405,874032717,876031524,876583520,880066130,883173882,886087643,889241016,889778836,890711354,891044651,892565660,895884195,896350623,901809844,903685409,904413851,905237492,905557128,906022312,908875367,910845852,910953205,912112127,912342018,915561383,915640172,916209685,916357184,917487251,924821812,928516793,929760488,930047471,930107001,932967027,934784669,937082794,946922782,948366449,949735855,951976332,955577514,957881531,960953781,963325937,964199168,966667839,971123076,978364460,979021960,985434430,987580874,988583067,993649414,996963475,997953467,998551465]
    arrb = [-998815035,-998162808,-997897920,-993481753,-987501079,-987394769,-985619452,-983633202,-983474752,-983425510,-982934489,-981414171,-980451623,-976979763,-974828788,-974523737,-974065509,-971827988,-970860944,-967643419,-962527028,-958857114,-956485171,-956405244,-954192484,-952157807,-950511528,-949920529,-949485842,-949054807,-947357154,-947152962,-946070920,-940568601,-939663637,-939150095,-937487167,-931373849,-930204879,-928142895,-927135720,-922872993,-917995539,-916529627,-912454815,-912393087,-912281611,-906500563,-905919503,-900891820,-896465662,-894131516,-889711792,-886478062,-883287051,-881970262,-876509347,-872540242,-871624993,-871066622,-867990177,-865277237,-857489911,-856840496,-856201273,-854045868,-852391305,-851448164,-849219697,-846610532,-845881751,-837503395,-834540782,-834424257,-831641786,-831040903,-830197771,-828845899,-813521493,-809899401,-808725074,-808369918,-807808533,-805022238,-804886649,-804268395,-803683929,-801045720,-797546603,-795523897,-793355841,-788193179,-787934675,-787721966,-780089831,-776710424,-776457433,-774622417,-768943215,-753474534,-752801520,-750542316,-748637896,-745257385,-742027301,-741805134,-739411227,-736884806,-736771861,-735020101,-730913219,-725841047,-725037175,-721388047,-717305132,-715639227,-712800552,-712743483,-710873992,-708382855,-706714705,-703342100,-702565418,-700726476,-698498657,-693924472,-690442668,-689487025,-688773677,-686387100,-684981203,-684963027,-684790111,-684172315,-681851325,-679230338,-678169753,-677484377,-672051143,-668908835,-667642963,-662043357,-661990394,-661880670,-660821438,-659021799,-655131344,-651511014,-644727069,-643951240,-642251414,-641403286,-641063917,-638987438,-638972681,-636587850,-632517585,-630594383,-630570333,-630327024,-627730136,-624291707,-622489064,-620594596,-620444378,-619100506,-618708418,-618261832,-618217077,-616812868,-612012243,-611786549,-610919338,-602267581,-601841682,-600994593,-592550697,-591521924,-586531362,-583959255,-582128630,-581064751,-580443344,-579558354,-578049369,-573363450,-567510656,-563736119,-563285908,-559554055,-559133558,-556884172,-551819415,-550448366,-548751621,-545533196,-543964782,-538960849,-535056624,-530315368,-528261277,-516762888,-516064842,-512045579,-508278554,-500389729,-498333733,-498235052,-494273708,-493142075,-490309994,-489655850,-488200146,-487422189,-485686494,-485265848,-482835674,-478297039,-476784842,-475647054,-469151127,-466390757,-462897933,-462319373,-461949641,-461044372,-460315334,-449496440,-445545741,-445423208,-441838999,-441507041,-440075770,-438087510,-437108846,-435339187,-431402062,-425813455,-423279184,-416483812,-413553986,-411738108,-405945092,-398643647,-398175078,-391403451,-390972731,-388065387,-385370320,-383928811,-383564287,-382329261,-379426912,-377400242,-377024737,-376542449,-375588651,-375004138,-374341113,-371941054,-368966919,-368173180,-368107693,-367882870,-366687440,-365525168,-363360885,-362244230,-361461937,-359770999,-359088293,-358909972,-355639534,-355205435,-354919201,-351914212,-351554251,-348676342,-347044846,-346249320,-342852073,-339801369,-338362207,-335960934,-335952965,-335755028,-334713388,-331244881,-331127724,-327008040,-325494071,-317997241,-316008419,-314541676,-314324904,-313327640,-312591044,-312100144,-312012867,-310013237,-308801971,-307613656,-305896235,-304776079,-303693446,-303357363,-303161650,-302773453,-302270456,-299040896,-298949682,-294505749,-293659367,-292574074,-288255866,-288228856,-286294035,-284000404,-280092662,-264417778,-258736088,-253605029,-253137882,-252314430,-250521063,-247171469,-246907295,-246221072,-246073136,-246016221,-245452738,-244151857,-242471617,-240878941,-239891713,-235195638,-234775042,-233483352,-231646475,-229947383,-229843788,-226542679,-225929106,-224643769,-219999471,-216940515,-207649021,-205781675,-200923853,-199911488,-198434909,-197507764,-197130899,-190479090,-184809623,-183257480,-183081636,-182968899,-176370630,-176269772,-174483213,-170674729,-170129385,-169029680,-165686914,-161476521,-156649479,-155425059,-154795275,-147323062,-144608852,-139952380,-139902715,-136522050,-136065334,-135290142,-132048387,-128094992,-123742412,-123718233,-120110035,-118966763,-116741701,-109381930,-107623553,-102172395,-101321790,-99675966,-98055381,-94097741,-93378166,-92074045,-89474532,-88331240,-84810158,-82029659,-81526657,-81208435,-80092624,-79869918,-75058608,-74394433,-71804361,-69530731,-58272928,-57093347,-56300142,-55857018,-53942170,-52782973,-52320173,-51997658,-51476256,-51296664,-51001457,-49720261,-46235113,-43235747,-42776581,-41855309,-35891544,-35124511,-34991562,-31759416,-31703931,-30061878,-28889851,-28840418,-27518749,-24696306,-23497459,-21627778,-21310742,-20631485,-18079496,-17526037,-17199232,-13316175,-11682579,-11044550,-10843897,-9955077,-3158856,507285,3244524,4663101,6813856,11064144,14168650,16544310,18000454,19627195,33026799,36809261,37327394,40273676,40417702,41087844,42247958,43022321,48233171,48965386,52551896,53182025,53979525,56056660,59256400,62273227,63661516,64231969,65096881,66308481,66470445,68196128,69468467,75059398,77098489,77535735,78697974,79531957,85703284,89255906,97205669,98999434,99604118,99799057,100413955,103869684,104233993,105794844,106061987,107612097,110183789,111093710,120676526,123131506,123844496,126102505,128551054,129177473,129905602,136196782,136459978,138442316,142272324,143726453,146576605,147005083,147292092,151740458,154174560,159883972,167796185,171864652,173322165,175858229,177982926,178986232,181621842,193717877,194094594,205137291,209868454,210561554,212172155,215513448,217830808,217888523,225543184,226364713,226838599,227843722,227985773,231482897,231743080,234663042,236903025,242972185,246662568,246708907,249495522,252968085,254703781,256422834,256591501,265167090,268625723,269023386,269951868,272453751,275270641,278269956,280871614,283916791,285092616,285669559,287404971,287442616,291332875,293113054,297055018,297179202,298413505,299008666,305399915,306322215,307024390,309685320,312503610,315987548,318599790,331464485,331487149,334609951,334975243,335030422,341638424,342352407,343611825,346677439,347417539,349248856,350995468,352888249,357623116,359412256,359437937,360042984,360242480,360754228,367614382,368115639,368829449,369752184,371442841,371462604,371584056,372950246,374853128,381033912,381497123,382977648,384581617,384746199,387647270,388202736,389098043,389541510,389701252,390160918,390357966,393567988,394613080,395265593,395807052,396417894,396503721,397257984,397753208,406267361,406865939,409306112,410226726,410431746,417333707,417566657,419594054,420248465,421090493,421372032,423485397,426321045,427254733,427759603,429390041,434362217,434855170,435011994,437292285,444532715,446827067,447087788,448896383,455135305,460479017,465392316,469791751,470818636,473472726,474733140,475319215,476385881,478914056,480081042,484427014,486163510,488092010,488097455,488887778,489708549,491966292,494289714,496881599,497313880,498046699,499414135,501049392,501320810,502020234,502869221,504004329,505301146,507075580,508327769,508951950,509358769,510524609,512653737,514012730,515129393,518865056,520407683,521833340,522495720,526766653,526830293,527811936,533859601,535590223,538212136,540582856,541455971,543009292,544238756,546274230,550315141,551432540,552224548,554895028,555191827,556627226,558700549,559493610,560473011,563578949,565540544,568984280,570421904,571551880,571701898,573694571,574967466,576767084,577763380,580922031,582386984,586419118,593811535,597722689,601299006,607352471,610721131,611257032,613658407,616408905,617289001,618379364,620786251,622943718,629096249,631680777,633379401,634557257,637417805,642410778,644834633,645330437,645498763,651403013,651623243,656089033,656363209,658970554,660786461,675647641,676768413,677250996,678589483,680003032,680151042,682089235,683002535,683715473,687278610,688175639,691416536,695475274,697334748,699204510,707760940,711156281,714151336,722293146,724149189,724618528,727349002,727870335,729394731,729767874,736394074,738256585,742652139,743737126,743902554,744405966,744839307,746366013,747199739,747940005,748036576,748538214,751853367,752740147,755107448,756691091,760931818,761627695,765506012,769775729,773441738,773883719,774559517,779844732,781237883,788705681,793084765,796904888,798611949,799061857,799864065,800690511,800783905,803515837,805164571,805566055,806969047,807864682,812321902,813481170,814541063,815323859,816386018,818074712,819570650,826757617,834792867,838177199,841627132,842421774,843644242,846167541,847744604,848398669,850687479,853060368,853414313,854770316,856430761,858653296,859038648,865027721,870503430,871598090,874106285,875092252,879308768,880091467,881658069,882655360,887293611,887330997,888112482,893049371,897919837,898277504,902538075,903232003,903914780,904868317,905222524,911085769,911234174,912218213,917207152,917841487,918515289,920990562,922267914,924075038,927835853,928511689,931367718,937791498,938168784,938802176,941046949,941600767,944621568,945602375,948446883,949730708,958152982,960951937,961613691,966855366,969380719,970181131,978283209,983516972,984198249,984619872,988919559,989513087,993031068,995067333,995920643,996660467,996796961,997135054,999390289]    

    print(sol.sortedArray(arra, arrb))

if __name__ == "__main__":
    main()

