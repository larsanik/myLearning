text = """
//#####################################################################################################################
//-----------------------------------------	 Аварийные сообщения	-------------------------------------------------
//#####################################################################################################################
LG.AOb:= LG.AOb AND NOT unlock;
LG.AOs:= LG.AOs AND NOT unlock;
LG.NOb:= LG.NOb AND NOT unlock;
LG.NOs:= LG.NOs AND NOT unlock;
IF unlock THEN Str_PLC.first_NOs :=''; Str_PLC.first_NOb :=''; Str_PLC.first_AOs :='';Str_PLC.first_AOb :=''; END_IF;
//------------------------------DGI---------------------------------------
//AOs: Уровень в аккумуляторе масла уплотнения аварийно-низкий
AS.Hmu_An := Q_ON.dPmg AND (ANB.Lma_Av OR DGI.Hmu_An) OR AS.Hmu_An AND  NOT unlock ;
IF AS.Hmu_An AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Уровень в аккумуляторе масла уплотнения аварийно-низкий'; END_IF;
LG.AOs := LG.AOs OR AS.Hmu_An;
AS_INDX[0] := AS.Hmu_An;
//AOs: Загазованность в укрытии ГПА 20%
//AS.Gas_20 := DGI.Gas_20 AND DGI.KCD_Gas_20 OR AS.Gas_20 AND  NOT unlock ;
IF AS.Gas_20 AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Загазованность в укрытии ГПА 20%'; END_IF;
LG.AOs := LG.AOs OR AS.Gas_20;
AS_INDX[1] := AS.Gas_20;

//AOs: Пожар в укрытии ГПА
//AS.Fire_GPA := DGI.Fire_GPA AND DGI.KCD_Fire_GPA OR AS.Fire_GPA AND  NOT unlock ;
IF AS.Fire_GPA AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Пожар в укрытии ГПА'; END_IF;
LG.AOs := LG.AOs OR AS.Fire_GPA;
AS_INDX[4] := AS.Fire_GPA;
//AOs: Кнопка АО в БУ нажата
//AS.Btn_AO_BU := DGI.Btn_AO_BU OR AS.Btn_AO_BU AND  NOT unlock ;
IF AS.Btn_AO_BU AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Кнопка АО в БУ нажата'; END_IF;
LG.AOs := LG.AOs OR AS.Btn_AO_BU;
AS_INDX[5] := AS.Btn_AO_BU;
//NOs: Кнопка НО в БУ нажата
//AS.Btn_NO_BU := DGI.Btn_NO_BU OR AS.Btn_NO_BU AND  NOT unlock ;
IF AS.Btn_NO_BU AND Str_PLC.first_NOs = ''  THEN  Str_PLC.first_NOs:= 'Кнопка НО в БУ нажата'; END_IF;
LG.NOs := LG.NOs OR AS.Btn_NO_BU;
AS_INDX[6] := AS.Btn_NO_BU;
//AOs: АО из РК БУ
//AS.AO_RK_BU := DGI.AO_RK_BU AND DGI.KCD_AO_RK_BU OR AS.AO_RK_BU AND  NOT unlock ;
IF AS.AO_RK_BU AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'АО из РК БУ'; END_IF;
LG.AOs := LG.AOs OR AS.AO_RK_BU;
AS_INDX[7] := AS.AO_RK_BU;
//AOs: БЭАО сработал
//AS.BEO_work := DGI.BEO_work OR AS.BEO_work AND  NOT unlock ;
IF AS.BEO_work AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'БЭАО сработал'; END_IF;
LG.AOs := LG.AOs OR AS.BEO_work;
AS_INDX[8] := AS.BEO_work;
//AOs: БЗРТ сработал
(*AS.BZRT_ON := DGI.BZRT_ON OR AS.BZRT_ON AND  NOT unlock ;
IF AS.BZRT_ON AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'БЗРТ сработал'; END_IF;
LG.AOs := LG.AOs OR AS.BZRT_ON;
AS_INDX[9] := AS.BZRT_ON;*)
//AOs: ПРУ: Кнопка ЭАО нажата
AS.Btn_EAO_ON := DGI.Btn_EAO_ON  OR AS.Btn_EAO_ON AND  NOT unlock ;
IF AS.Btn_EAO_ON AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'ПРУ: Кнопка ЭАО нажата'; END_IF;
LG.AOs := LG.AOs OR AS.Btn_EAO_ON;
AS_INDX[10] := AS.Btn_EAO_ON;
//AOs: ПРУ: Кнопка АО нажата
AS.Btn_AO := DGI.Btn_AO OR AS.Btn_AO AND  NOT unlock ;
IF AS.Btn_AO AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'ПРУ: Кнопка АО нажата'; END_IF;
LG.AOs := LG.AOs OR AS.Btn_AO;
AS_INDX[11] := AS.Btn_AO;
//NOs: ПРУ: Кнопка НО нажата
//AS.Btn_NO := DGI.Btn_NO OR AS.Btn_NO AND  NOT unlock ;
IF AS.Btn_NO AND Str_PLC.first_NOs = ''  THEN  Str_PLC.first_NOs:= 'ПРУ: Кнопка НО нажата'; END_IF;
LG.NOs := LG.NOs OR AS.Btn_NO;
AS_INDX[12] := AS.Btn_NO;
//AOs: Аварийный останов от САУ КЦ
AS.AO_SauKC := DGI.AO_SauKC OR AS.AO_SauKC AND  NOT unlock ;
IF AS.AO_SauKC AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Аварийный останов от САУ КЦ'; END_IF;
LG.AOs := LG.AOs OR AS.AO_SauKC;
AS_INDX[13] := AS.AO_SauKC;
//-------------------------------LG--------------------------------------
//AOs: Аварийная остановка с дисплея оператора (АОсс)
AS.ARM_AOss := LG.ARM_AOss OR AS.ARM_AOss AND NOT unlock ;
IF AS.ARM_AOss AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Аварийная остановка с дисплея оператора (АОсс)'; END_IF;
LG.AOs := LG.AOs OR AS.ARM_AOss;
AS_INDX[14] := AS.ARM_AOss;
//AOb: Аварийная остановка с дисплея оператора (АОбс)
AS.ARM_AObs := LG.ARM_AObs OR AS.ARM_AObs AND NOT unlock ;
IF AS.ARM_AObs AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Аварийная остановка с дисплея оператора (АОбс)'; END_IF;
LG.AOb := LG.AOb OR AS.ARM_AObs;
AS_INDX[15] := AS.ARM_AObs;
//NOs: Нормальная остановка с дисплея оператора (НОсс)
AS.ARM_NOss := LG.ARM_NOss OR AS.ARM_NOss AND NOT unlock ;
IF AS.ARM_NOss AND Str_PLC.first_NOs = ''  THEN  Str_PLC.first_NOs:= 'Нормальная остановка с дисплея оператора (НОсс)'; END_IF;
LG.NOs := LG.NOs OR AS.ARM_NOss;
AS_INDX[16] := AS.ARM_NOss;
//NOb: Нормальная остановка с дисплея оператора (НОбс)
AS.ARM_NObs := LG.ARM_NObs OR AS.ARM_NObs AND NOT unlock ;
IF AS.ARM_NObs AND Str_PLC.first_NOb = ''  THEN  Str_PLC.first_NOb:= 'Нормальная остановка с дисплея оператора (НОбс)'; END_IF;
LG.NOb := LG.NOb OR AS.ARM_NObs;
AS_INDX[17] := AS.ARM_NObs;
//AOs: Помпаж нагнетателя
AS.SurgeN := flag_from_SR.SurgeN OR AS.SurgeN AND NOT unlock ;
IF AS.SurgeN AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Помпаж нагнетателя'; END_IF;
LG.AOs := LG.AOs OR AS.SurgeN;
AS_INDX[18] := AS.SurgeN;
//AOb: Погасание факела
IF Q_ON.Flame AND LG.Flame_failur THEN IF delay[0]  <= 3.0 THEN delay[0] := delay[0] + cycle; END_IF; ELSE delay[0]  := 0.0; END_IF;
AS.Flame_failur := delay[0] > 3.0 OR AS.Flame_failur  AND NOT unlock ;
IF AS.Flame_failur AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Погасание факела '; END_IF;
LG.AOb := LG.AOb OR AS.Flame_failur;
AS_INDX[19] := AS.Flame_failur;
//AOs: Самопроизвольная перестановка крана 1
AS.Kr1_ON_OF := LG.Kr1_ON_OF OR AS.Kr1_ON_OF AND NOT unlock ;
IF AS.Kr1_ON_OF AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Самопроизвольная перестановка крана 1'; END_IF;
LG.AOs := LG.AOs OR AS.Kr1_ON_OF;
AS_INDX[20] := AS.Kr1_ON_OF;
//AOs: Самопроизвольная перестановка крана 2
AS.Kr2_ON_OF := LG.Kr2_ON_OF OR AS.Kr2_ON_OF AND NOT unlock ;
IF AS.Kr2_ON_OF AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Самопроизвольная перестановка крана 2'; END_IF;
LG.AOs := LG.AOs OR AS.Kr2_ON_OF;
AS_INDX[21] := AS.Kr2_ON_OF;
//AOs: Неисправность регулятора
AS.REG := LG.REG OR AS.REG AND NOT unlock ;
IF AS.REG AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Неисправность регулятора'; END_IF;
LG.AOs := LG.AOs OR AS.REG;
AS_INDX[23] := AS.REG;
//AOb: Провал оборотов
AS.L70NHL := Q_ON.Flame AND LG.L70NHL OR AS.L70NHL AND NOT unlock ;
IF AS.L70NHL AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Провал оборотов'; END_IF;
LG.AOb := LG.AOb OR AS.L70NHL;
AS_INDX[24] := AS.L70NHL;
//AOb: ТР: Отказ оборотов ТВД
AS.N_VD_fault := LG.N_VD_fault OR AS.N_VD_fault AND NOT unlock ;
IF AS.N_VD_fault AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'ТР: Отказ оборотов ТВД'; END_IF;
LG.AOb := LG.AOb OR AS.N_VD_fault;
AS_INDX[25] := AS.N_VD_fault;
//AOb: ТР: Отказ оборотов ТНД
AS.N_ND_fault := LG.N_ND_fault OR AS.N_ND_fault AND NOT unlock ;
IF AS.N_ND_fault AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'ТР: Отказ оборотов ТНД'; END_IF;
LG.AOb := LG.AOb OR AS.N_ND_fault;
AS_INDX[26] := AS.N_ND_fault;
//AOb: ТР: Отказ РК
IF LG.FR_fault THEN IF delay[2]  <= 0.5 THEN delay[2] := delay[2] + cycle; END_IF; ELSE delay[2]  := 0.0; END_IF;
AS.FR_fault := delay[2] > 0.5 OR AS.FR_fault  AND NOT unlock ;
IF AS.FR_fault AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'ТР: Отказ РК'; END_IF;
LG.AOb := LG.AOb OR AS.FR_fault;
AS_INDX[27] := AS.FR_fault;
//AOb: ТР: Отказ ПНА
IF LG.PNA_fault THEN IF delay[3]  <= 0.5 THEN delay[3] := delay[3] + cycle; END_IF; ELSE delay[3]  := 0.0; END_IF;
AS.PNA_fault := delay[3] > 0.5 OR AS.PNA_fault  AND NOT unlock ;
IF AS.PNA_fault AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'ТР: Отказ ПНА'; END_IF;
LG.AOb := LG.AOb OR AS.PNA_fault;
AS_INDX[28] := AS.PNA_fault;
//AOb: ТР:Чрезмерное открытие ТРК на поджиге
//#IF LG.RK_maxopen THEN IF delay[4]  <= 3.0 THEN delay[4] := delay[4] + cycle; END_IF; ELSE delay[4]  := 0.0; END_IF;
AS.SK_maxopen := delay[4] > 0.5 OR AS.SK_maxopen  AND NOT unlock ;
IF AS.SK_maxopen AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'ТР:Чрезмерное открытие ТРК на поджиге'; END_IF;
LG.AOb := LG.AOb OR AS.SK_maxopen;
AS_INDX[29] := AS.SK_maxopen;
//-------------------------------FR--------------------------------------
//------------------------------------SR---------------------------------
//------------------------------AI---------------------------------------
//AOs: Давление газа на выходе нагнетателя аварийно высокое
IF ANB.Pg_out_N_Av THEN IF delay[5]  <= 1.0 THEN delay[5] := delay[5] + cycle; END_IF; ELSE delay[5]  := 0.0; END_IF;
AS.Pg_out_N_Av := delay[5] > 1.0 OR AS.Pg_out_N_Av AND NOT unlock ;
IF AS.Pg_out_N_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Давление газа на выходе нагнетателя аварийно высокое'; END_IF;
LG.AOs := LG.AOs OR AS.Pg_out_N_Av;
AS_INDX[30] := AS.Pg_out_N_Av;
//AOs: Перепад масло-газ аварийно низкий # в проекте GE авария отклбчена
//IF Q_ON.dPmg AND ANB.dP_mg_An THEN IF delay[6]  <= 180.0 THEN delay[6] := delay[6] + cycle; END_IF; ELSE delay[6]  := 0.0; END_IF;
//AS.dP_mg_An := delay[6] > 180.0 OR AS.dP_mg_An AND NOT unlock ;
//IF AS.dP_mg_An AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Перепад масло-газ аварийно низкий '; END_IF;
//LG.AOs := LG.AOs OR AS.dP_mg_An;
//AS_INDX[31] := AS.dP_mg_An;
//AOs: Давление масла в коллекторе смазки нагнетателя аварийно-низкое
IF Q_ON.MS AND ANB.Pmsm_N_An THEN IF delay[8]  <= 5.0 THEN delay[8] := delay[8] + cycle; END_IF; ELSE delay[8]  := 0.0; END_IF;
AS.Pmsm_N_An := delay[8] > 5.0 OR AS.Pmsm_N_An AND NOT unlock ;
IF AS.Pmsm_N_An AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Давление масла в коллекторе смазки нагнетателя аварийно-низкое'; END_IF;
LG.AOs := LG.AOs OR AS.Pmsm_N_An;
AS_INDX[33] := AS.Pmsm_N_An;
//AOs: Давление масла смазки в коллекторе насосов аварийно-низкое # нет такой аварии в GE
//IF Q_ON.MS AND ANB.Pmn_An THEN IF delay[9]  <= 5.0 THEN delay[9] := delay[9] + cycle; END_IF; ELSE delay[9]  := 0.0; END_IF;
//AS.Pmn_An := delay[9] > 5.0 OR AS.Pmn_An AND NOT unlock ;
//IF AS.Pmn_An AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Давление масла смазки в коллекторе насосов аварийно-низкое'; END_IF;
//LG.AOs := LG.AOs OR AS.Pmn_An;
//AS_INDX[34] := AS.Pmn_An;

//AOs: Давление масла гидравлики аварийно-низкое
IF Q_ON.MG AND ANB.Pmg_An THEN IF delay[12]  <= 5.0 THEN delay[12] := delay[12] + cycle; END_IF; ELSE delay[12]  := 0.0; END_IF;
AS.Pmg_An := delay[12] > 5.0 OR AS.Pmg_An AND NOT unlock ;
IF AS.Pmg_An AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Давление масла гидравлики аварийно-низкое'; END_IF;
LG.AOs := LG.AOs OR AS.Pmg_An;
AS_INDX[37] := AS.Pmg_An;
//AOs: Давление масла предельной защиты аварийно-низкое
IF Q_ON.MZ AND ANB.Pmz_An THEN IF delay[13]  <= 3.0 THEN delay[13] := delay[13] + cycle; END_IF; ELSE delay[13]  := 0.0; END_IF;
AS.Pmz_An := delay[13] > 3.0 OR AS.Pmz_An AND NOT unlock ;
IF AS.Pmz_An AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Давление масла предельной защиты аварийно-низкое'; END_IF;
LG.AOs := LG.AOs OR AS.Pmz_An;
AS_INDX[38] := AS.Pmz_An;
//AOs: Вибрация подшипника нагнетателя горизонтальная со стороны привода аварийно-высокая
LG.Vg_N_stP := ANB.Vg_N_stP_Av (*AND (ANB.Vv_N_stP_Pv OR ANB.Vg_N_stK_Pv OR ANB.Vv_N_stK_Pv)*);
IF LG.Vg_N_stP THEN IF delay[32]  <= 10.0 THEN delay[32] := delay[32] + cycle; END_IF; ELSE delay[32]  := 0.0; END_IF;
AS.Vg_N_stP_Av := delay[32] > 10.0 OR AS.Vg_N_stP_Av AND NOT unlock ;
IF AS.Vg_N_stP_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Вибрация подшипника Н горизонтальная со стороны привода аварийно-высокая'; END_IF;
LG.AOs := LG.AOs OR AS.Vg_N_stP_Av;
AS_INDX[40] := AS.Vg_N_stP_Av;
//AOs: Вертикальная вибрация подшипника нагнетателя со стороны привода аварийно-высокая
LG.Vv_N_stP := ANB.Vv_N_stP_Av (*AND (ANB.Vg_N_stP_Pv OR ANB.Vg_N_stK_Pv OR ANB.Vv_N_stK_Pv)*);
IF LG.Vv_N_stP THEN IF delay[33]  <= 10.0 THEN delay[33] := delay[33] + cycle; END_IF; ELSE delay[33]  := 0.0; END_IF;
AS.Vv_N_stP_Av := delay[33] > 10.0 OR AS.Vv_N_stP_Av AND NOT unlock ;
IF AS.Vv_N_stP_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Вертикальная вибрация подшипника Н со стороны привода аварийно-высокая'; END_IF;
LG.AOs := LG.AOs OR AS.Vv_N_stP_Av;
AS_INDX[41] := AS.Vv_N_stP_Av;
//AOs: Вибрация подшипника нагнетателя горизонтальная со стороны крышки  аварийно-высокая
LG.Vg_N_stK := ANB.Vg_N_stK_Av (*AND (ANB.Vg_N_stP_Pv OR ANB.Vv_N_stP_Pv OR ANB.Vv_N_stK_Pv)*);
IF LG.Vg_N_stK THEN IF delay[34]  <= 10.0 THEN delay[34] := delay[34] + cycle; END_IF; ELSE delay[34]  := 0.0; END_IF;
AS.Vg_N_stK_Av := delay[34] > 10.0 OR AS.Vg_N_stK_Av AND NOT unlock ;
IF AS.Vg_N_stK_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Вибрация подшипника Н горизонтальная со стороны крышки  аварийно-высокая'; END_IF;
LG.AOs := LG.AOs OR AS.Vg_N_stK_Av;
AS_INDX[42] := AS.Vg_N_stK_Av;
//AOs: Вибрация подшипника нагнетателя вертикальная со стороны крышки аварийно-высокая
LG.Vv_N_stK := ANB.Vv_N_stK_Av (*AND (ANB.Vg_N_stP_Pv OR ANB.Vv_N_stP_Pv OR ANB.Vg_N_stK_Pv)*);
IF LG.Vv_N_stK THEN IF delay[35]  <= 10.0 THEN delay[35] := delay[35] + cycle; END_IF; ELSE delay[35]  := 0.0; END_IF;
AS.Vv_N_stK_Av := delay[35] > 10.0 OR AS.Vv_N_stK_Av AND NOT unlock ;
IF AS.Vv_N_stK_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Вибрация подшипника нагнетателя вертикальная со стороны крышки аварийно-высокая'; END_IF;
LG.AOs := LG.AOs OR AS.Vv_N_stK_Av;
AS_INDX[43] := AS.Vv_N_stK_Av;
//AOs: Осевой сдвиг ротора нагнетателя аварийно высокий (вперёд)
AS.OS_N_Av := ANB.OS_N_Av OR AS.OS_N_Av AND NOT unlock ;
IF AS.OS_N_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Осевой сдвиг ротора нагнетателя аварийно высокий (вперёд)'; END_IF;
LG.AOs := LG.AOs OR AS.OS_N_Av;
AS_INDX[44] := AS.OS_N_Av;
//AOs: Осевой сдвиг ротора нагнетателя аварийно высокий (назад)
AS.OS_N_An := ANB.OS_N_An OR AS.OS_N_An AND NOT unlock ;
IF AS.OS_N_An AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Осевой сдвиг ротора нагнетателя аварийно высокий (назад)'; END_IF;
LG.AOs := LG.AOs OR AS.OS_N_An;
AS_INDX[45] := AS.OS_N_An;
//AOs: Вибрация подшипника ТВД аварийно-высокая
IF Calc_AI.VD_pr.PV >= 80.0 AND Calc_AI.VD_pr.PV <= 95.0 THEN
	time_delay := 15.0;
ELSE
	time_delay := 1.0;
END_IF;
IF ANB.V_1p_TVD_Av OR ANB.V_1p_TVD_vert_Av THEN IF delay[14]  <= time_delay THEN delay[14] := delay[14] + cycle; END_IF; ELSE delay[14]  := 0.0; END_IF;
AS.V_1p_TVD_Av := delay[14] > time_delay  OR AS.V_1p_TVD_Av AND NOT unlock ;
IF AS.V_1p_TVD_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Вибрация подшипника ТВД аварийно-высокая'; END_IF;
LG.AOs := LG.AOs OR AS.V_1p_TVD_Av;
AS_INDX[46] := AS.V_1p_TVD_Av;
//AOs: Вибрация подшипника ТНД аварийно-высокая
IF ANB.V_4p_TND_Av THEN IF delay[31]  <= time_delay THEN delay[31] := delay[31] + cycle; END_IF; ELSE delay[31]  := 0.0; END_IF;
AS.V_4p_TND_Av := delay[31] > time_delay  OR AS.V_4p_TND_Av AND NOT unlock ;
IF AS.V_4p_TND_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Вибрация подшипника нагнетателя вертикальная со стороны привода аварийно-высокая'; END_IF;
LG.AOs := LG.AOs OR AS.V_4p_TND_Av;
AS_INDX[47] := AS.V_4p_TND_Av;
//AOb: Температура масла на выходе из упорного подшипника № 1 ТВД аварийно-высокая
IF ANB.Tm_sl_up1_TVD_Av THEN IF delay[15]  <= 5.0 THEN delay[15] := delay[15] + cycle; END_IF; ELSE delay[15]  := 0.0; END_IF;
AS.Tm_sl_up1_TVD_Av := delay[15] > 5.0 OR AS.Tm_sl_up1_TVD_Av AND NOT unlock ;
IF AS.Tm_sl_up1_TVD_Av AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Температура масла на выходе из упорного подшипника № 1 ТВД аварийно-высокая'; END_IF;
LG.AOb := LG.AOb OR AS.Tm_sl_up1_TVD_Av;
AS_INDX[48] := AS.Tm_sl_up1_TVD_Av;
//AOb: Температура масла на сливе из опорного подшипника № 2 ТВД аварийно-высокая
IF ANB.Tm_sl_p2_TVD_Av THEN IF delay[16]  <= 5.0 THEN delay[16] := delay[16] + cycle; END_IF; ELSE delay[16]  := 0.0; END_IF;
AS.Tm_sl_p2_TVD_Av := delay[16] > 5.0 OR AS.Tm_sl_p2_TVD_Av AND NOT unlock ;
IF AS.Tm_sl_p2_TVD_Av AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Температура масла на сливе из опорного подшипника № 2 ТВД аварийно-высокая'; END_IF;
LG.AOb := LG.AOb OR AS.Tm_sl_p2_TVD_Av;
AS_INDX[49] := AS.Tm_sl_p2_TVD_Av;
//AOb: Температура масла смазки в коллекторе аварийно-высокая
IF ANB.Tmsm_D_Av THEN IF delay[17]  <= 5.0 THEN delay[17] := delay[17] + cycle; END_IF; ELSE delay[17]  := 0.0; END_IF;
AS.Tmsm_D_Av := delay[17] > 5.0 OR AS.Tmsm_D_Av AND NOT unlock ;
IF AS.Tmsm_D_Av AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Температура масла смазки в коллекторе аварийно-высокая '; END_IF;
LG.AOb := LG.AOb OR AS.Tmsm_D_Av;
AS_INDX[50] := AS.Tmsm_D_Av;
//AOb: Температура масла на сливе из опорного подшипника № 1 ТВД аварийно-высокая
IF ANB.Tm_sl_p1_TVD_Av THEN IF delay[18]  <= 5.0 THEN delay[18] := delay[18] + cycle; END_IF; ELSE delay[18]  := 0.0; END_IF;
AS.Tm_sl_p1_TVD_Av := delay[18] > 5.0 OR AS.Tm_sl_p1_TVD_Av AND NOT unlock ;
IF AS.Tm_sl_p1_TVD_Av AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Температура масла на сливе из опорного подшипника № 1 ТВД аварийно-высокая'; END_IF;
LG.AOb := LG.AOb OR AS.Tm_sl_p1_TVD_Av;
AS_INDX[51] := AS.Tm_sl_p1_TVD_Av;
//AOb: Температура масла на сливе из опорного подшипника № 3 ТНД аварийно-высокая
IF ANB.Tm_sl_p3_TND_Av THEN IF delay[19]  <= 5.0 THEN delay[19] := delay[19] + cycle; END_IF; ELSE delay[19]  := 0.0; END_IF;
AS.Tm_sl_p3_TND_Av := delay[19] > 5.0 OR AS.Tm_sl_p3_TND_Av AND NOT unlock ;
IF AS.Tm_sl_p3_TND_Av AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Температура масла на сливе из опорного подшипника № 3 ТНД аварийно-высокая'; END_IF;
LG.AOb := LG.AOb OR AS.Tm_sl_p3_TND_Av;
AS_INDX[52] := AS.Tm_sl_p3_TND_Av;
//AOb: Температура масла на сливе из опорного подшипника № 4 ТНД аварийно-высокая
IF ANB.Tm_sl_p4_TND_Av THEN IF delay[20]  <= 5.0 THEN delay[20] := delay[20] + cycle; END_IF; ELSE delay[20]  := 0.0; END_IF;
AS.Tm_sl_p4_TND_Av := delay[20] > 5.0 OR AS.Tm_sl_p4_TND_Av AND NOT unlock ;
IF AS.Tm_sl_p4_TND_Av AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Температура масла на сливе из опорного подшипника № 4 ТНД аварийно-высокая'; END_IF;
LG.AOb := LG.AOb OR AS.Tm_sl_p4_TND_Av;
AS_INDX[53] := AS.Tm_sl_p4_TND_Av;
//AOs: Температура масла на сливе из подшипника № 2 нагнетателя аварийно-высокая
IF ANB.Tm_sl_opN2_Av THEN IF delay[21]  <= 5.0 THEN delay[21] := delay[21] + cycle; END_IF; ELSE delay[21]  := 0.0; END_IF;
AS.Tm_sl_opN2_Av := delay[21] > 5.0 OR AS.Tm_sl_opN2_Av AND NOT unlock ;
IF AS.Tm_sl_opN2_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Температура масла на сливе из подшипника № 2 нагнетателя аварийно-высокая'; END_IF;
LG.AOs := LG.AOs OR AS.Tm_sl_opN2_Av;
AS_INDX[54] := AS.Tm_sl_opN2_Av;
//AOs: Температура подшипника №2 нагнетателя аварийно-высокая
IF ANB.T_up2_N_Av THEN IF delay[22]  <= 5.0 THEN delay[22] := delay[22] + cycle; END_IF; ELSE delay[22]  := 0.0; END_IF;
AS.T_up2_N_Av := delay[22] > 5.0 OR AS.T_up2_N_Av AND NOT unlock ;
IF AS.T_up2_N_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Температура подшипника №2 нагнетателя аварийно-высокая'; END_IF;
LG.AOs := LG.AOs OR AS.T_up2_N_Av;
AS_INDX[55] := AS.T_up2_N_Av;
//AOs: Температура масла на сливе из подшипника №1 нагнетателя аварийно-высокая
IF ANB.Tm_sl_opN1_Av THEN IF delay[23]  <= 5.0 THEN delay[23] := delay[23] + cycle; END_IF; ELSE delay[23]  := 0.0; END_IF;
AS.Tm_sl_opN1_Av := delay[23] > 5.0 OR AS.Tm_sl_opN1_Av AND NOT unlock ;
IF AS.Tm_sl_opN1_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Температура масла на сливе из подшипника №1 нагнетателя аварийно-высокая'; END_IF;
LG.AOs := LG.AOs OR AS.Tm_sl_opN1_Av;
AS_INDX[56] := AS.Tm_sl_opN1_Av;
//AOs: Температура газа на выходе нагнетателя аварийно-высокая
IF ANB.Tg_out_N_Av THEN IF delay[24]  <= 10.0 THEN delay[24] := delay[24] + cycle; END_IF; ELSE delay[24]  := 0.0; END_IF;
AS.Tg_out_N_Av := delay[24] > 10.0 OR AS.Tg_out_N_Av AND NOT unlock ;
IF AS.Tg_out_N_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Температура газа на выходе нагнетателя аварийно-высокая'; END_IF;
LG.AOs := LG.AOs OR AS.Tg_out_N_Av;
AS_INDX[57] := AS.Tg_out_N_Av;
//------------------------------Calc_AI---------------------------------------
//AOb: Средняя температура на выхлопе турбины аварийно-высокая
IF ANB.ev_T_out_D_Av THEN IF delay[36]  <= 0.2 THEN delay[36] := delay[36] + cycle; END_IF; ELSE delay[36]  := 0.0; END_IF;
AS.ev_T_out_D_Av := delay[36] > 0.2 OR AS.ev_T_out_D_Av AND NOT unlock ;
IF AS.ev_T_out_D_Av AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Средняя температура на выхлопе турбины аварийно-высокая'; END_IF;
LG.AOb := LG.AOb OR AS.ev_T_out_D_Av;
AS_INDX[58] := AS.ev_T_out_D_Av;
//AOs: Обороты ТВД аварийно-высокие
IF ANB.ev_N_VD_Av THEN IF delay[25]  <= 3.0 THEN delay[25] := delay[25] + cycle; END_IF; ELSE delay[25]  := 0.0; END_IF;
AS.ev_N_VD_Av := delay[25] > 3.0 OR AS.ev_N_VD_Av AND NOT unlock ;
IF AS.ev_N_VD_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Обороты ТВД аварийно-высокие'; END_IF;
LG.AOs := LG.AOs OR AS.ev_N_VD_Av;
AS_INDX[60] := AS.ev_N_VD_Av;
//AOs: Обороты ТНД аварийно-высокие
IF ANB.ev_N_ND_Av THEN IF delay[26]  <= 2.0 THEN delay[26] := delay[26] + cycle; END_IF; ELSE delay[26]  := 0.0; END_IF;
AS.ev_N_ND_Av := delay[26] > 2.0 OR AS.ev_N_ND_Av AND NOT unlock ;
IF AS.ev_N_ND_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Обороты ТНД аварийно-высокие'; END_IF;
LG.AOs := LG.AOs OR AS.ev_N_ND_Av;
AS_INDX[61] := AS.ev_N_ND_Av;
//AOs: Приведенные обороты ТВД аварийно-высокие
IF ANB.ev_VD_pr_Av THEN IF delay[28]  <= 3.0 THEN delay[28] := delay[28] + cycle; END_IF; ELSE delay[28]  := 0.0; END_IF;
AS.ev_VD_pr_Av := delay[28] > 3.0 OR AS.ev_VD_pr_Av AND NOT unlock ;
IF AS.ev_VD_pr_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Приведенные обороты ТВД аварийно-высокие'; END_IF;
LG.AOs := LG.AOs OR AS.ev_VD_pr_Av;
AS_INDX[63] := AS.ev_VD_pr_Av;
//AOs: Приведенные обороты ТНД аварийно-высокие
IF ANB.ev_ND_pr_Av THEN IF delay[29]  <= 2.0 THEN delay[29] := delay[29] + cycle; END_IF; ELSE delay[29]  := 0.0; END_IF;
AS.ev_ND_pr_Av := delay[29] > 2.0 OR AS.ev_ND_pr_Av AND NOT unlock ;
IF AS.ev_ND_pr_Av AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Приведенные обороты ТНД аварийно-высокие'; END_IF;
LG.AOs := LG.AOs OR AS.ev_ND_pr_Av;
AS_INDX[64] := AS.ev_ND_pr_Av;
//AOb: Средняя температура на выхлопе турбины аварийно низкая [22.08.08 dfc]
//#IF ((LG.rStart or LG.GPA_Work) and Calc_AI.VD_pr.PV > 40.0 and not Calc_AI.VD_pr.fault) or LG.Check_PZ and ANB.ev_T_out_D_An THEN IF delay[65]  <= 0.0 THEN delay[65] := delay[65] + cycle; END_IF; ELSE delay[65]  := 0.0; END_IF;
AS.ev_T_out_D_An := delay[65] > 0.0 OR AS.ev_T_out_D_An AND NOT unlock ;
IF AS.ev_T_out_D_An AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Средняя температура на выхлопе турбины аварийно низкая'; END_IF;
LG.AOb := LG.AOb OR AS.ev_T_out_D_An;
AS_INDX[65] := AS.ev_T_out_D_An;
//AOb: Нерасцепление пусковой муфты [22.08.08 dfc]
//#IF (Calc_AI.VD_pr.PV > 40.0 and not Calc_AI.VD_pr.fault) or LG.Check_PZ and DGI.PM_ON THEN IF delay[66]  <= 3.0 THEN delay[66] := delay[66] + cycle; END_IF; ELSE delay[66]  := 0.0; END_IF;
AS.PM_ON := delay[66] > 3.0 OR AS.PM_ON AND NOT unlock ;
IF AS.PM_ON AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Нерасцепление пусковой муфты'; END_IF;
LG.AOb := LG.AOb OR AS.PM_ON;
AS_INDX[66] := AS.PM_ON;
//AOb: ТР: Отказ СК
IF ((FR.L3GCV and Q_ON.MZ and Q_ON.MG) or LG.Check_PZ) and LG.SK_fault THEN IF delay[67]  <= 0.0 THEN delay[67] := delay[67] + cycle; END_IF; ELSE delay[67]  := 0.0; END_IF;
AS.SK_fault := delay[67] > 0.0 OR AS.SK_fault AND NOT unlock ;
LG.AOb := LG.AOb OR AS.SK_fault;
AS_INDX[67] := AS.SK_fault;

//AOb: Давление дымовых газов в выхлопном коробе аварийно-высокое
IF ANB.Pg_vihlop_Av THEN IF delay[68]  <= 20.0 THEN delay[68] := delay[68] + cycle; END_IF; ELSE delay[68]  := 0.0; END_IF;
AS.Pg_vihlop_Av := delay[68] > 20.0 OR AS.Pg_vihlop_Av AND NOT unlock ;
IF AS.Pg_vihlop_Av AND Str_PLC.first_AOb = ''  THEN  Str_PLC.first_AOb:= 'Давление дымовых газов в выхлопном коробе аварийно-высокое'; END_IF;
LG.AOb := LG.AOb OR AS.Pg_vihlop_Av;
AS_INDX[68] := AS.Pg_vihlop_Av;

//AOs: Давление масла в коллекторе смазки (96QL) аварийно-низкое
IF Q_ON.MS AND ANB.P_msm_An THEN IF delay[69]  <= 5.0 THEN delay[69] := delay[69] + cycle; END_IF; ELSE delay[69]  := 0.0; END_IF;
AS.P_msm_An := delay[69] > 5.0 OR AS.P_msm_An AND NOT unlock ;
IF AS.P_msm_An AND Str_PLC.first_AOs = ''  THEN  Str_PLC.first_AOs:= 'Давление масла в коллекторе смазки аварийно-низкое'; END_IF;
LG.AOs := LG.AOs OR AS.P_msm_An;
AS_INDX[69] := AS.P_msm_An;

//______ Формирование звукового сигнала _______________________________________________
L_SND_COUNT := FALSE;
FOR j := 0 TO 254 BY 1 DO
IF SND_AS_OFF[j] = FALSE AND ((BTN_SND_OFF OR DGI.Btn_Kvitir) AND AS_INDX[j]) THEN
SND_AS_OFF[j] := TRUE;
ELSE IF SND_AS_OFF[j] = TRUE AND unlock THEN
SND_AS_OFF[j] := FALSE;
END_IF;
END_IF;
IF L_SND_COUNT = FALSE THEN
L_SND_COUNT := AS_INDX[j] AND NOT SND_AS_OFF[j];
END_IF;
END_FOR;
SND_AS := L_SND_COUNT;
"""