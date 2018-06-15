#ifndef _NEDDF07_H_
   #define _NEDDF07_H_

#include "cobbler.h"

class tED007 : public tCobbler
{
public:
  tED007() : tCobbler(572){}
  void sCO                     (char *c) {moveX(c,   0,   2, 0);}
  void sINVESTOR               (char *c) {moveN(c,   2,  10, 0);}
  void sINVESTMENT             (char *c) {moveN(c,  12,   6, 0);}
  void sASSET_LIABILITY        (char *c) {moveX(c,  18,   1, 0);}
  void sFNC_IND                (char *c) {moveX(c,  19,   1, 0);}
  void sCLASS_CODE             (char *c) {moveN(c,  20,   3, 0);}
  void sBRANCH                 (char *c) {moveN(c,  23,   4, 0);}
  void sEXPENSES_REGION        (char *c) {moveN(c,  27,   4, 0);}
  void sTYPE                   (char *c) {moveN(c,  31,   1, 0);}
  void sPERIOD                 (char *c) {moveN(c,  32,   3, 0);}
  void sBA9_IND                (char *c) {moveN(c,  35,   1, 0);}
  void sTERM                   (char *c) {moveN(c,  36,   1, 0);}
  void sME_TERM_IND            (char *c) {moveN(c,  37,   1, 0);}
  void sRATE                   (char *c) {moveN(c,  38,   7, 4);}
  void sRATE_TYPE              (char *c) {moveX(c,  45,   1, 0);}
  void sLINKED_RATE_TYPE       (char *c) {moveN(c,  46,  12, 0);}
  void sCURRENCY               (char *c) {moveX(c,  58,   3, 0);}
  void sCAPITAL                (char *c) {moveN(c,  61,  15, 2);}
  void sDAILY_INT_SIGN         (char *c) {moveX(c,  76,   1, 0);}
  void sDAILY_INT              (char *c) {moveN(c,  77,  14, 6);}
  void sACCRUED_INT_SIGN       (char *c) {moveX(c,  91,   1, 0);}
  void sACCRUED_INT            (char *c) {moveN(c,  92,  14, 2);}
  void sENTRY_DATE             (char *c) {moveN(c, 106,   8, 0);}
  void sEXPIRY_DATE            (char *c) {moveN(c, 114,   8, 0);}
  void sNEXT_INT_DATE          (char *c) {moveN(c, 122,   8, 0);}
  void sLAST_TRAN_DATE         (char *c) {moveN(c, 130,   8, 0);}
  void sDROP_DATE              (char *c) {moveN(c, 138,   8, 0);}
  void sINT_FREQ               (char *c) {moveN(c, 146,   3, 0);}
  void sINT_PAYM_METHOD        (char *c) {moveN(c, 149,   1, 0);}
  void sBLOCK_STATUS           (char *c) {moveN(c, 150,   2, 0);}
  void sPLEDGED                (char *c) {moveX(c, 152,   1, 0);}
  void sLIMIT                  (char *c) {moveN(c, 153,  13, 0);}
  void sDCAR                   (char *c) {moveN(c, 166,   5, 0);}
  void sTCIS_NO                (char *c) {moveN(c, 171,  10, 0);}
  void sSARB_CODE              (char *c) {moveX(c, 181,   4, 0);}
  void sFIN_BRANCH             (char *c) {moveX(c, 185,   6, 0);}
  void sAVECAPOUT              (char *c) {moveN(c, 191,  22, 2);}
  void sAVEUNCAPACCRINT        (char *c) {moveN(c, 213,  22, 2);}
  void sSTARTINTRATE           (char *c) {moveN(c, 235,   9, 6);}
  void sFILLER1                (char *c) {moveN(c, 244,   5, 0);}
  void sRUNDATE                (char *c) {moveN(c, 249,   8, 0);}
  void sHOGANCISNO             (char *c) {moveN(c, 257,  12, 0);}
  void sINTPAID                (char *c) {moveN(c, 269,  14, 2);}
  void sINTREC                 (char *c) {moveN(c, 283,  14, 2);}
  void sSTATUS                 (char *c) {moveN(c, 297,   1, 0);}
  void sBACKDATED_INT_SIGN     (char *c) {moveX(c, 298,   1, 0);}
  void sBACKDATED_INT          (char *c) {moveN(c, 299,  14, 6);}
  void sBASERATE               (char *c) {moveN(c, 313,  18, 6);}
  void sVARIANCEIND            (char *c) {moveX(c, 331,  1, 0);}
  void sBANDDIFF               (char *c) {moveN(c, 332,  18, 6);}
  void sSOURCESYSTEM           (char *c) {moveX(c, 350,  4, 0);}
  void sAVAILABLEBALANCE       (char *c) {moveN(c, 354,  22, 2);}
  void sNOTICEPERIOD           (char *c) {moveN(c, 376,  8, 0);}
  void sORIGINVESTAMT_SIGN      (char *c) {moveX(c, 384,  1, 0);}
  void sORIGINVESTAMT           (char *c) {moveN(c, 385, 22, 2);}
  void sFIXEDAMT_SIGN           (char *c) {moveX(c, 407,  1, 0);}
  void sFIXEDAMT                (char *c) {moveN(c, 408, 22, 2);}
  void sACCESSPERC_SIGN         (char *c) {moveX(c, 430,  1, 0);}
  void sACCESSPERC              (char *c) {moveN(c, 431,  7, 2);}
  void sACCESSAMT_SIGN          (char *c) {moveX(c, 438,  1, 0);}
  void sACCESSAMT               (char *c) {moveN(c, 439, 22, 2);}
  void sACCESSCAP_SIGN          (char *c) {moveX(c, 461,  1, 0);}
  void sACCESSCAP               (char *c) {moveN(c, 462, 22, 2);}
  void sACCESSFLOOR_SIGN        (char *c) {moveX(c, 484,  1, 0);}
  void sACCESSFLOOR             (char *c) {moveN(c, 485, 22, 2);}
  void sWITHDRAWALBAL_SIGN      (char *c) {moveX(c, 507,  1, 0);}
  void sWITHDRAWALBAL           (char *c) {moveN(c, 508, 22, 2);}
  void sDEPOSITBAL_SIGN         (char *c) {moveX(c, 530,  1, 0);}
  void sDEPOSITBAL              (char *c) {moveN(c, 531, 22, 2);}
  void sPREVRESETDATE           (char *c) {moveX(c, 553,  8, 0);}
  void sNEXTRESETDATE           (char *c) {moveX(c, 561,  8, 0);} 
  void sRESETFREQ               (char *c) {moveX(c, 569,  2, 0);}
  void sRATEFLAG                (char *c) {moveX(c, 571,  1, 0);}   
//  void sPENALTYAMOUNT_SIGN      (char *c) {moveX(c, 553,  1, 0);}
//  void sPENALTYAMOUNT           (char *c) {moveN(c, 555, 22, 2);}
//  void sPENALTYCOMMENTS         (char *c) {moveX(c, 577, 300, 0);}
};

#endif
