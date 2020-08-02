clear all
set type double 
set more off

cd "C:\Users\lhaase\Documents\"

log using "hw1_log", replace

use "strike_data.dta", clear

gen cntrdate = date - 15992
gen interstkdt = cntrdate*strike

areg deficit_60 strike cntrdate interstkdt i.dayofwk [aw=weight], absorb(vds) cluster(vds)

****restrict data to 10 day bandwidth
drop if cntrdate>10 | cntrdate <-10
areg deficit_60 strike cntrdate interstkdt i.dayofwk [aw=weight], absorb(vds) cluster(vds)

****restrict data to 5 day bandwidth
drop if cntrdate>5 | cntrdate <-5
areg deficit_60 strike cntrdate interstkdt i.dayofwk [aw=weight], absorb(vds) cluster(vds)
