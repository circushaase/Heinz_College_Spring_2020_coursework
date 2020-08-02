*** Metrics
*** Figures 4.2 4.4 4.5
*** Tables 4.1
*** MLDA Regression Discontinuity (based on data from Carpenter and Dobkin 2009)

clear

// set to directory where data is located
cd "/Users/lhaase/Documents"

// create a folder called "Output" in that directory

use AEJfigs.dta

* All = all deaths
gen age = agecell - 21
gen over21 = agecell >= 21

gen age2 = age^2
gen age3 = age^3
gen over_age = over21*age
gen over_age2 = over21*age2
gen over_age3 = over21*age3

* Regressions for Figure 4.2.
* linear trend, and linear on each side
reg all age over21
predict allfitlin
reg all age over21 over_age
predict allfitlini

* Regressions for Figure 4.4.
* Quadratic, and quadratic on each side
reg all age age2 age3 over21
predict allfitq
reg all age age2 age3 over21 over_age over_age2 over_age3
predict allfitqi

label variable all       "Mortality rate from all causes (per 100,000)"
label variable allfitlin "Mortality rate from all causes (per 100,000)"
label variable allfitqi  "Mortality rate from all causes (per 100,000)"

* Figure 4.4.		 
twoway (scatter all agecell) (line allfitlin allfitqi agecell if age < 0,  lcolor(red black) lwidth(medthick medthick) lpattern(dash)) ///
                             (line allfitlin allfitqi agecell if age >= 0, lcolor(red black) lwidth(medthick medthick) lpattern(dash)), ///
							 xline(21, lcolor(cranberry)) legend(off)

graph save Output/fig44_3, replace
graph export Output/fig44_3.pdf, replace


log close
translate hw1_log.smcl hw1_log.pdf
