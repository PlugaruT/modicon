"""
Dictionary that contains all information about bits
Each register has a list of bit names, all bits have
associated a bit number
"""
BITMAP = {
    'ALARME_DWORD_1': {
        'TENSIUNE_RETEA': 0,
        'TENSIUNE_UPS': 1,
        'SURSA_DC_T1': 2,
        'SURSA_DC_T2': 3,
        'REDUNDANTA_C1': 4,
        'PROT_F5_T1': 5,
        'PROT_F6_T2': 6,
        'PROT_F7_220_PC': 7,
        'PROT_F8_220_PF': 8,
        'PROT_F9_24_PC': 9,
        'PROT_F10_24_PF': 10,
        'ERROR_U1_MV1_2': 11,
        'ERROR_U2_MV2_3': 12,
        'PLC_U_ERROR': 13,
        'PROT_F13_HI1_1': 14,
        'PROT_F17_SWICH': 15,
        'PROT_F18_T4': 16,
        'PROT_F19_DI': 17,
        'PROT_F20_DO': 18,
        'PROT_F21_AI_AO': 19,
        'EMERGENCY_STOP': 20,
        'INTRARE_1_TRIP': 21,
        'PROT_CF1_TRIP': 22,
        'PROT_CF2_TRIP': 23,
        'CUPLA_TRIP': 24,
        'INTRARE_2_TRIP': 25,
        'PROT_CF3_TRIP': 26,
        'AUX_INTR_1_TRIP': 27,
        'AUX_INTR_2_TRIP': 28,
        'CODITIE_SZ': 29,
        'INITIERE_SZ': 30,
        'SZ_PI1_1_MIN': 31
    },
    'ALARME_DWORD_2': {
        'SZ_PI2_1_MIN': 0,
        'SZ_PI2_1_MAX_1': 1,
        'SZ_PI2_1_MAX_2': 2,
        'ERROR_SEMNAL_4_20_H1_1': 3,
        'ERROR_SEMNAL_4_20_H2_1': 4,
        'ERROR_SEMNAL_4_20_PI1_1': 5,
        'ERROR_SEMNAL_4_20_PI1_2': 6,
        'ERROR_SEMNAL_4_20_PI1_3': 7,
        'ERROR_SEMNAL_4_20_PI1_4': 8,
        'ERROR_SEMNAL_4_20_PI2_1A': 9,
        'ERROR_SEMNAL_4_20_PI2_1B': 10,
        'ERROR_SEMNAL_4_20_PI2_2': 11,
        'ERROR_SEMNAL_4_20_PI2_3': 12,
        'ERROR_SEMNAL_4_20_PI2_4': 13,
        'ERROR_SEMNAL_4_20_PI2_5': 14,
        'ERROR_SEMNAL_4_20_PI2_6': 15,
        'ERROR_SEMNAL_4_20_TI1_1': 16,
        'ERROR_SEMNAL_4_20_TI1_2': 17,
        'ERROR_SEMNAL_4_20_TI2_1': 18,
        'ERROR_SEMNAL_4_20_TI2_2': 19,
        'FAULT_CF1': 20,
        'COM_ERROR_CF1': 21,
        'FAULT_CF2': 22,
        'COM_ERROR_CF2': 23,
        'FAULT_CF3': 24,
        'COM_ERROR_CF3': 25,
        'ERROR_START_CF1': 26,
        'ERROR_RUN_CF1': 27,
        'ERROR_START_CF2': 28,
        'ERROR_RUN_CF2': 29,
        'ERROR_START_CF3': 30,
        'ERROR_RUN_CF3': 31
    },
    'ALARME_DWORD_3': {
        'EROARE_BLINKER_MV1_1': 0,
        'EROARE_TERMICA_MV1_1': 1,
        'EROARE_QF_MV1_1': 2,
        'EROARE_BLINKER_MV1_2': 4,
        'EROARE_TERMICA_MV1_2': 5,
        'EROARE_QF_MV1_2': 6,
        'EROARE_BLINKER_MV1_3': 8,
        'EROARE_TERMICA_MV1_3': 9,
        'EROARE_QF_MV1_3': 10,
        'EROARE_BLINKER_MV2_1': 12,
        'EROARE_TERMICA_MV2_1': 13,
        'EROARE_QF_MV2_1': 14,
        'EROARE_BLINKER_MV2_2': 16,
        'EROARE_TERMICA_MV2_2': 17,
        'EROARE_QF_MV2_2': 18,
        'EROARE_BLINKER_MV2_3': 20,
        'EROARE_TERMICA_MV2_3': 21,
        'EROARE_QF_MV2_3': 22,
        'EROARE_BLINKER_MV2_4': 24,
        'EROARE_TERMICA_MV2_4': 25,
        'EROARE_QF_MV2_4': 26,
        'EROARE_BLINKER_MV3_1': 28,
        'EROARE_TERMICA_MV3_1': 29,
        'EROARE_QF_MV3_1': 20,
    },
    'ALARME_DWORD_4': {
        'EROARE_BLINKER_MV3_2': 0,
        'EROARE_TERMICA_MV3_2': 1,
        'EROARE_QF_MV3_2': 2,
        'EROARE_BLINKER_MV4_1': 4,
        'EROARE_TERMICA_MV4_1': 5,
        'EROARE_QF_MV4_1': 6,
        'EROARE_BLINKER_MV4_2': 8,
        'EROARE_TERMICA_MV4_2': 9,
        'EROARE_QF_MV4_2': 10,
        'EROARE_BLINKER_MV5_1': 12,
        'EROARE_TERMICA_MV5_1': 13,
        'EROARE_QF_MV5_1': 14,
        'EROARE_BLINKER_MV5_2': 16,
        'EROARE_TERMICA_MV5_2': 17,
        'EROARE_QF_MV5_2': 18
    }
}
