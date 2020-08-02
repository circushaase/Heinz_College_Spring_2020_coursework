set type double
set more off
clear all

cd "C:\Users\Acer\Desktop\academia\Econometrics\Stata\"

log using "econ2hw2", replace

use "psu_data.dta", clear

** 1. **

** a **
drop if psu475t1 > 46 | psu475t1 < -46
reg enrolt1 m475t1 psu475t1 m475psut1 if qqt1==1, robust

** d. **
reg everelig1 m475t1 psu475t1 m475psut1 if qqt1==1, robust

** e. **
gen x4=psu475t1^4
ivreg everenroll1 (everelig1=m475t1) psu475t1 m475psut1 x4 if qqt1==1, robust

log close
translate "econ2hw2.smcl" "econ2hw2.pdf"