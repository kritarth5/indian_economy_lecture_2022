/* this do file is to prep data that'll be used in the Friday IITKGP presentation  */

/* set globals */
/* Edit this path to where you store the data
global pub_shrug ~/public_shrug/
global $tmp ~/where/you/want/the data/
*/

/* Question: How many Indians have been employed in Services versus Manufacturing post liberalisation */
/* collapse (or aggregate) to national level */
use $pub_shrug/shrug_ec.dta, clear
gen id = "india"
collapse_save_labels
collapse (sum) *emp_manuf *emp_services *emp_all, by(id)
collapse_apply_labels

/* turn variable names we can reshape */
ren (ec90_*) (*_ec1990)
ren (ec98_*) (*_ec1998)
ren (ec05_*) (*_ec2005)
ren (ec13_*) (*_ec2013)

/* reshape data */
reshape long emp_manuf_ec emp_services_ec emp_all_ec, i(id) j(year)

/* turn employment into millions */
foreach sector in manuf services all {
  replace emp_`sector'_ec = emp_`sector'_ec/1000000
}

/* save data */
save $tmp/ec_india_summary, replace

/* plot data */
set scheme pn
twoway (line emp_services_ec year,lwidth(medthick) ) (line emp_manuf_ec year, lwidth(medthick)), ytitle(Employment (Millions)) xtitle(Year) ///
    legend( label(1 "Services") label(2 "Manufacturing") pos(4) ring(0)) 
graphout emp_over_time

/*****************************************************************************/
/* Question: Which regions have seen highest increase in services employment */
/*****************************************************************************/
/* District */
/* use shrug ec data */
use $pub_shrug/shrug_ec.dta, clear

/* merge to pc11 keys */
merge 1:m shrid using $pub_shrug/shrug_pc11_district_key.dta, keep(match) nogen

/* collapse (or aggregate) to district level */
collapse_save_labels
collapse (mean) *emp_manuf *emp_services *emp_all, by(pc11_state_id pc11_state_name pc11_district_id pc11_district_name)
collapse_apply_labels

/* save data */
save $tmp/ec_dist, replace

/* Subistrict */
/* use shrug ec data */
use $pub_shrug/shrug_ec.dta, clear

/* merge to pc11 keys */
merge 1:m shrid using $pub_shrug/shrug_pc11_subdistrict_key.dta, keep(match) nogen

/* collapse (or aggregate) to subdistrict level */
collapse_save_labels
collapse (mean) *emp_manuf *emp_services *emp_all, by(pc11_state_id pc11_state_name pc11_district_id pc11_district_name pc11_subdistrict_id pc11_subdistrict_name)
collapse_apply_labels

/* save data */
save $tmp/ec_subdist, replace


