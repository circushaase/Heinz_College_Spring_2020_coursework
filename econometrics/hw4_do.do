clear all
set type double 
set more off

cd "C:\Users\Lara\Documents\Econo2\hw4"

log using "hw4_log", replace

use "lowbirth.dta", clear

reg lowbrth afdcprc lphypc lbedspc lpcinc lpopul i.county i.year

reg lowbrth afdcprc lphypc lbedspc lpcinc lpopul i.county i.year, robust

reg lowbrth afdcprc lphypc lbedspc lpcinc lpopul i.county i.year, cluster(county)


***** Part 1C

gen dum_year = 0
replace dum_year = 1 if year == 1990
sort county
* Calculate mean by county *
foreach x in lowbrth afdcprc lphypc lbedspc lpcinc lpopul dum_year{
	by county: egen `x'_mean = mean(`x')
}
* Demean variables *
foreach x in lowbrth afdcprc lphypc lbedspc lpcinc lpopul dum_year{
	gen `x'_dm = `x' - `x'_mean
}

reg *_dm,  vce(cluster county)



****** Part 1E

gen afdc2 = afdcprc^2

xtset county year

xtreg lowbrth afdcprc afdc2 lphypc lbedspc lpcinc lpopul dum_year, fe cluster(county)


******Q2******

use "curfews_class.dta", clear

gen E = 0
replace E = 1 if t==0

egen cityid=group(city) 

tsset cityid year

gen Emin= year-enacted <=-5
gen Emax= year-enacted >=5

xi: areg lnarrests Emin l(-4/-2).E E l(1/4).E Emax i.year, abs(city) cluster(city)


mat coeff=[_b[Emin]\  _b[F4.]\ _b[F3.]\ _b[F2.]\ 0\ _b[E]\ _b[L1.]\ _b[L2.]\ _b[L3.]\ _b[L4.]\  _b[Emax]]
mat se=[_se[Emin]\  _se[F4.]\ _se[F3.]\ _se[F2.]\ 0\ _se[E]\ _se[L1.]\ _se[L2.]\ _se[L3.]\ _se[L4.]\  _se[Emax]]
mat upper=coeff+((1.96)*se)
mat lower=coeff-((1.96)*se)
mat x=(-5\-4\-3\-2\-1\0 \1 \2 \3 \4 \5)
mat data=[coeff,upper,lower,x]
svmat data
rename data1 coeff
rename data2 upper
rename data3 lower
rename data4 x
twoway (line coeff x, lpattern(solid) lcolor(black)) (line upper x, lpattern(dash)  lcolor(black)) (line lower x, lpattern(dash) lcolor(black)), xline(0, lpattern(shortdash)) legend(off)xtitle(Years Since Enactment) title("Estimates and 95% Confidence Interval")  xlabel(-5 -4 -3 -2 -1 0 1 2 3 4 5)
graph export event_study_fig1.pdf, replace

**********
use "curfews_class.dta", clear
gen E = 0
replace E = 1 if t==0
egen cityid=group(city) 
tsset cityid year
gen Emin= year-enacted <=-3
gen Emax= year-enacted >=3
xi: areg lnarrests Emin l(-3/-2).E E l(1/3).E Emax i.year, abs(city) cluster(city)


use "curfews_class.dta", clear
gen E = 0
replace E = 1 if t==0
egen cityid=group(city) 
tsset cityid year
gen Emin= year-enacted <=-8
gen Emax= year-enacted >=8
xi: areg lnarrests Emin l(-8/-2).E E l(1/8).E Emax i.year, abs(city) cluster(city)

*****
use "curfews_class.dta", clear
gen E = 0
replace E = 1 if t==0
egen cityid=group(city) 
tsset cityid year
gen Emin= year-enacted <=-5
gen Emax= year-enacted >=5
xi: areg lnarrests Emin l(-4/-1).E l(1/4).E Emax i.year i.t, abs(city) cluster(city)


log close
translate hw4_log.smcl hw4_log.pdf