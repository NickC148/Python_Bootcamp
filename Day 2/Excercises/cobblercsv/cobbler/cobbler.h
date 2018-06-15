#ifndef _COBBLER_H_
#define _COBBLER_H_ "$Revision: 47 $ $Date: 2009-01-15 10:22:38 +0200 (Thu, 15 Jan 2009) $"

#include "versions.h"
HEADER_VERSION(_COBBLER_H_);

/*
 **************************************************************************
 *
 *  System :
 *
 *  File   : $URL: http://zug/Nedbank/MCCA/targsrc/c/util/cobbler.h $
 *
 *  Description :
 *
 *  Created By : BB&D
 *
 *  Date Created :
 *
 *  $Author: rudolph $
 *
 *  $Revision: 47 $
 *
 *  $Date: 2009-01-15 10:22:38 +0200 (Thu, 15 Jan 2009) $
 *
 *  Change History :
 *
 *  $Log: $
 *
 **************************************************************************
 */


#include "ti.h"

#define xCobblerErrorName "xCobblerError"

class tCobbler;
class xCept;

class xCobblerError : public xCept
{
public:
  enum eError
  { errCobOK
  , errCobInit
  , errCobShut
  , errCobMem
  , errCobWrit
  };
  xCobblerError(pchar aFname, int aLine, eError aError,pchar aMsg1);
  xCobblerError(const xCobblerError& aX)
  : xCept(aX) {}
};

#define XCobblerError(err,msg1) \
        xCobblerError(__FILE__, __LINE__, xCobblerError::err,msg1)

const char HIGH_VALUES[] = "\xFF";
const char LOW_VALUES[]  = "\x00";
const char SPACES[]      = " ";
const char ZEROES[]      = "0";

class tCobbler
{
public:
  void Write(int FileHandle);
  char* GetCStructure()  {return CStructure;}
  int   GetCStructSize() {return CStructSize;}

protected:
  ~tCobbler();
  tCobbler(int SSize);
  void moveG(char *SData,int SOffset,int SLen,int SScale,int SOccur = 0,int SMaxOccur = 1,int SEveryOccur = 0);
  void moveN(char *SData,int SOffset,int SLen,int SScale,int SOccur = 0,int SMaxOccur = 1,int SEveryOccur = 0);
  void move9(char *SData,int SOffset,int SLen,int SScale,int SOccur = 0,int SMaxOccur = 1,int SEveryOccur = 0);
  void move9ts(char *SData,int SOffset,int SLen,int SScale,int SOccur = 0,int SMaxOccur = 1,int SEveryOccur = 0);
  void moveX(char *SData,int SOffset,int SLen,int SScale,int SOccur = 0,int SMaxOccur = 1,int SEveryOccur = 0);
  void moveA(char *SData,int SOffset,int SLen,int SScale,int SOccur = 0,int SMaxOccur = 1,int SEveryOccur = 0);
  void moveS(char *SData,int SOffset,int SLen,int SScale,int SOccur = 0,int SMaxOccur = 1,int SEveryOccur = 0);
  void moveL(char *SData,int SOffset,int SLen,int SScale,int SOccur = 0,int SMaxOccur = 1,int SEveryOccur = 0);
  void moveD(double Data,int SOffset,int SLen,int SScale,int SOccur = 0,int SMaxOccur = 1,int SEveryOccur = 0);
  void moveDts(double Data,int SOffset,int SLen,int SScale,int SOccur = 0,int SMaxOccur = 1,int SEveryOccur = 0);
  void moveE(char *SData,int SOffset,int SLen,int SScale,int SOccur = 0,int SMaxOccur = 1,int SEveryOccur = 0);
private:
  char* CStructure;
  int CStructSize;
  tCobbler() {}
};


#endif

