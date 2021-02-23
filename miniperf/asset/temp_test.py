from u3driver import AltrunUnityDriver
from u3driver import By
import time
import random
import re
import datetime
import pages
from pages import phase_treasure_test
from pages import phase_field_test
from pages import phase_secret_fire_test
from pages import phase_secret_test
from pages import phase_battlefield_test
from pages import phase_killer_test
from pages import phase_time_test
from pages import phase_five_elements_test
from pages import phase_answer_test
from pages import phase_CheckBag_test

def log_to_file(message):
    now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(now + '   ' + message)
    with open("TestCastLog.txt", "a",encoding="utf-8") as f:
        f.write(message+"\n")

def PartLogin(udriver):
    try:
        print("----------------开始登陆案例（少林）--------------")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UILoginChannelInner//imgBG//btnSelectZone").tap()
        print("选择大区")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISelectZone//imgBG//ZoneList//ZoneList//Element1").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UILoginChannelInner//imgBG//btnEnterGame").tap()
        print("进入游戏")
        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIAgreement//imgBG//btnAgree"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIAgreement//imgBG//btnAgree").tap()
            time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UILoginServer//imgBG//PanelServer//btnChange").tap()
        print("选择服务器")
        time.sleep(2)
        # udriver.find_object(By.PATH, "//UIModule//Group1//UILoginServer//imgBG//btnAgreement").tap()
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIAgreement//imgBG//btnAgree"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIAgreement//imgBG//btnAgree").tap()
            time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISelectServer//imgBG//PanelKindList//MaskView//List//Element2").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISelectServer//imgBG//PanelServerList//MaskView//List//Element2").tap()
        print("选择2服")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UILoginServer//imgBG//PanelServer//btnChange").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISelectServer//imgBG//PanelServerList//MaskView//List//Element1").tap()
        print("选择1服")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UILoginServer//imgBG//btnLoginServer").tap()
        print("进入游戏")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISelectRole//imgBG//imgSelectRole//btnRole1").tap()
        print("选择门派：少林")
        time.sleep(2)
        try:
            udriver.find_object(By.PATH, "//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
            print("随机取名")
        except:
            raise Exception("当前已有角色")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISelectRole//imgBG//btnCreateRole").tap()
        print("创建角色")
        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIMessageBox//imgBG//btnCenter"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIMessageBox//imgBG//btnCenter").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UISelectRole//imgBG//PanelCreateRole//btnRandRoleName").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UISelectRole//imgBG//btnCreateRole").tap()
            time.sleep(2)
        print("----------------登陆案例（少林）完成--------------")

    except Exception as e:
        print(f"{e}")
        raise Exception("----------------登陆案例（少林）错误--------------")

def PartOne(udriver):
    try:
        uiauto = u2.connect(udriver.appium_driver)
        w, h = udriver.get_screen()
        w = int(w)
        h = int(h)
        time.sleep(2)
        print("--- 主线任务（1-10级）---")
        log_to_file("---主线任务（1~10级）---")
        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIBanner//imgBG//btnClose1"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIBanner//imgBG//btnClose1").tap()
            time.sleep(2)
        val1 = (350 / 2232) * w
        val2 = (820 / 1080) * h
        val3 = (700 / 2232) * w
        val4 = (300 / 1080) * h
        uiauto.swipe(val1, val2, val3, val4, 0.5)
        print(uiauto.info)
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
        # print("主线-初入江湖")
        # log_to_file("主线-初入江湖")
        name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
        task_name = re.search(r'(?<=])(.*)(?=<)', name)
        print("主线-" + str(task_name.group(0)))
        log_to_file("主线-" + str(task_name.group(0)))
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                time.sleep(1)
                if not udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    break
        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
            time.sleep(1)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
            time.sleep(1)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
            time.sleep(2)

        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
        #print("主线-了解流派")
        #log_to_file("主线-了解流派")
        name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
        task_name = re.search(r'(?<=])(.*)(?=<)', name)
        print("主线-" + str(task_name.group(0)))
        log_to_file("主线-" + str(task_name.group(0)))
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
        print("GM跳过师门任务与野叟任务")
        log_to_file("GM跳过师门任务与野叟任务")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//btnGM").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element1//txtParamTip1//inputParam1").tap()
        time.sleep(2)
        udriver.find_object(By.PATH,"//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element1//txtParamTip1//inputParam1").set_text("/? Task:Test_SetIgnorTaskFlag(me, 1)")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element1//txtDesc//btnExecute").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//btnClose").tap()

        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                time.sleep(1)
                if not udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    break
        time.sleep(3)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
            time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSkill").tap()
        print("武功指引")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISkill//imgBG//FactionSect//maskLayer//paneBG//Element2").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        print("切换功法")
        time.sleep(2)

        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
        # print("主线-小试身手")
        # log_to_file("主线-小试身手")
        name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
        task_name = re.search(r'(?<=])(.*)(?=<)', name)
        print("主线-" + str(task_name.group(0)))
        log_to_file("主线-" + str(task_name.group(0)))
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                time.sleep(1)
                if not udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    break
        time.sleep(3)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        print("战斗指引")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//btnSwitch").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightSkill//imgBG//btnMedicine").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIMedicineShop//UIBg//MedicineBuyPanel//btnBuy").tap()
        print("购买药品")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        time.sleep(2)
        try:
            val1 = (2160 / 2340) * w
            val2 = (660 / 1080) * h
            uiauto.long_click(val1, val2, 2)
            print("长按药品")
            time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
                time.sleep(2)
            else:
                val1 = (2180 / 2340) * w
                val2 = (660 / 1080) * h
                uiauto.long_click(val1, val2, 2)
                print("长按药品")
                time.sleep(1)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
                    time.sleep(2)
                else:
                    val1 = (2280 / 2340) * w
                    val2 = (660 / 1080) * h
                    uiauto.long_click(val1, val2, 2)
                    print("长按药品")
                    time.sleep(1)
                    if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn"):
                        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
                        time.sleep(2)
                    else:
                        val1 = (2200 / 2340) * w
                        val2 = (660 / 1080) * h
                        uiauto.long_click(val1, val2, 2)
                        print("长按药品")
                        time.sleep(1)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        except Exception:
            print(f"{e}")
            log_to_file("长按药品错误")
            raise Exception("长按药品错误")
        time.sleep(4)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
        while True:
            time.sleep(3)
            task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
            if "白猪" not in task:
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
                break
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                time.sleep(1)
                if not udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    break
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
        time.sleep(3)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        print("技能升级指引")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSkill").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISkill//imgBG//FactionSkillView//group//DaChengSkill//Element1//btnAddPoint").tap()
        print("升级技能")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISkill//imgBG//FactionSkillView//group//QuickAdd//imgBG//btnQuickAdd").tap()
        print("一键升级")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISkill//imgBG//btnClose").tap()
        time.sleep(3)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        print("加点指引")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//btnRoleHead").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIBag//imgBG//AttributePanel//PotencyPanel//PotentialPointObj//btnAddPotential").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIAddPotentialPoint//imgBG//btnGroup//btnRecommend").tap()
        print("推荐加点")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIAddPotentialPoint//imgBG//btnGroup//btnAdd").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIAddPotentialPoint//imgBG//btnClose").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIBag//imgBG//btnClose").tap()
        time.sleep(3)

        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
        # print("主线-小渔救父")
        # log_to_file("主线-小渔救父")
        name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
        task_name = re.search(r'(?<=])(.*)(?=<)', name)
        print("主线-" + str(task_name.group(0)))
        log_to_file("主线-" + str(task_name.group(0)))
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                break
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
        time.sleep(2)

        udriver.find_object(By.PATH,"//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
        # print("主线-品格证明")
        # log_to_file("主线-品格证明")
        name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
        task_name = re.search(r'(?<=])(.*)(?=<)', name)
        print("主线-" + str(task_name.group(0)))
        log_to_file("主线-" + str(task_name.group(0)))
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn"):
                break
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        print("任务指引")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//ButtonGroup//ToggleTask").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UITask//imgBG//panelDetail//btnGo").tap()
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element2"):
                text = udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options/Element2//Text").get_text()
                if text == "我要做其它事情":
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                else:
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element2").tap()
            elif udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                break
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
        time.sleep(2)

        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
        # print("主线-木人试炼")
        # log_to_file("主线-木人试炼")
        name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
        task_name = re.search(r'(?<=])(.*)(?=<)', name)
        print("主线-" + str(task_name.group(0)))
        log_to_file("主线-" + str(task_name.group(0)))
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                break
        while True:
            time.sleep(3)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
            else:
                break
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
            else:
                break
        udriver.find_object(By.PATH, "//UIModule//Group1//AchievementDisplay//node//btnGain").tap()
        print("领取奖励")

        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
            time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        print("自动补药指引")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//btnList//btnSkill").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//panelSkill//Content//LeftRouletteMedicineSetting//maskLayer//panelBG//toggleReplyMedicine").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//btnClose").tap()
        time.sleep(1)
        level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
        Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
        print("当前等级" + " " + str(level) + "," + str(Exp))
        log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
        print("--- 主线任务（1-10级）完成---")
        log_to_file("---主线任务（1~10级）完成---")
        time.sleep(2)

    except Exception as e:
        print(f"{e}")
        log_to_file("*** 主线任务（1~10级）错误 ***")
        raise Exception("*** 主线任务（1~10级）错误 ***")

def PartTwo(udriver):
    try:
        print("--- 师门任务 ---")
        log_to_file("--- 师门任务 ---")
        time.sleep(1)
        task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
        if "龙五" not in task:
            print("师门任务已跳过")
            log_to_file("师门任务已跳过")
        else:
            log_to_file("师门任务未跳过")
            raise Exception("师门任务未跳过")
        time.sleep(1)
        level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
        Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
        print("当前等级" + " " + str(level) + "," + str(Exp))
        log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
        time.sleep(1)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
        print("GM等级升至15级")
        log_to_file("GM等级升至15级")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//btnGM").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").tap()
        time.sleep(2)
        udriver.find_object(By.PATH,  "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").set_text("15")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtDesc//btnExecute").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//btnClose").tap()
        time.sleep(1)
        level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
        Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
        print("当前等级" + " " + str(level) + "," + str(Exp))
        log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
        print("--- 师门任务完成---")
        log_to_file("---师门任务完成---")
        time.sleep(2)

    except Exception as e:
        print(f"{e}")
        log_to_file("*** 师门任务错误 ***")
        raise Exception("*** 师门任务错误 ***")

def PartThree(udriver):
    try:
        print("--- 主线任务/支线任务10001、10014（15~18级） ---")
        log_to_file("--- 主线任务/支线任务10001、10014（15~18级） ---")
        time.sleep(1)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
        # print("主线-一个蛮人")
        # log_to_file("主线-一个蛮人")
        name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
        task_name = re.search(r'(?<=])(.*)(?=<)', name)
        print("主线-" + str(task_name.group(0)))
        log_to_file("主线-" + str(task_name.group(0)))
        while True:
            time.sleep(2)
            # task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            else:
                task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                if "玄悲" not in task:
                    time.sleep(2)
                    break
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            else:
                task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                if "玄悲" in task:
                    break
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH,  "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            else:
                udriver.find_object(By.PATH,"//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
                break
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH,  "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                break
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
            time.sleep(2)

        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
        # print("主线-塔林夺经")
        # log_to_file("主线-塔林夺经")
        name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
        task_name = re.search(r'(?<=])(.*)(?=<)', name)
        print("主线-" + str(task_name.group(0)))
        log_to_file("主线-" + str(task_name.group(0)))
        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIYeSouTaskPanel//btnClose"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIYeSouTaskPanel//btnClose").tap()
            time.sleep(2)
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                break
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIYeSouTaskPanel//btnClose"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIYeSouTaskPanel//btnClose").tap()
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
            print("同伴招募指引")
            time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnPartner").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIPartner//BG//btnList//btnCardPicking").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIPartner//panelCardPicking//GoldPanel//btnGoldFreePick").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UICardPickingResult//ClickEmpty").tap()
        time.sleep(3)
        udriver.find_object(By.PATH, "//UIModule//Group1//UICardPickingResult//ClickEmpty").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIPartner//BG//btnList//btnPartner").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIPartner//panelPartnerMain//PartnerInfo//UILoopScrollView//Viewport//Content//Element1//togFight").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIPartner//btnClose").tap()
        time.sleep(2)

        if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIYeSouTaskPanel//btnClose"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIYeSouTaskPanel//btnClose").tap()
            time.sleep(2)

        log_to_file("支线10001-装备强化")
        if udriver.find_object_in_range_where_text_contains("txtTitle", "装备强化", "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//panelOtherTask//Content"):
            name = udriver.find_object_in_range_where_text_contains("txtTitle", "装备强化", "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//panelOtherTask//Content")
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//panelOtherTask//Content//" + name + "//btnTrack").tap()
            print("支线10001-装备强化")
        else:
            log_to_file("支线10001-装备强化未开启")
            raise Exception("支线10001-装备强化未开启")
        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIYeSouTaskPanel//btnClose"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIYeSouTaskPanel//btnClose").tap()
            time.sleep(2)
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn"):
                break
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        print("装备强化指引")
        time.sleep(2)
        try:
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//btnBag").tap()
        except:
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnBag").tap()
        time.sleep(2)
        one = udriver.find_child("//UIModule//Group1//UIBag//imgBG//BagPanel//bagBackground//maskView//imgInventory")[0]
        # name = one['name']
        udriver.find_object(By.PATH, "//UIModule//Group1//UIBag//imgBG//BagPanel//bagBackground//maskView//imgInventory//" + one +"//UIItemGrid//ItemLayer").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIEquipTips//imgBG//btnGroup//btn1").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIBag//imgBG//BagPanel//UIEquipPanel//EquipPanel//PanelEquip//Armor//UIItemGrid//ItemLayer").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIEquipTips//imgBG//btnGroup//btn2").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIEquipment//node//EnhancePanel//btnEnhance").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//AchievementDisplay//node//btnGain").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIEquipment//node//btnClose").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIBag//imgBG//btnClose").tap()
        time.sleep(2)

        print("支线任务10014-你问我答")
        phase_answer_test.AutoRun(udriver)
        print("--- 主线任务/支线任务10001、10014（15~18级）完成 ---")
        log_to_file("--- 主线任务/支线任务10001、10014（15~18级）完成 ---")
        time.sleep(2)

    except Exception as e:
        print(f"{e}")
        log_to_file("*** 主线任务/支线任务10001、10014（15~18级）错误***")
        raise Exception("*** 主线任务/支线任务10001、10014（15~18级）错误***")

def PartFour(udriver):
    try:
        print("--- 野叟任务 ---")
        log_to_file("--- 野叟任务 ---")
        while True:
            time.sleep(2)
            task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
            if "玄因" in task:
                print("野叟任务已跳过")
                log_to_file("野叟任务已跳过")
                break
            elif "请先把等级" in task:
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
                print("等级未到20级，GM等级升至20级")
                log_to_file("等级未到20级，GM等级升至20级")
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//btnGM").tap()
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").tap()
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").set_text("20")
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtDesc//btnExecute").tap()
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//btnClose").tap()
            else:
                log_to_file("野叟任务未跳过")
                raise Exception("野叟任务未跳过")
                break
        level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
        Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
        print("当前等级" + " " + str(level) + "," + str(Exp))
        log_to_file("当前等级" + " " + str(level) + "," + str(Exp))

        print("--- 野叟任务完成 ---")
        log_to_file("--- 野叟任务完成 ---")
        time.sleep(2)

    except Exception as e:
        print(f"{e}")
        log_to_file("*** 野叟任务错误 ***")
        raise Exception("*** 野叟任务错误 ***")

def PartFive(udriver):
    try:
        print("--- 主线任务/支线任务10013（20~22级） ---")
        log_to_file("--- 主线任务/支线任务10013（20~22级） ---")
        time.sleep(1)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
        # print("主线-寂灭二僧")
        # log_to_file("主线-寂灭二僧")
        name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
        task_name = re.search(r'(?<=])(.*)(?=<)', name)
        print("主线-" + str(task_name.group(0)))
        log_to_file("主线-" + str(task_name.group(0)))
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                break
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
            time.sleep(2)

        log_to_file("支线10013-披风加身")
        if udriver.find_object_in_range_where_text_contains("txtTitle", "披风加身", "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//panelOtherTask//Content"):
            name = udriver.find_object_in_range_where_text_contains("txtTitle", "披风加身", "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//panelOtherTask//Content")
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//panelOtherTask//Content//" + name + "//btnTrack").tap()
            print("支线10013-披风加身")
        else:
            log_to_file("支线10013-披风加身未开启")
            raise Exception("支线10013-披风加身未开启")
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                break
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
            time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        print("拜师指引")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudChat//imgBG//bottomChat//btnFriend").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISocial//node//imgBG//btnList//btnMaster").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UISocial//node//imgBG//btnClose").tap()
        time.sleep(1)
        level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
        Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
        print("当前等级" + " " + str(level) + "," + str(Exp))
        log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
        print("--- 主线任务/支线任务10013（20~22级）完成 ---")
        log_to_file("--- 主线任务/支线任务10013（20~22级）完成 ---")
        time.sleep(2)

    except Exception as e:
        print(f"{e}")
        log_to_file("*** 主线任务/支线任务10013（20~22级）错误***")
        raise Exception("*** 主线任务/支线任务10013（20~22级）错误***")

def PartSix(udriver):
    try:
        print("--- 龙脉任务 ---")
        log_to_file("--- 龙脉任务 ---")
        phase_treasure_test.AutoRun(udriver)
        print("--- 龙脉任务完成 ---")
        log_to_file("--- 龙脉任务完成 ---")
        time.sleep(2)

    except Exception as e:
        print(f"{e}")
        raise Exception("*** 龙脉任务错误 ***")

def PartSeven(udriver):
    try:
        print("--- 主线任务/支线任务10021、10022（23-26级） ---")
        log_to_file("--- 主线任务/支线任务10021、10022（23-26级） ---")
        time.sleep(1)
        pages.phase_CheckBag_test.AutoRun(udriver)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
        # print("主线-征战沙场")
        name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
        task_name = re.search(r'(?<=])(.*)(?=<)', name)
        print("主线-" + str(task_name.group(0)))
        log_to_file("主线-" + str(task_name.group(0)))
        time.sleep(3)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIBanner//imgBG//btnClose1"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIBanner//imgBG//btnClose1").tap()
            time.sleep(2)
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            else:
                break
        while True:
            time.sleep(5)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIBattleRank//imgBG//btnLeave"):
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIBattleRank//imgBG//btnLeave").tap()
                print("宋金战场完成，离开战场")
                break
        time.sleep(5)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIBattleRank//imgBG//btnLeave"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIBattleRank//imgBG//btnLeave").tap()
            print("宋金战场完成，离开战场")
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//AchievementDisplay//node//btnGain"):
            udriver.find_object(By.PATH, "//UIModule//Group1//AchievementDisplay//node//btnGain").tap()
            time.sleep(2)
        # 潜龙秘宝
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIItemTips//imgBG//btnGroup//btnCenter"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIItemTips//imgBG//btnGroup//btnCenter").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIItemBatchPanel//imgBG//btnClose").tap()
            time.sleep(2)
        phase_CheckBag_test.AutoRun(udriver)

        log_to_file("支线10021-披风升阶")
        if udriver.find_object_in_range_where_text_contains("txtTitle", "披风升阶", "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//panelOtherTask//Content"):
            name = udriver.find_object_in_range_where_text_contains("txtTitle", "披风升阶", "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//panelOtherTask//Content")
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//panelOtherTask//Content//" + name + "//btnTrack").tap()
            print("支线10021-披风升阶")
        else:
            log_to_file("支线10021-披风升阶未开启")
            raise Exception("支线10021-披风升阶未开启")
        time.sleep(3)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIMantleUpgrade//BtnUpgrade").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIMantleUpgrade//BtnClose").tap()
        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
            time.sleep(2)

        log_to_file("支线10022-装备镶嵌")
        if udriver.find_object_in_range_where_text_contains("txtTitle", "装备镶嵌", "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//panelOtherTask//Content"):
            name = udriver.find_object_in_range_where_text_contains("txtTitle", "装备镶嵌", "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//panelOtherTask//Content")
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//panelOtherTask//Content//" + name + "//btnTrack").tap()
            print("支线10022-装备镶嵌")
        else:
            log_to_file("支线10022-装备镶嵌未开启")
            raise Exception("支线10022-装备镶嵌未开启")
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIBanner//imgBG//btnClose1"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIBanner//imgBG//btnClose1").tap()
            time.sleep(2)
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn"):
                break
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        print("装备镶嵌指引")
        time.sleep(2)
        try:
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//btnBag").tap()
        except:
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnBag").tap()
        time.sleep(3)
        for i in udriver.find_child( "//UIModule//Group1//UIBag//imgBG//BagPanel//bagBackground//maskView//imgInventory"):
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIBag//imgBG//BagPanel//bagBackground//maskView//imgInventory//" + i + "//UIItemGrid//TagTip"):
                wq = udriver.find_object(By.PATH, "//UIModule//Group1//UIBag//imgBG//BagPanel//bagBackground//maskView//imgInventory//" + i + "//UIItemGrid//TagTip").get_text()
                if wq == "可装备":
                    udriver.find_object(By.PATH, "//UIModule//Group1//UIBag//imgBG//BagPanel//bagBackground//maskView//imgInventory//" + i + "//UIItemGrid//ItemLayer").tap()
                    break
        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIEquipTips//imgBG//btnGroup//btn1"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIEquipTips//imgBG//btnGroup//btn1").tap()
            time.sleep(3)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIBag//imgBG//BagPanel//UIEquipPanel//EquipPanel//PanelEquip//Helm//UIItemGrid//ItemLayer").tap()
        time.sleep(3)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIEquipTips//imgBG//btnGroup//btn3").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIEquipment//node//InsetPanel//EquipStonePanel//EquipStoneList//Viewport//Content//Element1//Empty").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIEquipment//node//InsetPanel//BagStonePanel//BagStoneList//Viewport//Content//Element1").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//AchievementDisplay//node//btnGain").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIEquipment//node//btnClose").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIBag//imgBG//btnClose").tap()
        time.sleep(3)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIItemTips//imgBG//btnGroup//btnCenter"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIItemTips//imgBG//btnGroup//btnCenter").tap()
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIShopBuy//imgBG//btnClose"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIShopBuy//imgBG//btnClose").tap()
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIShop//imgBG//btnClose"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIShop//imgBG//btnClose").tap()
            time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//ClickEmptyToClose"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//ClickEmptyToClose").tap()
            time.sleep(2)

    except Exception as e:
        print(f"{e}")
        log_to_file("*** 主线任务/支线任务10021、10022（23-26级）错误 ***")
        raise Exception("*** 主线任务/支线任务10021、10022（23-26级）错误 ***")

def PartSeven2(udriver):
    try:
        time.sleep(1)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
        # print("主线-易骨经")
        # log_to_file("主线-易骨经")
        name = udriver.find_object(By.PATH,  "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
        task_name = re.search(r'(?<=])(.*)(?=<)', name)
        print("主线-" + str(task_name.group(0)))
        log_to_file("主线-" + str(task_name.group(0)))
        while True:
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                break
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
            time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        print("组队指引")
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//ButtonGroup//ToggleTeam").tap()
        time.sleep(2)
        if udriver.object_exist(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//ButtonGroup//ToggleTeam"):
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//ButtonGroup//ToggleTeam").tap()
            time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIGuide//imgBG//DefaultBtn").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UITeam//imgBG//btnClose").tap()
        time.sleep(2)
        udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//ButtonGroup//ToggleTask").tap()
        time.sleep(1)
        level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
        Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
        print("当前等级" + " " + str(level) + "," + str(Exp))
        log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
        print("--- 主线任务/支线任务10021、10022（23-26级）完成 ---")
        log_to_file("--- 主线任务/支线任务10021、10022（23-26级）完成 ---")
        time.sleep(2)

    except Exception as e:
        print(f"{e}")
        log_to_file("*** 主线任务/支线任务10021、10022（23-26级）错误 ***")
        raise Exception("*** 主线任务/支线任务10021、10022（23-26级）错误 ***")

def PartEight(udriver):
    try:
        # 野外修炼
        print("--- 支线10009（27级） ---")
        log_to_file("--- 支线任务10009（27级） ---")
        phase_field_test.AutoRun(udriver)
        print("--- 支线10009（27级）完成 ---")
        log_to_file("--- 支线10009（27级）完成 ---")
        time.sleep(2)

    except Exception as e:
        print(f"{e}")
        log_to_file("*** 支线任务10009（27级）错误 ***")
        raise Exception("*** 支线任务10009（27级）错误 ***")

def PartNine(udriver):
    try:
        print("--- 支线10004、10005、10018、10019（25级） ---")
        log_to_file("--- 支线10004、10005、10018、10019（25级） ---")

        # 宋金战场
        print("支线10004-宋金战场")
        phase_battlefield_test.AutoRun(udriver) # 检查装备是否换上、装备是否强化、加技能点、加潜能

        # 时间挑战
        time.sleep(2)
        pages.phase_CheckBag_test.AutoRun(udriver) # 检查装备是否换上、装备是否强化、加技能点、加潜能
        print("支线10005-时间挑战")
        phase_time_test.AutoRun(udriver)

        # 千里追凶（杀手任务）
        time.sleep(2)
        pages.phase_CheckBag_test.AutoRun(udriver) # 检查装备是否换上、装备是否强化、加技能点、加潜能
        print("支线10018-千里追凶")
        phase_killer_test.AutoRun(udriver)

        # 五行奇阵
        time.sleep(2)
        pages.phase_CheckBag_test.AutoRun(udriver) # 检查装备是否换上、装备是否强化、加技能点、加潜能
        print("支线10019-五行奇阵")
        phase_five_elements_test.AutoRun(udriver)

        print("--- 支线10004、10005、10018、10019（25级）完成 ---")
        log_to_file("--- 支线10004、10005、10018、10019（25级）完成 ---")
        time.sleep(2)

    except Exception as e:
        print(f"{e}")
        log_to_file("*** 支线10004、10005、10018、10019（25级）错误 ***")
        raise Exception("*** 支线10004、10005、10018、10019（25级）错误 ***")

def PartTen(udriver):
    try:
        print("--- 支线10002、10003 ---")
        log_to_file("--- 支线10002、10003 ---")

        # 加入帮会
        time.sleep(3)
        print("支线10002-加入帮会")
        phase_secret_test.AutoRun(udriver)

        # 帮会烤火
        time.sleep(3)
        print("支线10003-帮会烤火")
        phase_secret_fire_test.AutoRun(udriver)

        print("--- 支线10002、10003完成 ---")
        log_to_file("--- 支线10002、10003完成 ---")

    except Exception as e:
        print(f"{e}")
        log_to_file("*** 支线10002、10003错误 ***")
        raise Exception("*** 支线10002、10003错误 ***")

def PartEleven(udriver,run = True):
    if run == True:
        try:
            print("--- 30级之后主线任务/支线任务 ---")
            log_to_file("--- 30级之后主线任务/支线任务 ---")
            time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            else:
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//btnSwitch").tap()
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//btnGM").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//MainCmd//CmdList//CmdList//Element1").tap()
            time.sleep(1)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").set_text("31")
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtDesc//btnExecute").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//btnClose").tap()
            time.sleep(1)
            print("GM升至31级")
            log_to_file("GM升至31级")

            time.sleep(1)
            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-弟子争雄")
            # log_to_file("主线-弟子争雄")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                # task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                else:
                    task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                    if "金国" in task:
                        break
            while True:
                time.sleep(2)
                task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                if "金国" not in task:
                    time.sleep(2)
                    if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                        udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                    break
            time.sleep(1)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver,False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-罗汉阵")33级
            # log_to_file("主线-罗汉阵")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                # task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                else:
                    task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                    if "击败" in task:
                        break
            time.sleep(1)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver,False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-莫愁的试探 一")36级
            # log_to_file("莫愁的试探 一")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver,False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-莫愁的试探 二")39级
            # log_to_file("莫愁的试探 二")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                # task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                else:
                    task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                    if "交谈" in task:
                        break
            while True:
                time.sleep(1)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
                    break
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose") or udriver.object_exist(By.PATH, "//UIModule//Group1//UIMessageBox//imgBG//CheckTips//ToggleCheck"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIMessageBox//imgBG//CheckTips//ToggleCheck"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIMessageBox//imgBG//CheckTips//ToggleCheck").tap()
                time.sleep(1)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UIMessageBox//imgBG//btnCancel"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UIMessageBox//imgBG//btnCancel").tap()
                    time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver,False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-公子不笑 一")43级
            # log_to_file("主线-公子不笑 一")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIMessageBox//imgBG//CheckTips//ToggleCheck"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIMessageBox//imgBG//CheckTips//ToggleCheck").tap()
                time.sleep(1)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UIMessageBox//imgBG//btnCancel"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UIMessageBox//imgBG//btnCancel").tap()
                    time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver, False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-公子不笑 二")45级
            # log_to_file("主线-公子不笑 二")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                # task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                else:
                    task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                    if "交给" in task:
                       break
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                else:
                    break
            while True:
                time.sleep(1)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
                    break
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver,False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-九现疑云 一")46级
            # log_to_file("主线-九现疑云 一")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver,False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-九现疑云 二")48级
            # log_to_file("主线-九现疑云 二")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                # task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                else:
                    task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                    if "交给" in task:
                        break
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                else:
                    break
            while True:
                time.sleep(1)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
                    break
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver,False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-莫愁失踪 一")49级
            # log_to_file("莫愁失踪 一")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver,False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-莫愁失踪 二")51级
            # log_to_file("莫愁失踪 二")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                # task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                else:
                    task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                    if "交谈" in task:
                       break
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                else:
                    break
            while True:
                time.sleep(1)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask"):
                    udriver.find_object(By.PATH,  "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
                    break
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver,False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-真相大白 一")53级
            # log_to_file("真相大白 一")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                # task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                else:
                    task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                    if "交谈" in task:
                       break
            time.sleep(2)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver,False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-真相大白 二")
            # log_to_file("真相大白 二")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            else:
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//btnSwitch").tap()
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//btnGM").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//MainCmd//CmdList//CmdList//Element1").tap()
            time.sleep(1)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").set_text("60")
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtDesc//btnExecute").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//btnClose").tap()
            time.sleep(1)
            print("GM升至60级")
            log_to_file("GM升至60级")
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver, False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-宝刀蒙尘")
            # log_to_file("宝刀蒙尘")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            else:
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//btnSwitch").tap()
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//btnGM").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//MainCmd//CmdList//CmdList//Element1").tap()
            time.sleep(1)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").set_text("70")
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtDesc//btnExecute").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//btnClose").tap()
            time.sleep(1)
            print("GM升至70级")
            log_to_file("GM升至70级")
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver, False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-锦帕抒情")
            # log_to_file("锦帕抒情")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH,  "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            else:
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//btnSwitch").tap()
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//btnGM").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//MainCmd//CmdList//CmdList//Element1").tap()
            time.sleep(1)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").set_text("80")
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtDesc//btnExecute").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//btnClose").tap()
            time.sleep(1)
            print("GM升至80级")
            log_to_file("GM升至80级")
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver, False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-苏忠报国")
            # log_to_file("苏忠报国")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH,  "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            else:
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//btnSwitch").tap()
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//btnGM").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//MainCmd//CmdList//CmdList//Element1").tap()
            time.sleep(1)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").set_text("90")
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtDesc//btnExecute").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//btnClose").tap()
            time.sleep(1)
            print("GM升至90级")
            log_to_file("GM升至90级")
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver, False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-千里传书")
            # log_to_file("千里传书")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            else:
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//btnSwitch").tap()
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//btnGM").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//MainCmd//CmdList//CmdList//Element1").tap()
            time.sleep(1)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").set_text("100")
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtDesc//btnExecute").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//btnClose").tap()
            time.sleep(1)
            print("GM升至100级")
            log_to_file("GM升至100级")
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver, False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-递扇传情")
            # log_to_file("递扇传情")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element3"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element2").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            else:
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//btnSwitch").tap()
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//btnGM").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//MainCmd//CmdList//CmdList//Element1").tap()
            time.sleep(1)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").set_text("110")
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtDesc//btnExecute").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//btnClose").tap()
            time.sleep(1)
            print("GM升至110级")
            log_to_file("GM升至110级")
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver, False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-阳春白雪")
            # log_to_file("阳春白雪")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                # task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                else:
                    task = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTarget").get_text()
                    if "交给" in task:
                        break
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element3"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element2").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            else:
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//btnSwitch").tap()
                time.sleep(2)
                udriver.find_object(By.PATH, "//UIModule//Group1//UIHudRightBottom//imgBG//rightBottomSystem//btnSetting").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UISetting//imgBG//btnGM").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//MainCmd//CmdList//CmdList//Element1").tap()
            time.sleep(1)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtParamTip1//inputParam1").set_text("120")
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//GmCmdPanel//CmdList//CmdList//Element2//txtDesc//btnExecute").tap()
            time.sleep(2)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIGM//imgBG//btnClose").tap()
            time.sleep(1)
            print("GM升至120级")
            log_to_file("GM升至120级")
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            level = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtLevel").get_text()
            Exp = udriver.find_object(By.PATH, "//UIModule//Group1//UIHud//top//Frame//TextGroup//txtExp").get_text()
            print("当前等级" + " " + str(level) + "," + str(Exp))
            log_to_file("当前等级" + " " + str(level) + "," + str(Exp))
            time.sleep(1)
            phase_CheckBag_test.AutoRun(udriver, False)
            udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//btnTrack").tap()
            # print("主线-武林向背")
            # log_to_file("武林向背")
            name = udriver.find_object(By.PATH, "//UIModule//Group1//UIHudLeftFrameExt//imgBG//Root//Dynamic//PanelGroup//UIHudLeftPanelTask//panelAllTask//itemMainTask//txtTitle").get_text()
            task_name = re.search(r'(?<=])(.*)(?=<)', name)
            print("主线-" + str(task_name.group(0)))
            log_to_file("主线-" + str(task_name.group(0)))
            while True:
                time.sleep(2)
                if udriver.object_exist(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1"):
                    udriver.find_object(By.PATH, "//UIModule//Group1//UINpcDialog//Panel//imgBG//bottom//options//options//Element1").tap()
                elif udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                    break
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIGetAwardShow//ClickEmptyToClose").tap()
                time.sleep(1)
            if udriver.object_exist(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse"):
                udriver.find_object(By.PATH, "//UIModule//Group1//UIQuickUseEquip//imgBG//btnUse").tap()
                time.sleep(1)

            print("--- 30级之后主线任务完成 ---")
            log_to_file("--- 30级之后主线任务完成 ---")

        except Exception as e:
            print(f"{e}")
            log_to_file("*** 30级之后主线任务错误 ***")
            raise Exception("*** 30级之后主线任务错误 ***")
    else:
        pass

def AutoRun(udriver):
    try:
        start = datetime.datetime.now()
        print('----------------开始任务（少林）案例--------------')
        with open("TestCastLog.txt", "w", encoding="utf-8") as f:
            f.write("----------------开始任务（少林）案例--------------" + "\n")
        PartLogin(udriver)
        PartOne(udriver)
        PartTwo(udriver)
        PartThree(udriver)
        PartFour(udriver)
        PartFive(udriver)
        PartSix(udriver)
        PartSeven(udriver)
        PartSeven2(udriver)
        PartEight(udriver)
        PartNine(udriver)
        PartTen(udriver)
        PartEleven(udriver)
        print("----------------任务案例（少林）完成--------------")
        log_to_file("----------------任务案例（少林）完成--------------")
        end = datetime.datetime.now()
        pages.mem_unity(udriver,"少林任务流程",start,end)

    except Exception as e:
        print(f"{e}")
        log_to_file("----------------任务案例（少林）错误--------------")
        raise Exception("----------------任务案例（少林）错误--------------")