import datetime
import random
import re
from tally.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from calendar import month
from urllib import response
from datetime import datetime, timedelta
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from errno import ETIME
from datetime import date
from re import S
from re import A, S
from this import s
from unittest import signals
from webbrowser import get
from django.db.models.functions import Coalesce
from xml.etree.ElementTree import tostring
from django.db.models import Sum
from cgi import print_arguments
from multiprocessing import context
from symtable import Symbol
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse
from django.db.models.functions import TruncDay
from django.db.models.functions import TruncMonth
from django.db.models.functions import TruncDate
from django.db.models.functions import Extract
from django.db.models import Count
from unittest import TextTestRunner

# Create your views here.

def login(request):
    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        # user = authenticate(username=email,password=password)
        # if user is not None:
        #     request.session['SAdm_id'] = user.id
        #     return redirect( 'Admin_dashboard')

        if Companies.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
                
                member=Companies.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['t_id'] = member.id 
                tally=Companies.objects.filter(id= member.id)
                
                return render(request,'base.html',{'tally':tally})
    
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'Login.html', context)

    return render(request, 'Login.html')

def logout(request):
    if 't_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def register(request):
    return render(request, 'Register.html')

def base(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'base.html',{'tally':tally})
    return redirect("/")

#......................jisha........................

def company_list(request):
    com=Companies.objects.all()
    return render(request,'company_list.html',{'comp':com})    

def change_company(request):
	com=Companies.objects.all()
	return render(request, 'change_company.html',{'comp':com})

def select_c(request):
	com = Companies.objects.all()
	return render(request,'select_c.html',{'com':com})

def shut_cmpny(request):
	com=Companies.objects.all() 
	return render(request, 'shut_cmpny.html',{'com':com})

def shut(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=False
    c.save()
    return redirect('shut_cmpny') 

def enable(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=True
    c.save()
    return redirect('/')

def create_cmpny(request):
    return render(request, 'create_cmpny.html')

def tally_gst(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'gst.html',{'tally':tally})
    return redirect('/')

def gst_tax(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'gst_tax.html',{'tally':tally})
    return redirect('/')

def features(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'features.html',{'tally':tally})
    return redirect('/')

def tds(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'tds.html',{'tally':tally})
    return redirect('/')

def person(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'tds_person.html',{'tally':tally})
    return redirect('/')
    
def c_rates(request):
    return render(request, 'c_rates.html')

def lut_bond(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'lut_bond.html',{'tally':tally})
    return redirect('/')

def groups(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        # grp=tally_group.objects.all()
        grp=tally_group.objects.filter(company=t_id)
        return render(request, 'group.html',{'tally':tally,'grp':grp})
    return redirect('/')

def group_alt(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        grp=tally_group.objects.all()
        return render(request, 'group_alt.html',{'grp':grp,'tally':tally})
    return redirect('/')

def create_group(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            gname=request.POST['gname']
            galias=request.POST['alias']
            under=request.POST['group']
            nature=request.POST['group_nature']
            gross=request.POST['gorss_profit']
            ledg=request.POST['ledger']
            cred=request.POST['debit/credit']
            calc=request.POST['calculation']
            invc=request.POST['invoice']
            grp=tally_group(group_name=gname,
                    group_alias=galias,
                    group_under=under,
                    nature=nature,
                    gross_profit=gross,
                    sub_ledger=ledg,
                    debit_credit=cred,
                    calculation=calc,
                    invoice=invc,
                    company_id=t_id)          
            grp.save()
            print("added")
            return redirect('groups')
        return render(request,'group.html',{'tally':tally})
    return redirect('/')

def currency(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'currency.html',{'tally':tally})
    return redirect("/")

def c_create(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'c_create.html',{'tally':tally})
    return redirect('/')

def create_currency(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            smbl=request.POST['c_symbl']
            fname=request.POST['fname']
            isoc=request.POST['isocode']
            dcml=request.POST['decimal_p']
            amt=request.POST['show_amt']
            sfx=request.POST['suffix']
            spc=request.POST['add_space']
            wrd=request.POST['word_rep']
            ndcml=request.POST['no_decimal']
            crny=currencyAlteration(Symbol=smbl,
                            FormalName = fname,
                            ISOCurrency = isoc,
                            DecimalPlace = dcml,
                            showAmount = amt,
                            suffixSymbol = sfx,
                            AddSpace = spc,
                            wordRep = wrd,
                            DecimalWords = ndcml,
                            company_id=t_id,)          
            crny.save()
            print("added")
            return redirect('c_create')
    return redirect('/')

def rates(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        ccr=currencyAlteration.objects.filter(company_id=t_id)
        ccr1=currencyAlteration.objects.filter(status=0)
        return render(request,'rates.html',{'ccr' : ccr,'tally':tally,'ccr1' : ccr1})
    return redirect('/')

def create_ROE(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            # cmp=Companies.objects.get(id=pk)
            # dt=request.POST['dt']
            crname=request.POST['curname']
            stdr=request.POST['stdr']
            # lv=request.POST['lvr']
            ssr=request.POST['ssr']
            # lv1=request.POST['lvr2']
            bsr=request.POST['bsr']
            croe=rateofexchange(
                            currencyName = crname,
                            std_rate = stdr,
                            
                            sell_specified_rate = ssr,
                            
                            buy_voucher_rate = bsr,company_id=t_id)          
            croe.save()
            return redirect('rates')
        return render(request,'rates.html',{'tally':tally})
    return redirect('/')

def c_alter(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'c_alter.html',{'tally':tally})
    return redirect('/')

def alter_currency(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            smbl=request.POST['c_symbl']
            fname=request.POST['fname']
            isoc=request.POST['isocode']
            dcml=request.POST['decimal_p']
            amt=request.POST['show_amt']
            sfx=request.POST['suffix']
            spc=request.POST['add_space']
            wrd=request.POST['word_rep']
            ndcml=request.POST['no_decimal']
            crny=company_alt_currency(c_symbol=smbl,
                            formal_name = fname,
                            iso_Ccode = isoc,
                            decimal_place = dcml,
                            show_amtM = amt,
                            suffix_smblA = sfx,
                            add_space = spc,
                            word_rep = wrd,
                            no_decimal = ndcml)          
            crny.save()
            print("added")
            return redirect('c_alter')
        return render(request,'a_alter.html',{'tally':tally})
    return redirect('/')

def gocost(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        costt=cost_centre.objects.all()
        return render(request,'cost.html',{'costt' : costt,'tally':tally})
    return redirect('/')

def cost_alt(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        costt=cost_centre.objects.all()
        return render(request,'cost_alt.html',{'costt' : costt,'tally':tally})
    return redirect('/')

def load_centre(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        costt=cost_centre.objects.all()
        if request.method=='POST':
            nm=request.POST['cst_name']
            als=request.POST['alias']
            unr=request.POST['c_under']
            cost=cost_centre(c_name=nm,
                            cost_alias = als,
                            under = unr,
                            company_id=t_id,)          
            cost.save()
            print("added")
        return render(request,'cost.html',{'costt':costt,'tally':tally})
		

def create_tds(request,pk):
    
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		t_reg = request.POST['tan_reg_no']
		tax_clct = request.POST['tax_ded_clctn']
		ded_type = request.POST['deductor_type']
		ded_bd = request.POST['ded_brachdevision']
		prsn_res = request.POST['person_res']
		ignr = request.POST['ignore_it']
		st_itm = request.POST['tds_stock_items']
		
		ctds=Tds_Details(tan_regno=t_reg,
                        tan = tax_clct,
                        deductor_type = ded_type,
                        deductor_branch = ded_bd,
                        person_details = prsn_res,
                        ignore_it = ignr,
                        active_tds = st_itm,
						company = id)          
		ctds.save()
		print("added")
		return redirect('/')
	return render(request,'tds.html')

def person_tds(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		name = request.POST['name']
		sd = request.POST['son_daughter']
		des = request.POST['designation']
		pan = request.POST['pan']
		ftno = request.POST['flat_no']
		pnm = request.POST['premise_name']
		str = request.POST['street']
		are = request.POST['area']
		city = request.POST['city']
		st = request.POST['state']
		pcd = request.POST['pincode']
		m_no = request.POST['mobile_no']
		std = request.POST['std_code']
		tph = request.POST['telephone']
		emal = request.POST['email']
	    
		prs=tds_person(name=name,
                        son_daughter = sd,
                        designation = des,
                        pan = pan,
                        flat_no = ftno,
                        building = pnm,
                        street = str,
                        area = are,
                        town = city,
                        state = st,
                        pincode = pcd,
                        mobile = m_no,
                        std = std,
                        telephone = tph,
                        email = emal,
						company = id)          
		prs.save()
		print("added")
		return redirect('/')
	return render(request,'tds_person.html')

def vouchers(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'vouchers.html',{'tally':tally})
    return redirect('/')

def create_voucher(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            # cmp=Companies.objects.get(id=pk)
        
            nm=request.POST['vname']
            als=request.POST['alias']
            vtp=request.POST['vouch_type']
            abbr=request.POST['Abbreviation']
            actp=request.POST['activate_Vtype']
            mvno=request.POST['method_Vno']
            prnt=request.POST['prevent']
            acn=request.POST['advance_con']
            use=request.POST['use_EDV']
            zero=request.POST['zero_val']
            mvd=request.POST['mVoptional_defualt']
            anar=request.POST['allow_nar']
            prvdl=request.POST['provide_L']
            jrnl=request.POST['manu_jrnl']
            track=request.POST['track_purchase']
            enbl=request.POST['enable_acc']
            prntva=request.POST['prnt_VA_save']
            prntfml=request.POST['prnt_frml']
            juri=request.POST['jurisdiction']
            tprint=request.POST['title_print']
            setaltr=request.POST['set_alter']
            posinv=request.POST['pos_invoice']
            msg1=request.POST['msg_1']
            msg2=request.POST['msg_2']
            dbank=request.POST['default_bank']
            nc=request.POST['name_class']

            vhr=Voucher(voucher_name=nm,
                        alias = als,
                        voucher_type = vtp,
                        abbreviation = abbr,
                        voucherActivate = actp,
                        voucherNumber = mvno,
                        preventDuplicate = prnt,
                        advance_con = acn,
                        voucherEffective = use,
                        transaction = zero,
                        make_optional = mvd,
                        voucherNarration = anar,
                        provideNarration = prvdl,
                        manu_jrnl = jrnl,
                        track_purchase = track,
                        enable_acc = enbl,
                        prnt_VA_save = prntva,
                        prnt_frml = prntfml,
                        jurisdiction = juri,
                        title_print = tprint,
                        set_alter = setaltr,
                        pos_invoice = posinv,
                        msg_1 = msg1,
                        msg_2 = msg2,
                        default_bank = dbank,
                        name_class = nc,
                        company_id=t_id)          
            vhr.save()
            print("Added")
            return redirect('base')
        return render(request,'vouchers.html',{'tally':tally})
    return redirect('/')

def vouch_advance(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'vouch_advance.html',{'tally':tally})
    return redirect('/')

def create_voucher_advance(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            stn=request.POST['starting_no']
            npw=request.POST['numerical_partwidth']
            pz=request.POST['prefill_zero']
            rsad=request.POST['restart_applicable_dt']
            rsrtsno=request.POST['restart_startingno']
            repert=request.POST['restart_particular']
            pread=request.POST['prefix_applicable_dt']
            preper=request.POST['prefix_particular']
            sfxapd=request.POST['suffix_applicable_dt']
            sfxper=request.POST['suffix_particular']

            cva=voucher_advanceconf(starting_no=stn,
                            numerical_partwidth = npw,
                            prefill_zero = pz,
                            restart_applicable_dt = rsad,
                            restart_startingno = rsrtsno,
                            restart_particular = repert,
                            prefix_applicable_dt = pread,
                            prefix_particular = preper,
                            suffix_applicable_dt = sfxapd,
                            suffix_particular = sfxper)    
            cva.save()  
            print("Added")
            return redirect('/')
        return render(request,'vouch_advance.html',{'tally':tally})
    return redirect('/')

def ledgers(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        # grp=tally_group.objects.all()
        grp=tally_group.objects.filter(company=t_id)
        return render(request,'ledgers.html',{'grp' : grp,'tally':tally})
    return redirect('ledgers')

def create_ledger(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            nm=request.POST.get('name')
            als=request.POST.get('alias')
            under=request.POST.get('under')
            mname=request.POST.get('mailingname')
            adr=request.POST.get('address')
            st=request.POST.get('state')
            cntry=request.POST.get('country')
            pin=request.POST.get('pincode')
            pno=request.POST.get('pan_no')
            bdetls=request.POST.get('bank_details')
            rtype=request.POST.get('registration_type')
            gst_uin=request.POST.get('gst_uin')
            opnbn=request.POST.get('opening_blnc')

            spdl=request.POST.get('set_odl')
            achnm=request.POST.get('ac_holder_nm')
            acno=request.POST.get('acc_no')
            ifsc=request.POST.get('ifsc_code')
            scode=request.POST.get('swift_code')
            bn=request.POST.get('bank_name')
            brnch=request.POST.get('branch')
            sacbk=request.POST.get('SA_cheque_bk')
            ecp=request.POST.get('Echeque_p')
            sacpc=request.POST.get('SA_chequeP_con')

            typofled=request.POST.get('type_of_ledger')
            rometh=request.POST.get('rounding_method')
            rolmt=request.POST.get('rounding_limit')

            typdutytax=request.POST.get('type_duty_tax')
            taxtyp=request.POST.get('tax_type')
            valtype=request.POST.get('valuation_type')
            rateperu=request.POST.get('rate_per_unit')
            percalc=request.POST.get('percentage_of_calcution')
            rondmethod=request.POST.get('rond_method')
            roimlit=request.POST.get('rond_limit')

            gstapplicbl=request.POST.get('gst_applicable')
            sagatdet=request.POST.get('setalter_gstdetails')
            typsupply=request.POST.get('type_of_supply')
            asseval=request.POST.get('assessable_value')
            appropto=request.POST.get('appropriate_to')
            methcalcu=request.POST.get('method_of_calculation')

            balbillbybill=request.POST.get('balance_billbybill')
            credperiod=request.POST.get('credit_period')
            creditdaysvouch=request.POST.get('creditdays_voucher')
            
            ldr=tally_ledger(name=nm,alias=als,under=under,mname=mname,address=adr,state=st,country=cntry,
                            pincode=pin,pan_no=pno,bank_details=bdetls,registration_type=rtype,gst_uin=gst_uin,
                            opening_blnc=opnbn,set_odl=spdl,ac_holder_nm=achnm,acc_no=acno,ifsc_code=ifsc,swift_code=scode,
                            bank_name=bn,branch=brnch,SA_cheque_bk=sacbk,Echeque_p=ecp,SA_chequeP_con=sacpc,
                            type_of_ledger=typofled,rounding_method=rometh,rounding_limit=rolmt,type_duty_tax=typdutytax,tax_type=taxtyp,
                            valuation_type=valtype,rate_per_unit=rateperu,percentage_of_calcution=percalc,rond_method=rondmethod,rond_limit=roimlit,
                            gst_applicable=gstapplicbl,setalter_gstdetails=sagatdet,type_of_supply=typsupply,assessable_value=asseval,
                            appropriate_to=appropto,method_of_calculation=methcalcu,balance_billbybill=balbillbybill,credit_period=credperiod,
                            creditdays_voucher=creditdaysvouch,company_id=t_id)
            
            ldr.save()
            if under =="Bank Accounts":
                group_under = Account_Books_Group_under.objects.all()
                ad =""
                for i in group_under:
                    if i.group_under_Name == under:

                        ad = under

                        gup=Account_Books_Group_under.objects.get(group_under_Name=under)

                        account_book_ledger = Account_Books_Ledger()
                        account_book_ledger.ledger_name = nm
                        account_book_ledger.group_under = gup
                        account_book_ledger.ledger_opening_bal = opnbn
                        account_book_ledger.ledger_opening_bal_type = type
                        account_book_ledger.save()
                
                
                if ad != under:
                    account_book_group_under = Account_Books_Group_under()
            
                    account_book_group_under.group_under_Name =under
                    account_book_group_under.save()

                    account_book_ledger = Account_Books_Ledger()
                    account_book_ledger.ledger_name = nm
                    gu =Account_Books_Group_under.objects.get(id=account_book_group_under.id)
                    account_book_ledger.group_under = gu
                    account_book_ledger.ledger_opening_bal = opnbn
                    account_book_ledger.ledger_opening_bal_type = type
                    account_book_ledger.save()


            if under =="Cash in Hand":
                group_under = Account_Books_Group_under.objects.all()
                ad =""
                for i in group_under:
                    if i.group_under_Name == under:

                        ad = under

                        gup=Account_Books_Group_under.objects.get(group_under_Name=under)

                        account_book_ledger = Account_Books_Ledger()
                        account_book_ledger.ledger_name = nm
                        account_book_ledger.group_under = gup
                        account_book_ledger.ledger_opening_bal = opnbn
                        account_book_ledger.ledger_opening_bal_type = type
                        account_book_ledger.save()
                
                
                if ad != under:
                    account_book_group_under = Account_Books_Group_under()
            
                    account_book_group_under.group_under_Name =under
                    account_book_group_under.save()

                    account_book_ledger = Account_Books_Ledger()
                    account_book_ledger.ledger_name = nm
                    gu =Account_Books_Group_under.objects.get(id=account_book_group_under.id)
                    account_book_ledger.group_under = gu
                    account_book_ledger.ledger_opening_bal = opnbn
                    account_book_ledger.ledger_opening_bal_type = type
                    account_book_ledger.save()
            # return render(request,'ledgers.html',{'tally':tally})
            return render(request,'account_books_ledger.html',{'tally':tally})
    return redirect('/')

def ledger_chequed(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'ledger_chequed.html',{'tally':tally})
    return redirect('/')

def create_ledgerdimension(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method == 'POST':
            cw= request.POST.get('cheque_width')
            ch= request.POST.get('cheque_height')
            sle= request.POST.get('startL_leftEdge')
            slte= request.POST.get('startL_topEdge')
            dlle= request.POST.get('distancel_leftEdge')
            dlte= request.POST.get('distancel_topEdge')
            ds= request.POST.get('date_style')
            dts= request.POST.get('date_seperator')
            sw= request.POST.get('separator_width')
            cd= request.POST.get('character_distance')
            pdle= request.POST.get('Pdistancel_leftEdge')
            pdlte= request.POST.get('Pdistancel_topEdge')
            aw= request.POST.get('area_width')
            sldte= request.POST.get('secondL_DTE')
            sflh= request.POST.get('secondfirstL_height')
            fldte= request.POST.get('firstL_dTE')
            slfle= request.POST.get('sl_fisrtl_LE')
            slsle= request.POST.get('sl_secondl_LE')
            awa= request.POST.get('amount_widtharea')
            cfnmp= request.POST.get('currencyFNM_print')
            dfte= request.POST.get('df_TE')
            sle= request.POST.get('startL_LE')
            amwa= request.POST.get('amt_widtharea')
            csp= request.POST.get('currencyS_print')
            cn= request.POST.get('company_name')
            pcn= request.POST.get('print_CN')
            sfs= request.POST.get('salutation_Fsign')
            sss= request.POST.get('salutation_Ssign')
            tes= request.POST.get('top_Edistance')
            slfl= request.POST.get('startLF_leftE')
            wsa= request.POST.get('width_sign_area')
            hsa= request.POST.get('height_sign_area')

            cld= ledger_cheque_demension(cheque_width=cw,cheque_height=ch,startL_leftEdge=sle,startL_topEdge=slte,distancel_leftEdge=dlle,
                                        distancel_topEdge=dlte,date_style=ds,date_seperator=dts,separator_width=sw,character_distance=cd,
                                        Pdistancel_leftEdge=pdle,Pdistancel_topEdge=pdlte,area_width=aw,secondL_DTE=sldte,secondfirstL_height=sflh,
                                        firstL_dTE=fldte,sl_fisrtl_LE=slfle,sl_secondl_LE=slsle,amount_widtharea=awa,currencyFNM_print=cfnmp,
                                        df_TE=dfte,startL_LE=sle,amt_widtharea=amwa,currencyS_print=csp,company_name=cn,print_CN=pcn,
                                        salutation_Fsign=sfs,salutation_Ssign=sss,top_Edistance=tes,startLF_leftE=slfl,width_sign_area=wsa,
                                        height_sign_area=hsa)

            cld.save()
            return redirect('/')
        return render(request,'ledger_chequed.html',{'tally':tally})
    return redirect('/')

def ledger_bd(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        bn = bank_name.objects.all()
        
        return render(request,'ledger_bd.html',{'bn' : bn,'tally':tally})
    return redirect(' ledger_bd')

def create_ledger_bankdetails(request):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
    #     tally = Companies.objects.filter(id=t_id)
    #     if request.method=='POST':
    #         transaction_type=request.POST['transaction_type']
    #         acp=request.POST['ac_payee']
    #         acc_no=request.POST['acc_no']
    #         ifsc_code=request.POST['ifsc_code']
    #         bank_name=request.POST['bank_name']
    #         lbd=ledger_bankdetails(transaction_type=transaction_type,
    #                         cross_using = acp,
    #                         acc_no = acc_no,      
    #                         ifsc_code = ifsc_code,      
    #                         bank_name =bank_name)      
    #         lbd.save() 
    #         print("Added")
    #         return redirect('ledger_bd')
    #     return render(request,'ledger_bd.html',{'tally':tally})
    return redirect('/')

def b_name(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request,'bankname.html',{'tally':tally})
    return redirect('/')

def bankname(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            bn = request.POST['bank_name']
            bnn=bank_name(bankname = bn)
            bnn.save()
            return redirect('bankname')
        return render(request,'bankname.html',{'tally':tally})
    return redirect('/')

def ledger_chequebk(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'ledger_chequebk.html',{'tally':tally})
    return redirect('/')

def create_ledger_chequebk(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            fn=request.POST['from_number']
            tn=request.POST['to_number']
            nc=request.POST['number_cheques']
            nmc=request.POST['name_chequebk']
            lcb=ledger_chequebook(from_number=fn,
                                to_number = tn,
                                no_of_cheques = nc,
                                cheque_bookname = nmc)      
            lcb.save() 
            print("Added")
            return redirect('ledger_chequebk')
        return render(request,'ledger_chequebk.html',{'tally':tally})
    return redirect('/')

def ledger_gst(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'ledger_gst.html',{'tally':tally})
    return redirect('/')

def create_ledger_gst(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            ntrot=request.POST['nature_of_transaction']
            txbl=request.POST['taxable']
            txblty=request.POST['taxability']
            aplifm=request.POST['appicable_from']
            inttx=request.POST['integrated_tax']
            ces=request.POST['cess']
            lgst=ledger_gstvalues(nature_of_transaction=ntrot,
                            taxable = txbl,
                            taxability = txblty,
                            appicable_from = aplifm,
                            integrated_tax = inttx,
                            cess = ces)    
            lgst.save()  
            print("Added")
            return redirect('ledger_gst')
        return render(request,'ledger_gst.html',{'tally':tally})
    return redirect('/')

def ledger_taxgst(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'ledger_taxgst.html',{'tally':tally})
    return redirect('/')

def create_ledger_taxgst(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            regtp=request.POST['registration_type']
            assester=request.POST['assessee_teritory']
            comop=request.POST['commerce_operator']
            partde=request.POST['party_deemed']
            partytyp=request.POST['party_type']
            gstinuin=request.POST['gstin_uin']
            transp=request.POST['transporter']
            transpid=request.POST['transporter_id']

            lgt=ledger_taxreggst(registration_type=regtp,
                            assessee_teritory = assester,
                            commerce_operator = comop,
                            party_deemed = partde,
                            party_type = partytyp,
                            gstin_uin = gstinuin,
                            transporter = transp,
                            transporter_id = transpid)    
            lgt.save()  
            print("Added")
            return redirect('ledger_taxgst')
        return render(request,'ledger_taxgst.html',{'tally':tally})
    return redirect('/')

def create_gst(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		st = request.POST['state']
		rt = request.POST['registration_type']
		at = request.POST['assessee_territory']
		gsta = request.POST['gst_applicable']
		gstuin = request.POST['gstin_uin']
		prd = request.POST['periodicity']

	# .................regular.................

		kfca = request.POST['kerala_fca']
		af = request.POST['applicable_from']
		gstrd = request.POST['gst_rate_details']
		tla = request.POST['tl_advanceR']
		tlr = request.POST['tl_reverseC']
		gstc = request.POST['gst_classification'] 
		lb = request.POST['lut_bond']

    # ................composition................  
	  
		tr = request.POST['tax_rate']
		tc = request.POST['tax_calculation']
		tp = request.POST['tax_purchase']

	# ............e-Way bill applicable...........

		ea = request.POST['e_waybillA']
		aaf = request.POST['applicable_f']
		tli = request.POST['thresholdlimit_include']
		tl = request.POST['threshold_limit']
		intr = request.POST['intrastate']
		itl = request.POST['ithreshold_limit']
		pnw = request.POST['print_eway']

	# .............e-Invoice applicable..............

		einva = request.POST['e_invoiceA']
		appf = request.POST['app_f']
		bfp = request.POST['billfrom_place']
		peir = request.POST['period_einvoiceR']
		sewdei = request.POST['send_eW_details_einvoice']
        
		gstd=GST(state=st,
						reg_type=rt,
						assessee=at,
						gst_applicable=gsta,
						gstin=gstuin,
						periodicity=prd,
					# ........regular.......
						flood_cess=kfca,
						applicable_from=af,
						gst_rate_details=gstrd,
						advance_receipts=tla,
						reverse_charge=tlr,
						gst_classification=gstc,
						bond_details=lb,	
					# ........composition.......
						tax_rate=tr,		
						tax_calc=tc,		
						tax_purchase=tp,
					# ........e-Way bill applicable.......
						eway_bill=ea,
						applicable_form=aaf,
						threshold_includes=tli,
						threshold_limit=tl,
						intrastate=intr,
						threshold_limit2=itl,
						print_eway=pnw,
					# ........e-Invoice applicable.......
						e_invoice=einva,
						app_from=appf,
						billfrom_place=bfp,
						dperiod=peir,
						send_ewaybill=sewdei,
						company=id)
		gstd.save()
		print("Added")
		return redirect('/')
	return render(request,'gst.html')

def create_gsttax(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		txb=request.POST['taxability']
		af=request.POST['appicable_from']
		it=request.POST['integrated_tax']
		ces=request.POST['cess']
		fc=request.POST['flood_cess']
		
		cost=gst_taxability(taxability=txb,
                        applicable_dt = af,
                        integrated_tax = it,      
                        cess = ces,      
                        flood_cess = fc,
						company = id)          
		cost.save()
		print("Added")
		return redirect('/')
	return render(request,'gst_tax.html')

def create_lutbond(request,pk):
	if request.method=='POST':
		lbno=request.POST['lut_bondNo']
		afrom=request.POST['application_from']
		ato=request.POST['application_to']
		lb=gst_lutbond(lutbond=lbno,
                        validity_from = afrom,
                        validity_to = ato)      
		lb.save() 
		print("Added")
		return redirect('lut_bond')
	return render(request,'lut_bond')

def company_create(request):
	if request.method=="POST":
		name=request.POST['companyname']
		mname=request.POST['mailing_name']
		addr=request.POST['address']
		st=request.POST['state']
		cntry=request.POST['country']
		pncd=request.POST['pincode']
		tlphn=request.POST['telephone']
		mbl=request.POST['mobile']
		fax=request.POST['fax']
		email=request.POST['email']
		wbsit=request.POST['website']
		fin_begin=request.POST['fyear']
		bk_begin=request.POST['byear']
		crny_symbol=request.POST['currency']
		frml_name=request.POST['formal']

		ccmp=Companies.objects.filter(name=name)
		out=datetime.strptime (fin_begin,'%Y-%m-%d')+timedelta (days=364) 
		a=out.date()
		

		if ccmp:
			messages.info(request,'Company name already exists!!')
			return redirect('create_cmpny')
		else:
			cmp=Companies(name=name,mailing_name=mname,address=addr,state=st,country=cntry,
                pincode=pncd,telephone=tlphn,mobile=mbl,fax=fax,email=email,website=wbsit,fin_begin=fin_begin,
                books_begin=bk_begin,currency_symbol=crny_symbol,formal_name=frml_name,fin_end=a)
			cmp.save()
			messages.info(request,'Company created successfully(Enable the features as per your business needs)')
			return render(request,'features.html',{'cmp':cmp})

def company_feature(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=="POST":
            ma=request.POST['maintain_account']
            be=request.POST['billwise_entry']
            cc=request.POST['cost_centre']
            ic=request.POST['interest_calculation']
            mi=request.POST['maintain_inventry']
            ai=request.POST['account_inventry']
            mpl=request.POST['multiple_pricelevel']
            eb=request.POST['enable_batches']
            edt=request.POST['expiry_date']
            jop=request.POST['job_order_procress']
            ct=request.POST['cost_tracking']
            jc=request.POST['job_costing']
            dc=request.POST['discount_column']
            sa=request.POST['seperte_actual']
            gst=request.POST['gst']
            tds=request.POST['tds']
            tcs=request.POST['tcs']
            vat=request.POST['vat']
            excise=request.POST['excise']
            st=request.POST['service_tax']
            prl=request.POST['payroll']
            maddr=request.POST['multiple_address']
            mark_mod=request.POST['mark_modified']

            cmp_fet=Features(maintain_accounts=ma,bill_wise_entry=be,cost_centres=cc,interest_calc=ic,maintain_inventory=mi,
            integrate_accounts=ai,multiple_price_level=mpl,batches=eb,expirydate_batches=edt,joborder_processing=jop,cost_tracking=ct,job_costing=jc,discount_invoices=dc,
            Billed_Quantity=sa,gst=gst,tds=tds,tcs=tcs,vat=vat,excise=excise,servicetax=st,payroll=prl,multiple_addrss=maddr,
            vouchers=mark_mod,company=id)

            cmp_fet.save()
            return redirect('features')
        return render(request,'features.html',{'tally':tally})
    return redirect('/')

#......................Ajmy........................


def index(request):
    return render(request, 'home.html')

def group(request):
    return render(request, 'group.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')

def groupsummarypage(request):
    gps=CreateStockGrp.objects.all()
    con={
        'gps':gps,
        } 
    return render(request,'groupsummarypage.html',con)

# def catgroupsummary(request):
#     cat=CreateStockCateg.objects.all()
#     con={
#         'cat':cat,
#         } 
#     return render(request,'catgroupsummary.html',con)

def creategroups(request):
    gps=StockGroup.objects.all()
    con={
        'gps':gps,
        } 
    return render(request, 'creategroup.html',con)   

# def createcategory(request):
#     cat=Stockcategory.objects.all()
#     con={
#         'cat':cat,
#         } 
#     return render(request, 'createcategory.html',con) 

def savestockgroup(request):
    if request.method=='POST':
        gpname=request.POST['name']
        s=StockGroup(grp_name=gpname)
        s.save()
        abr=request.POST['alias']
        grp=request.POST.get('u')
        gp=StockGroup.objects.get(grp_name=grp)
        q=request.POST.get('qty')
        sg=CreateStockGrp(name=gpname,alias=abr,quantities=q,under=grp,group=gp)
        sg.save()
        return redirect('groupsummarypage')

# def savestockcategory(request):
#     if request.method=='POST':
#         catname=request.POST['name']
#         s=Stockcategory(cat_name=catname)
#         s.save()
#         abr=request.POST['alias']
#         cat=request.POST.get('u')
#         c=Stockcategory.objects.get(cat_name=cat)
#         q=request.POST.get('qty')
#         sc=CreateStockCateg(name=catname,alias=abr,quantities=q,under=cat,category=c)
#         sc.save()
#         return redirect('catgroupsummary')

def primarygrpsummary(request,sk):
    cmp=company.objects.get(id='1')
    gps=CreateStockGrp.objects.filter(group_id=sk)
    gt=0
    for g in gps:
        gg=StockGroup.objects.get(grp_name=g.name)
        gpsi= CreateStockGrp.objects.filter(group_id=gg.id)
        l=[]
        i=0
        h=0
        for gi in gpsi:
           gg=StockGroup.objects.get(grp_name=gi.name)
           si=stock_item.objects.filter(group_id=gg.id)
           ttpq=0
           ttsq=0
           r=0
           a=0
           y=0
      
           for s in si:
               w=s.rateper 
               oqty=s.quantity
               val=s.value
               tpq=voucherlist.objects.filter(item_id=s.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
               tpq=tpq+oqty
               ttpq=tpq+ttpq
               tsq=voucherlist.objects.filter(item_id=s.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
               ttsq=tsq+ttsq
               ttq=tpq-tsq
               s.qy=ttq
               s.value=ttq * w
               a=a+s.value
               y=y+w
           gi.q=ttpq-ttsq 
           gi.i=a
           h=h+gi.i
           gi.y=y
           i=i+1 
           gi.h=h   
           g.h=h
        gt=gt+g.h   
            



    con={
        'gpsi':gpsi,
        'gps':gps,
        'sk':sk,
        'gt':gt,
        'cmp':cmp
        } 
    return render(request, 'primarygrpsummary.html',con)  

def primarycatsummary(request,sk):
    cmp=company.objects.get(id='1')
    cat=CreateStockCateg.objects.filter(category_id=sk)
    gt=0
    for c in cat:
        cc=Stockcategory.objects.get(cat_name=c.name)
        cgsi= CreateStockCateg.objects.filter(category_id=cc.id)
        l=[]
        i=0
        h=0
        for ci in cgsi:
           cc=Stockcategory.objects.get(cat_name=ci.name)
           si=stock_item.objects.filter(category_id=cc.id)
           ttpq=0
           ttsq=0
           r=0
           a=0
           y=0
      
           for s in si:
               w=s.rateper 
               oqty=s.quantity
               val=s.value
               tpq=voucherlist.objects.filter(item_id=s.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
               tpq=tpq+oqty
               ttpq=tpq+ttpq
               tsq=voucherlist.objects.filter(item_id=s.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
               ttsq=tsq+ttsq
               ttq=tpq-tsq
               s.qy=ttq
               s.value=ttq * w
               a=a+s.value
               y=y+w
           ci.q=ttpq-ttsq 
           ci.i=a
           h=h+ci.i
           ci.y=y
           i=i+1 
           ci.h=h   
           c.h=h
        gt=gt+c.h   
            



    con={
        'cgsi':cgsi,
        'cat':cat,
        'sk':sk,
        'gt':gt,
        'cmp':cmp
        } 
    return render(request, 'primarycatsummary.html',con)

def secondarygrpsummary(request,sk):
    cmp=company.objects.get(id='1')
    gps=CreateStockGrp.objects.get(id=sk)
    gg=StockGroup.objects.get(grp_name=gps.name)
    gps= CreateStockGrp.objects.filter(group_id=gg.id)
    l=[]
    i=0
    h=0
    for g in gps:
      gg=StockGroup.objects.get(grp_name=g.name)
      si=stock_item.objects.filter(group_id=gg.id)
      ttpq=0
      ttsq=0
      r=0
      a=0
      y=0
      
      for s in si:
            w=s.rateper 
            oqty=s.quantity
            val=s.value
            tpq=voucherlist.objects.filter(item_id=s.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            tpq=tpq+oqty
            ttpq=tpq+ttpq
            tsq=voucherlist.objects.filter(item_id=s.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            ttsq=tsq+ttsq
            ttq=tpq-tsq
            s.qy=ttq
            s.value=ttq * w
            a=a+s.value
            y=y+w
      g.q=ttpq-ttsq 
      g.i=a
      h=h+g.i
      g.y=y
      i=i+1 
    con={
        'gps':gps,'a':a,'y':y,'gps':gps,'l':l,'h':h,'cmp':cmp
        } 
    return render(request, 'secondarygrpsummary.html',con) 

def secondarycatsummary(request,sk):
    cat=CreateStockCateg.objects.get(id=sk)
    cmp=company.objects.get(id='1')
    cc=Stockcategory.objects.get(cat_name=cat.name)
    cat= CreateStockCateg.objects.filter(category_id=cc.id)
    l=[]
    i=0
    h=0
    for c in cat:
      cc=Stockcategory.objects.get(cat_name=c.name)
      si=stock_item.objects.filter(category_id=cc.id)
      ttpq=0
      ttsq=0
      r=0
      a=0
      y=0
      
      for s in si:
            w=s.rateper 
            oqty=s.quantity
            val=s.value
            tpq=voucherlist.objects.filter(item_id=s.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            tpq=tpq+oqty
            ttpq=tpq+ttpq
            tsq=voucherlist.objects.filter(item_id=s.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            ttsq=tsq+ttsq
            ttq=tpq-tsq
            s.qy=ttq
            s.value=ttq * w
            a=a+s.value
            y=y+w
      c.q=ttpq-ttsq 
      c.i=a
      h=h+c.i
      c.y=y
      i=i+1 
    con={
        'cat':cat,'a':a,'y':y,'l':l,'h':h,'cmp':cmp
        } 
    return render(request, 'secondarycatsummary.html',con) 


def productsummary(request,sk):
    gps=CreateStockGrp.objects.get(id=sk)
    cmp=company.objects.get(id='1')
    gg=StockGroup.objects.get(grp_name=gps.name)
    si=stock_item.objects.filter(group_id=gg.id)
    ttpq=0
    ttsq=0
    r=0
    a=0
    y=0
    for s in si:
        w=s.rateper
        qty=s.quantity
        val=s.value
        tpq=voucherlist.objects.filter(item_id=s.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        tpq=tpq+qty
        ttpq=tpq+ttpq
        tsq=voucherlist.objects.filter(item_id=s.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        ttsq=tsq+ttsq
        ttq=tpq-tsq
        s.qy=ttq
        s.value=ttq * w
        a=a+s.value
        y=y+w
    
    
    q=ttpq-ttsq   
    con={
        'si':si,'ttpq':ttpq,'q':q,'ttpq':ttq,'w':w,'a':a,'y':y,'cmp':cmp
        } 
    return render(request, 'productsummary.html',con)


def prcatsummary(request,sk):
    cmp=company.objects.get(id='1')
    cat=CreateStockCateg.objects.get(id=sk)
    cc=Stockcategory.objects.get(cat_name=cat.name)
    si=stock_item.objects.filter(category_id=cc.id)
    ttpq=0
    ttsq=0
    r=0
    a=0
    y=0
    for s in si:
        w=s.rateper
        qty=s.quantity
        val=s.value
        tpq=voucherlist.objects.filter(item_id=s.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        tpq=tpq+qty
        ttpq=tpq+ttpq
        tsq=voucherlist.objects.filter(item_id=s.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        ttsq=tsq+ttsq
        ttq=tpq-tsq
        s.qy=ttq
        s.value=ttq * w
        a=a+s.value
        y=y+w
    
    
    q=ttpq-ttsq   
    con={
        'si':si,'ttpq':ttpq,'q':q,'ttpq':ttq,'w':w,'a':a,'y':y,'cmp':cmp
        } 
    return render(request, 'productcatsummary.html',con) 


def prdctmonthlysummary(request,sk):
    cmp=company.objects.get(id='1')
    si=stock_item.objects.get(id=sk)
    rate=si.rateper
    qty=si.quantity
    val=si.value
    tpq=voucherlist.objects.filter(item_id=si.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    tpqo=tpq+qty
    tpv=voucherlist.objects.filter(item_id=si.id,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    
    tsq=voucherlist.objects.filter(item_id=si.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    tsv=voucherlist.objects.filter(item_id=si.id,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ttq=tpqo-tsq
    rate=si.rateper
    qty=si.quantity
    val=si.value
    
    a=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    b=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    c=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    d=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ia=a
    ib=b
    oc=c
    od=d
    a=a+qty
    b=b+val
    aa=a-c
    

    e=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    f=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    g=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    h=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ie=e
    iv=f
    og=g
    oh=h
    cc=e-g
    cb5=aa+cc
    

    i=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    j=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    k=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    l=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    iiq=i
    ij=j
    okq=k
    ol=l
    ee=i-k
    cb6=cb5+ee
     
    
    m=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    n=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    o=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    p=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    im=m
    inv=n
    ooq=o
    op=p
    gg=m-o
    cb7=cb6+gg

    q=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    r=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    s=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    t=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    iq=q
    ir=r
    os=s
    ot=t
    ii=q-s
    cb8=cb7+ii

    u=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    v=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    w=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    x=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    iu=u
    ivv=v
    ow=w
    ox=x
    kk=u-w
    cb9=cb8+kk
    
    y=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    z=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    a1=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    b1=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    iy=y
    iz=z
    oa1=a1
    ob1=b1 
    mm=y-a1
    cb10=cb9+mm

    c1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    d1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    e1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    f1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ic1=c1
    id1=d1
    oe1=e1
    of1=f1
    oo=c1-e1
    cb11=cb10+oo

    g1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    h1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    i1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    j1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ig1=g1
    ih1=h1
    oi1=i1
    oj1=j1
    qq=g1-i1
    cb12=cb11+qq

    k1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    l1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    m1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    n1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ik1=k1
    il1=l1
    om1=m1
    on1=n1
    ss=k1-m1
    cb1=cb12+ss

    o1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    p1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    q1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    r1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    io1=o1
    ip1=p1
    oq1=q1
    or1=r1
    uu=o1-q1
    cb2=cb1+uu

    s1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    t1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    u1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    v1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']                            
    is1=s1
    it1=t1
    ou1=u1
    ov1=v1
    ww=s1-u1
    cb3=cb2+ww
    
    
    
    
    
    
    
    
    con={
        'si':si,'cmp':cmp,
        'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,'y':y,'z':z ,'a1':a1,
        'b1':b1,'c1':c1,'d1':d1,'e1':e1,'f1':f1,'g1':g1,'h1':h1,'i1':i1,'j1':j1,'k1':k1,'l1':l1,'m1':m1,'n1':n1,'o1':o1,'p1':p1,'q1':q1,'r1':r1,'s1':s1,'t1':t1,'u1':u1,'v1':v1,
        
        'ia':ia,'ib':ib,'oc':oc,'od':od,'ie':ie,'iv':iv,'og':og,'oh':oh,'iiq':iiq,'ij':ij,'okq':okq,'ol':ol,'im':im,'inv':inv,'ooq':ooq,'op':op,'iq':iq,'ir':ir,'os':os,'ot':ot,'iu':iu,'ivv':ivv,'ow':ow,'ox':ox,'iy':iy,'iz':iz ,'oa1':oa1,
        'ob1':ob1,'ic1':ic1,'id1':id1,'oe1':oe1,'of1':of1,'ig1':ig1,'ih1':ih1,'oi1':oi1,'oj1':oj1,'ik1':ik1,'il1':il1,'om1':om1,'on1':on1,'io1':io1,'ip1':ip1,'oq1':oq1,'or1':or1,'is1':is1,'it1':it1,'ou1':ou1,'ov1':ov1,
        
        'aa':aa,'cc':cc,'ee':ee,'gg':gg,'ii':ii,'kk':kk,'mm':mm,'oo':oo,'qq':qq,'ss':ss,'uu':uu,'ww':ww,
        'tpq':tpq,'tsq':tsq,'tpv':tpv,'tsv':tsv,'ttq':ttq,'rate':rate
        ,'qty':qty,'val':val,'cb5':cb5,'cb6':cb6,'cb7':cb7,'cb8':cb8,'cb9':cb9,'cb10':cb10,'cb11':cb11,'cb12':cb12,'cb1':cb1,'cb2':cb2,'cb3':cb3,}
    return render(request, 'prdctmonthlysummary.html',con)


def productcatmonthlysummary(request,sk):
    si=stock_item.objects.get(id=sk)
    rate=si.rateper
    qty=si.quantity
    val=si.value
    tpq=voucherlist.objects.filter(item_id=si.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    tpq=tpq+qty
    tpv=voucherlist.objects.filter(item_id=si.id,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    tpv=tpv+val
    tsq=voucherlist.objects.filter(item_id=si.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    tsv=voucherlist.objects.filter(item_id=si.id,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ttq=tpq-tsq
    rate=si.rateper
    qty=si.quantity
    val=si.value
    
    a=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    b=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    c=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    d=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    a=a+qty
    b=b+val
    aa=a-c
    

    e=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    f=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    g=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    h=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    cc=e-g
    

    i=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    j=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    k=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    l=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ee=i-k
   
     
    
    m=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    n=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    o=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    p=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    gg=m-o
    

    q=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    r=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    s=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    t=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ii=q-s
    
    u=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    v=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    w=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    x=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    kk=u-w
    
    y=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    z=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    a1=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    b1=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    mm=y-a1
    
    c1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    d1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    e1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    f1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    oo=c1-e1
    
    g1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    h1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    i1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    j1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    qq=g1-i1
    
    k1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    l1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    m1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    n1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ss=k1-m1
    
    o1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    p1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    q1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    r1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    uu=o1-q1
    
    s1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    t1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    u1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    v1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']                            
    ww=s1-u1
    
    
    
    
    
    
    
    
    
    con={
        'si':si,
        'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,'y':y,'z':z ,'a1':a1,
        'b1':b1,'c1':c1,'d1':d1,'e1':e1,'f1':f1,'g1':g1,'h1':h1,'i1':i1,'j1':j1,'k1':k1,'l1':l1,'m1':m1,'n1':n1,'o1':o1,'p1':p1,'q1':q1,'r1':r1,'s1':s1,'t1':t1,'u1':u1,'v1':v1
        
        ,'aa':aa,'cc':cc,'ee':ee,'gg':gg,'ii':ii,'kk':kk,'mm':mm,'oo':oo,'qq':qq,'ss':ss,'uu':uu,'ww':ww,
        'tpq':tpq,'tsq':tsq,'tpv':tpv,'tsv':tsv,'ttq':ttq,'rate':rate
        ,'qty':qty,'val':val,}
    return render(request, 'prdctmonthlysummary.html',con)


def vouchsummary(request,sk,m,n):
    cmp=company.objects.get(id='1')
    si=stock_item.objects.get(id=sk)
    rate=si.rateper
    
    
    if m==4:
        qty=si.quantity
        val=si.value
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte='2022-04-30')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        a=a+qty
        b=b+val
        e=a-c
        f=rate
        tq=e
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==5:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==6:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        a=a
        b=b
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==7:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==8:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==9:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==10:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==11:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==12:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==1:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==2:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==3:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
                                   
    
    con={
        'v':v,
        'si':si,
        'm':m,
        'a':a,
        'b':b,
        'c':c,
        'd':d,
        'e':e,
        'f':f,
        'qty':qty,
        'val':val,
        'fr':fr ,'tq':tq ,'n':n,
        'si':si,'cmp':cmp  
        }
    return render(request, 'vouchersummary.html',con)


def periodvouchsummary(request,sk,m,n):
    cmp=company.objects.get(id='1')
    si=stock_item.objects.get(id=sk)
    rate=si.rateper
    st=request.POST.get('start')
    et=request.POST.get('end')
    
    if m==4:
        qty=si.quantity
        val=si.value
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        a=a+qty
        b=b+val
        e=a-c
        f=rate
        tq=e
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==5:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==6:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        a=a
        b=b
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==7:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==8:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==9:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==10:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==11:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==12:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==1:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==2:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==3:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
                                   
    
    con={
        'v':v,
        'si':si,
        'm':m,
        'a':a,
        'b':b,
        'c':c,
        'd':d,
        'e':e,
        'f':f,
        'qty':qty,
        'val':val,
        'fr':fr ,'tq':tq ,'n':n,
        'si':si,'cmp':cmp  
        }
    return render(request, 'periodvouchersummary.html',con)


def categorysummary(request):
    return render(request, 'categorysummary.html')


def primarycategory(request):
    return render(request, 'primarycategory.html')

def categorysummarypage(request):
    return render(request, 'categorysummarypage.html')

def secondarycategory(request):
    return render(request, 'secondarycategorypage.html')

def productcategory(request):
    return render(request, 'productcategory.html')


#......................Praveen........................

def list_of_ledger(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        led=tally_ledger.objects.filter(status=0)
        led1=tally_ledger.objects.filter(company_id=t_id)
        context={'led':led,'led1':led1}
        return render(request,'list_of_ledger.html',context)
    return redirect('/')

def list_of_groups(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        grup=tally_group.objects.filter(status=0)
        grup1=tally_group.objects.filter(company_id=t_id)

        context={'grup':grup,'tally':tally,'grup1':grup1}
        return render(request,'list_of_groups.html',context)
    return redirect('/')


def list_of_voucher_type(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        vou=Voucher.objects.filter(status=0)
        vou1=Voucher.objects.filter(company_id=t_id)
        context={'vou':vou,'vou1':vou1}
        return render(request,'list_of_voucher_type.html',context)
    return redirect('/')

def list_of_currency(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        curr=currencyAlteration.objects.filter(status=0)
        curr1=currencyAlteration.objects.filter(company_id=t_id)
        context={'curr':curr,'tally':tally,'curr1':curr1}

        return render(request,'list_of_currency.html',context)
    return redirect('/')

def companyCreate1(request):
    return render(request,'create_companys.html')

def create_company(request):
    if request.method=='POST':
        dp=request.POST.get('dpath')
        cn=request.POST.get('name')
        mn=request.POST.get('mailing_name')
        ca=request.POST.get('address1')
        cs=request.POST.get('state')
        cc=request.POST.get('country')
        pin=request.POST.get('pincode')
        tel=request.POST.get('telephone')
        mob=request.POST.get('mobile')
        fax=request.POST.get('fax')
        email=request.POST.get('email')
        web=request.POST.get('website')
        fy=request.POST.get('fin_begin')
        bks=request.POST.get('books_begin')
        bc=request.POST.get('currency_symbol')
        fr=request.POST.get('formal_name')
        cmp=Companies.objects.filter(name=cn)
        out=datetime.strptime (fy,'%Y-%m-%d')+timedelta (days=364) 
        print(out)
        a=out.date()
        print(a)
        if cmp:
            messages.info(request,'Company name already exists!!')
        else:
            com=Companies(d_path=dp,
                                name=cn,
                                mailing_name=mn,
                                address=ca,
                                state=cs,
                                country=cc,
                                pincode=pin,
                                telephone=tel,
                                mobile=mob,
                                fax=fax,
                                email=email,
                                website=web,
                                fin_begin=fy,
                                books_begin=bks,
                                currency_symbol=bc,
                                formal_name=fr,
                                fin_end=a,)
            com.save()
            
                        
            return render(request,'company_feature_form.html',{'com':com})
    return render(request,'create_companys.html')

def companies_feature(request):
    return render(request,'company_feature_form.html')

def list_of_companies(request):
    return render(request,'list_of_companies.html')

def select_company1(request):
    comp=Companies.objects.all()
    
    return render(request,'select_company.html',{'comp1':comp})

def shut_company1(request):
	com=Companies.objects.all() 
	return render(request, 'shut_company.html',{'com':com})

def shut2(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=False
    c.save()
    return redirect('shut_company') 

def enable2(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=True
    c.save()
    return redirect('shut_company')

def list_of_cost_centers(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        cst=cost_centre.objects.filter(company_id=t_id)

    return render(request,'list_of_cost_centers.html',{'cst':cst,'tally':tally})
# def shut_card(request):
#     return render(request,'shut_card.html')

def load_ledger_alter1(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        led = tally_ledger.objects.get(id=pk)
        lga = tally_group.objects.filter(id=t_id)
        if request.method=='POST':
            led.name=request.POST.get('name')
            led.alias=request.POST.get('alias')
            led.under=request.POST.get('under')
            led.mname=request.POST.get('mailingname')
            led.address=request.POST.get('address')
            led.state=request.POST.get('state')
            led.country=request.POST.get('country')
            led.pincode=request.POST.get('pincode')
            led.pan_no=request.POST.get('pan_no')
            led.bank_details=request.POST.get('bank_details')
            led.registration_type=request.POST.get('registration_type')
            led.gst_uin=request.POST.get('gst_uin')
            led.opening_blnc=request.POST.get('opening_blnc')

            led.set_odl=request.POST.get('set_odl')
            led.aac_holder_nm=request.POST.get('ac_holder_nm')
            led.acc_no=request.POST.get('acc_no')
            led.ifsc_code=request.POST.get('ifsc_code')
            led.swift_code=request.POST.get('swift_code')
            led.bank_name=request.POST.get('bank_name')
            led.branch=request.POST.get('branch')
            led.SA_cheque_bk=request.POST.get('SA_cheque_bk')
            led.Echeque_p=request.POST.get('Echeque_p')
            led.SA_chequeP_con=request.POST.get('SA_chequeP_con')

            led.type_of_ledger=request.POST.get('type_of_ledger')
            led.rounding_method=request.POST.get('rounding_method')
            led.rounding_limit=request.POST.get('rounding_limit')
            led.type_duty_tax=request.POST.get('type_duty_tax')
            led.tax_type=request.POST.get('tax_type')
            led.rate_per_unit=request.POST.get('rate_per_unit')
            led.percentage_of_calcution=request.POST.get('percentage_of_calcution')
            led.rond_method=request.POST.get('rond_method')
            led.rond_limit=request.POST.get('rond_limit')
            led.gst_applicable=request.POST.get('gst_applicable')
            led.setalter_gstdetails=request.POST.get('setalter_gstdetails')
            led.type_of_supply=request.POST.get('type_of_supply')
            led.assessable_value=request.POST.get('assessable_value')
            led.appropriate_to=request.POST.get('appropriate_to')
            led.method_of_calculation=request.POST.get('method_of_calculation')
            led.balance_billbybill=request.POST.get('balance_billbybill')
            led.credit_period =request.POST.get('credit_period')
            led.creditdays_voucher=request.POST.get('creditdays_voucher')

            
            led.company_id=t_id
            led.save()
            print("added")
            return redirect('list_of_ledger')
        return render(request,'load_ledger_alter.html',{'i':led,'lga':lga,'tally':tally})
    return redirect('/')
    

def load_ledger_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        led = tally_ledger.objects.get(id=pk)
        lga = tally_group.objects.filter(id=t_id)
        if request.method=='POST':
            led.name=request.POST.get('name')
            led.alias=request.POST.get('alias')
            led.under=request.POST.get('under')
            led.mname=request.POST.get('mailingname')
            led.address=request.POST.get('address')
            led.state=request.POST.get('state')
            led.country=request.POST.get('country')
            led.pincode=request.POST.get('pincode')
            led.pan_no=request.POST.get('pan_no')
            led.bank_details=request.POST.get('bank_details')
            led.registration_type=request.POST.get('registration_type')
            led.gst_uin=request.POST.get('gst_uin')
            led.opening_blnc=request.POST.get('opening_blnc')

            led.set_odl=request.POST.get('set_odl')
            led.aac_holder_nm=request.POST.get('ac_holder_nm')
            led.acc_no=request.POST.get('acc_no')
            led.ifsc_code=request.POST.get('ifsc_code')
            led.swift_code=request.POST.get('swift_code')
            led.bank_name=request.POST.get('bank_name')
            led.branch=request.POST.get('branch')
            led.SA_cheque_bk=request.POST.get('SA_cheque_bk')
            led.Echeque_p=request.POST.get('Echeque_p')
            led.SA_chequeP_con=request.POST.get('SA_chequeP_con')

            led.type_of_ledger=request.POST.get('type_of_ledger')
            led.rounding_method=request.POST.get('rounding_method')
            led.rounding_limit=request.POST.get('rounding_limit')
            led.type_duty_tax=request.POST.get('type_duty_tax')
            led.tax_type=request.POST.get('tax_type')
            led.rate_per_unit=request.POST.get('rate_per_unit')
            led.percentage_of_calcution=request.POST.get('percentage_of_calcution')
            led.rond_method=request.POST.get('rond_method')
            led.rond_limit=request.POST.get('rond_limit')
            led.gst_applicable=request.POST.get('gst_applicable')
            led.setalter_gstdetails=request.POST.get('setalter_gstdetails')
            led.type_of_supply=request.POST.get('type_of_supply')
            led.assessable_value=request.POST.get('assessable_value')
            led.appropriate_to=request.POST.get('appropriate_to')
            led.method_of_calculation=request.POST.get('method_of_calculation')
            led.balance_billbybill=request.POST.get('balance_billbybill')
            led.credit_period =request.POST.get('credit_period')
            led.creditdays_voucher=request.POST.get('creditdays_voucher')

            
            
            led.save()
            print("added")
            return redirect('list_of_ledger')
        return render(request,'load_ledger_alter.html',{'i':led,'lga':lga,'tally':tally})
    return redirect('/')
    


def load_create_ledger(request):
    lg=tally_group.objects.all()
    if request.method=='POST':
        nm=request.POST.get('name')
        als=request.POST.get('alias')
        under=request.POST.get('under')
        mname=request.POST.get('mailingname')
        adr=request.POST.get('address')
        st=request.POST.get('state')
        cntry=request.POST.get('country')
        pin=request.POST.get('pincode')
        pno=request.POST.get('pan_no')
        bdetls=request.POST.get('bank_details')
        rtype=request.POST.get('registration_type')
        gst_uin=request.POST.get('gst_uin')
        opnbn=request.POST.get('opening_blnc')

        spdl=request.POST.get('set_odl')
        achnm=request.POST.get('ac_holder_nm')
        acno=request.POST.get('acc_no')
        ifsc=request.POST.get('ifsc_code')
        scode=request.POST.get('swift_code')
        bn=request.POST.get('bank_name')
        brnch=request.POST.get('branch')
        sacbk=request.POST.get('SA_cheque_bk')
        ecp=request.POST.get('Echeque_p')
        sacpc=request.POST.get('SA_chequeP_con')
        
        ldr=tally_ledger(name=nm,alias=als,under=under,mname=mname,address=adr,state=st,country=cntry,
						pincode=pin,pan_no=pno,bank_details=bdetls,registration_type=rtype,gst_uin=gst_uin,
						opening_blnc=opnbn,set_odl=spdl,ac_holder_nm=achnm,acc_no=acno,ifsc_code=ifsc,swift_code=scode,
						bank_name=bn,branch=brnch,SA_cheque_bk=sacbk,Echeque_p=ecp,SA_chequeP_con=sacpc)
		
        ldr.save()
    
    return render(request,'load_create_ledger.html',{'lg':lg})

def ledger_gst_details(request):
    return render(request,'ledger_gst_details.html')

def ledger_chequebooks(request):
    if request.method=='POST':
        cr=request.POST.get('ccon')
        fnum=request.POST.get('from_no')
        tnum=request.POST.get('to_no')
        nchq=request.POST.get('no_chq')
        nachq=request.POST.get('nm_chq')
        chqbk=ledger_chequebook(chq_range=cr,
                                from_num=fnum,
                                to_no=tnum,
                                no_chq=nchq,
                                nm_chq=nachq,
                
                                    )
        
        chqbk.save()
        print("added")
        return redirect('ledger_chequebook')
    return render(request,'ledger_cheque_book.html')

def ledger_bank_details(request):
    if request.method=='POST':
        bdt=request.POST['bankde']
        tt=request.POST['trans']
        cu=request.POST['cros']
        an=request.POST['acnt']
        ifs=request.POST['ifs']
        bn=request.POST['bank']
        bd=bank_details(bank_de=bdt,
                        trans_type=tt,
                        cros_using=cu,
                        acnt_no=an,
                        ifs=ifs,
                        bank_name=bn,)
        
        bd.save()
        print("added")
    return render(request,'ledger_bank_details.html')

def load_create_groups(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        grup=tally_group.objects.get(id=pk)
        if request.method=='POST':
            grup.group_name=request.POST['gname']
            grup.group_alias=request.POST['alias']
            grup.group_under=request.POST['group']
            grup.nature=request.POST['group_nature']
            grup.gross_profit=request.POST['gorss_profit']
            grup.sub_ledger=request.POST['ledger']
            grup.debit_credit=request.POST['debit/credit']
            grup.calculation=request.POST['calculation']
            grup.invoice=request.POST['invoice']
            grup.save()
            print("added")
        return render(request,'load_create_groups.html',{'i':grup,'tally':tally})
    return redirect('/')

def load_alter_groups(request):
    return render(request,'load_create_groups.html')

def load_create_ledger2(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            gname=request.POST['gname']
            galias=request.POST['alias']
            under=request.POST['group']
            nature=request.POST['group_nature']
            gross=request.POST['gorss_profit']
            ledg=request.POST['ledger']
            cred=request.POST['debit/credit']
            calc=request.POST['calculation']
            invc=request.POST['invoice']
            grp=tally_group(group_name=gname,
                    group_alias=galias,
                    group_under=under,
                    nature=nature,
                    gross_profit=gross,
                    sub_ledger=ledg,
                    debit_credit=cred,
                    calculation=calc,
                    invoice=invc,
                    company_id=t_id
                    )          
            grp.save()
            print("added")
            return redirect('base')
        return render(request,'load_create_ledger2.html',{'tally':tally})
    return redirect('/')


def load_voucher_type(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        vou=Voucher.objects.get(id=pk)
        if request.method=='POST':
            vou.voucher_name=request.POST['vname']
            vou.alias=request.POST['alias']
            vou.voucher_type=request.POST['vouch_type']
            vou.abbreviation=request.POST['Abbreviation']
            vou.voucherActivate=request.POST['activate_Vtype']

            vou.voucherNumber=request.POST['method_Vno']
            vou.preventDuplicate=request.POST['prevent']
            vou.advance_con=request.POST['advance_con'] 
            vou.voucherEffective=request.POST['use_EDV']
            vou.transaction=request.POST['zero_val']
            vou.make_optional=request.POST['mVoptional_defualt']

            vou.voucherNarration=request.POST['allow_nar']
            vou.provideNarration=request.POST['provide_L']
            vou.manu_jrnl=request.POST['manu_jrnl']
            vou.track_purchase=request.POST['track_purchase']
            vou.enable_acc=request.POST['enable_acc']
            vou.prnt_VA_save=request.POST['prnt_VA_save']

            vou.jurisdiction=request.POST['jurisdiction']
            vou.pos_invoice=request.POST['pos_invoice']
            vou.msg_1=request.POST['msg_1']
            vou.msg_2=request.POST['msg_2']
            vou.default_bank=request.POST['default_bank']
            vou.title_print=request.POST['title_print']
            vou.setAlter=request.POST['set_alter']
            vou.name_class=request.POST['name_class']
            vou.company_id=t_id
            
            
            vou.save()
            print("added")
            return redirect('base')
        return render(request,'load_voucher_type.html',{'i':vou})
    return redirect('/')

def voucher_type_alteration_secondary(request):
    return render(request,'voucher_type_alteration_secondary.html')

def load_create_voucher(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        vouchername=request.POST['vname']
        voucheralias=request.POST['valias']
        vouchertype=request.POST['vtype']
        abbreviation=request.POST['vabbre']
        vactive=request.POST['vactive']
        vnumber=request.POST['vnum']
        vprevent=request.POST['vprev']
        vadvcon=request.POST['advcon'] 
        veffective=request.POST['effct']
        vtrans=request.POST['trans']
        voptional=request.POST['opt']
        vnarration=request.POST['narrate']
        vprovide=request.POST['provide']
        vjournal=request.POST['journal']
        vpurchase=request.POST['purchase']
        vallocate=request.POST['allocate']
        vprint=request.POST['vprint']
        vjuri=request.POST['juri']
        vpos=request.POST['pos']
        vmsg1=request.POST['msg1']
        vmsg2=request.POST['msg2']
        vbank=request.POST['vbank']
        vtitle=request.POST['vtitle']
        vsetalt=request.POST['vsetalt']
        
        
        vouch=Voucher(voucher_name=vouchername,
                              alias=voucheralias,
                              voucher_type=vouchertype,
                              abbreviation=abbreviation,
                              voucherActivate=vactive,
                              voucherNumber=vnumber,
                              preventDuplicate=vprevent,
                              advance_con=vadvcon,
                              voucherEffective=veffective,
                              transaction=vtrans,
                              make_optional=voptional,
                              voucherNarration=vnarration,
                              provideNarration=vprovide,
                              journal=vjournal,
                              purchase= vpurchase,
                              allocation=vallocate,
                              printVoucher=vprint,
                              jurisdiction=vjuri,
                              POSInvoice=vpos,
                              message1=vmsg1,
                              message2=vmsg2,
                              defaultBank=vbank,
                              titlePrint=vtitle,
                              setAlter=vsetalt,
                             )
        vouch.save()
        print("added")
        return redirect('/')
    return render(request,'load_create_voucher.html',{'tally':tally})

def load_currency(request):
    return render(request,'load_currency.html')

def company_feature_form(request,pk):
    id=Companies.objects.get(id=pk)
    print(id)

    if request.method=='POST':
        coname=request.POST['name']
        ma=request.POST['main']
        bw=request.POST['bill']
        ecc=request.POST['cost']
        eic=request.POST['inter']
        mi=request.POST['inven']
        iawi=request.POST['intac']
        empl=request.POST['mulpri']
        eb=request.POST['enbat']
        medb=request.POST['mained']
        ejop=request.POST['ejob']
        ect=request.POST['ecost']
        ejc=request.POST['ejoco']
        udci=request.POST['used']
        usa=request.POST['uact']
        gst=request.POST['gst']
        tds=request.POST['tds']
        tcs=request.POST['tcs']
        vat=request.POST['vat']
        enex=request.POST['exci']
        est=request.POST['extax']
        mp=request.POST['mai']
        # eps=request.POST['enpa']
        ema=request.POST['enad']
        mmv=request.POST['mark']
        fc=Features(co_name=coname,
                          maintain_acconts=ma,
                          bill_wise_entry=bw,
                          cost_centers=ecc,
                          interest_calc=eic,
                          maintain_inventory=mi,
                          integrate_accounts=iawi,
                          multiple_price_level=empl,
                          batches=eb,
                          expirydate_batches=medb,
                          joborder_processing=ejop,
                          cost_tracking=ect,
                          job_costing=ejc,
                          discount_invoices=udci,
                          Billed_Quantity=usa,
                          gst=gst,
                          tds=tds,
                          tcs=tcs,
                          vat=vat,
                          excise=enex,
                          servicetax=est,
                          payroll=mp,
                        #   enb_pay=eps,
                          multiple_addrss=ema,
                          vouchers=mmv,
                          company=id,)
        fc.save()
        print("added")
    return render(request,'company_feature_form.html',{'com':id})

def load_rates_of_exchange(request):
    curcc=currencyAlteration.objects.all()
    rat=rateofexchange.objects.all()
    if request.method=='POST':
        
        curncy=request.POST['curname']
        
        cstdrate=request.POST['stdr']
        csrate=request.POST['sr']
        bsrate=request.POST['sr2']
        raex=rateofexchange(
                          
                          stdrate=cstdrate,
                          sell_specified_rate=csrate,
                          buy_specified_rate=bsrate,
                          currencyName=curncy,)
        raex.save()
        print("added")
        return redirect('/')
    return render(request,'load_rates_of_exchange.html',{'curcc':curcc,'rat':rat})

def create_currency3(request):
    
    
    return render(request,'create_currency.html')

def load_cost_centers(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        cst=cost_centre.objects.get(id=pk)
        ccst=cost_centre.objects.filter(id=t_id)
        if request.method=='POST':
            cst.c_name=request.POST['cst_name']
            cst.cost_alias=request.POST['alias']
            cst.under=request.POST['c_under']
            cst.company_id=t_id
            cst.save()
            print("added")
        return render(request,'load_cost_centers.html',{'i':cst,'ccst':ccst,'tally':tally})
    return redirect('/')

def alter_cost_create(request):
    ccst=cost_center.objects.all()
    if request.method=='POST':
        c_name=request.POST['cname']
        calias=request.POST['calias']
        cunder=request.POST['cunder']
        cost=cost_center(c_name=c_name,
                cost_alias=calias,
                under=cunder,
                )
        cost.save()
        print("added")
        return redirect('alter_cost_create')
    return render(request,'alter_cost_create.html',{'ccst':ccst})

def load_alter_currency(request):
    if request.method=='POST':
        casymbol=request.POST['symbol']
        caname=request.POST['name']
        caiso=request.POST['iso']
        canumdec=request.POST['numdec']
        caamount=request.POST['amount']
        casuffix=request.POST['suffix']
        casymam=request.POST['symam']
        caamodec=request.POST['amodec']
        cadecwo=request.POST['decwo']
        ca=currencyAlteration(Symbol=casymbol,
                              FormalName=caname,
                              ISOCurrency=caiso,
                              DecimalPlace=canumdec,
                              showAmount=caamount,
                              suffixSymbol=casuffix,
                              AddSpace=casymam,
                              wordRep=caamodec,
                              DecimalWords=cadecwo)
        ca.save()
        print("hi")
        return redirect('list_of_currency')
    return render(request,'load_alter_currency.html')


def currency_alteraion(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        calt=currencyAlteration.objects.get(id=pk)
        if request.method=='POST':
            calt.Symbol=request.POST.get('symbol')
            calt.FormalName=request.POST.get('name')
            calt.ISOCurrency=request.POST.get('iso')
            calt.DecimalPlace=request.POST.get('numdec')
            calt.showAmount=request.POST.get('show_amt')
            calt.suffixSymbol=request.POST.get('suffix')
            calt.AddSpace=request.POST.get('add_space')
            calt.wordRep=request.POST.get('word_rep')
            calt.DecimalWords=request.POST.get('no_decimalo')
            

            stadate=request.POST.get('standate')
            starate=request.POST.get('stdrate')
            seldate=request.POST.get('selldate')
            selvrate=request.POST.get('selvrate')
            selrate=request.POST.get('selsrate')
            buydate=request.POST.get('buydate')
            buyvrate=request.POST.get('buyvrate')
            buyrate=request.POST.get('buysrate')

            al=Currency_alt(stddate=stadate,
                            stdrate=starate,
                            selldate=seldate,
                            selvorate=selvrate,
                            sellrate=selrate,
                            buydate=buydate,
                            buyvorate=buyvrate,
                            buyrate=buyrate,
                            currencyAlteration_id=pk,company_id=t_id)
        
            
            al.save()
            calt.save()
            print("added")
            return redirect('list_of_currency')
        return render(request,'currency_alteraion.html',{'i':calt})
    return redirect('/')


def gst_details3(request,pk):
    id=Companies.objects.get(id=pk)
    company=Companies.objects.get(id=pk)

    if request.method=='POST':
        cmp=request.POST.get('cmpname')
        state=request.POST.get('cstate')
        reg=request.POST.get('creg')
        gapp=request.POST.get('cgapp')
        uin=request.POST.get('cuin')
        peri=request.POST.get('cperi')
        fl=request.POST.get('cflood')
        apf=request.POST.get('capf')
        grate=request.POST.get('cgrate')
        adr=request.POST.get('cadr')
        rev=request.POST.get('crev')
        gclass=request.POST.get('cgclass')
        lut=request.POST.get('clut')
        tv=request.POST.get('ctv')
        tc=request.POST.get('ctc')
        tp=request.POST.get('ctp')
        eway=request.POST.get('ceway')
        appform=request.POST.get('cappform')
        liin=request.POST.get('cliin')
        thr=request.POST.get('cthr')
        intra=request.POST.get('cintra')
        thre=request.POST.get('cthre')
        ewayb=request.POST.get('cewayb')
        einv=request.POST.get('ceinv')
        appli=request.POST.get('cappli')
        billf=request.POST.get('cbillf')
        dper=request.POST.get('cdper')
        snd=request.POST.get('csnd')
        gd=GST(company_name=cmp,
              state=state,
              reg_type=reg,
              gst_applicable=gapp,
              gstin=uin,
              periodicity=peri,
              flood_cess=fl,
              applicable_form1=apf,
              gst_rate_details=grate,
              advance_receipts=adr,
              reverse_charge=rev,
              gst_classification=gclass,
              bond_details=lut,
              tax_rate=tv,
              tax_calc=tc,
              tax_purchase=tp,
              eway_bill=eway,
              applicable_form=appform,
              threshold_includes=liin,
              threshold_limit=thr,
              intrastate=intra,
              threshold_limit2=thre,
              print_eway=ewayb,
              e_invoice=einv,
              app_form=appli,
              billfrom_place=billf,
              dperiod=dper,
              send_ewaybill=snd,
              company=id,)
        gd.save()
        print("added")
    return render(request,'gst_details.html',{'id':id,'companies':company})

def lutbond(request,pk):
    id=Companies.objects.get(id=pk)
    if request.method=='POST':
        lbn=request.POST.get('lbn')
        afrom=request.POST['application_from']
        ato=request.POST['application_to']
        lb=gst_lutbond(lutbond=lbn,
                        validity_from = afrom,
                        validity_to = ato,
                        company=id,)
        lb.save()

    return render(request,'lutbond.html',{'id':id})

def gst_details_of_company(request):
    if request.method=='POST':

        ta=request.POST.get('gta')
        it=request.POST.get('git')
        ce=request.POST.get('gce')
        fc=request.POST.get('gfc')
        gdc=gst_taxability(Taxability=ta,
                            integrated_tax=it,
                            cess=ce,
                            flood_cess=fc,)
        gdc.save()
        return redirect('gst_details_of_company')
    return render(request,'gst_details_of_company.html')

def tds_detuctor(request,pk):
    id=Companies.objects.get(id=pk)

    if request.method=='POST':
        cmp=request.POST.get('tcmpname')
        tr=request.POST.get('ttr')
        tx=request.POST.get('ttx')
        dr=request.POST.get('tdr')
        drb=request.POST.get('tdrb')
        sad=request.POST.get('tsad')
        ii=request.POST.get('tii')
        at=request.POST.get('tat')
        td=Tds_Details(company_name=cmp,
                tan_regno=tr,
                tan=tx,
                deductor_type=dr,
                deductor_branch=drb,
                person_details=sad,
                ignore_it=ii,
                active_tds=at,
                company=id)
        td.save()
        print("added")
    return render(request,'tds_detuctor.html',{'id':id})

def tds_personal(request,pk):
    id=Companies.objects.get(id=pk)
    if request.method=="POST":
        name=request.POST.get('tpname')
        sd=request.POST.get('tpsd')
        dn=request.POST.get('tpdn')
        pn=request.POST.get('tppn')
        ft=request.POST.get('tpft')
        ps=request.POST.get('tpps')
        st=request.POST.get('spst')
        ln=request.POST.get('spln')
        dt=request.POST.get('spdt')
        se=request.POST.get('tpse')
        pin=request.POST.get('tppin')
        mb=request.POST.get('spmb')
        std=request.POST.get('spstd')
        te=request.POST.get('spte')
        el=request.POST.get('spel')
        tp=tds_person(name=name,
                        son_daughter=sd,
                        designation=dn,
                        pan=pn,
                        flat_no=ft,
                        building=ps,
                        street=st,
                        area=ln,
                        town=dt,
                        state=se,
                        pincode=pin,
                        mobile=mb,
                        std=std,
                        telephone=te,
                        email=el,
                        company=id)
        tp.save()
        messages.info(request,'tds personal details added..!!')
    return render(request,'tds_personal.html',{'id':id})

def ledger_cheque_dimenssion(request):
    
    if request.method == 'POST':
            cc=request.POST.get('ccon')
            cw= request.POST.get('cheque_width')
            ch= request.POST.get('cheque_height')
            sle= request.POST.get('startL_leftEdge')
            slte= request.POST.get('startL_topEdge')
            dlle= request.POST.get('distancel_leftEdge')
            dlte= request.POST.get('distancel_topEdge')
            ds= request.POST.get('date_style')
            dts= request.POST.get('date_seperator')
            sw= request.POST.get('separator_width')
            cd= request.POST.get('character_distance')
            pdle= request.POST.get('Pdistancel_leftEdge')
            pdlte= request.POST.get('Pdistancel_topEdge')
            aw= request.POST.get('area_width')
            sldte= request.POST.get('secondL_DTE')
            sflh= request.POST.get('secondfirstL_height')
            fldte= request.POST.get('firstL_dTE')
            slfle= request.POST.get('sl_fisrtl_LE')
            slsle= request.POST.get('sl_secondl_LE')
            awa= request.POST.get('amount_widtharea')
            cfnmp= request.POST.get('currencyFNM_print')
            dfte= request.POST.get('df_TE')
            sle= request.POST.get('startL_LE')
            amwa= request.POST.get('amt_widtharea')
            csp= request.POST.get('currencyS_print')
            cn= request.POST.get('company_name')
            pcn= request.POST.get('print_CN')
            sfs= request.POST.get('salutation_Fsign')
            sss= request.POST.get('salutation_Ssign')
            tes= request.POST.get('top_Edistance')
            slfl= request.POST.get('startLF_leftE')
            wsa= request.POST.get('width_sign_area')
            hsa= request.POST.get('height_sign_area')

            cld= ledger_cheque_demension(cheque_config=cc,cheque_width=cw,cheque_height=ch,startL_leftEdge=sle,startL_topEdge=slte,distancel_leftEdge=dlle,
                                        distancel_topEdge=dlte,date_style=ds,date_seperator=dts,separator_width=sw,character_distance=cd,
                                        Pdistancel_leftEdge=pdle,Pdistancel_topEdge=pdlte,area_width=aw,secondL_DTE=sldte,secondfirstL_height=sflh,
                                        firstL_dTE=fldte,sl_fisrtl_LE=slfle,sl_secondl_LE=slsle,amount_widtharea=awa,currencyFNM_print=cfnmp,
                                        df_TE=dfte,startL_LE=sle,amt_widtharea=amwa,currencyS_print=csp,company_name=cn,print_CN=pcn,
                                        salutation_Fsign=sfs,salutation_Ssign=sss,top_Edistance=tes,startLF_leftE=slfl,width_sign_area=wsa,
                                        height_sign_area=hsa)

            cld.save()
            return redirect('ledger_cheque_dimenssion')
    return render(request,'ledger_cheque_dimenssion.html')



#......................Riya........................

def index1(request):
    comp=Companies.objects.all()
    return render(request,'index1.html',{'comp':comp})

# def basepage(request):
#     comp=Companies.objects.all()
#     return render(request,'base.html',{'comp':comp})

def company(request):
    com=Companies.objects.all()
    return render(request,'company2.html',{'com':com})

# def createcompany(request):
#     # st=States.objects.all()
#     # country=Countries.objects.all()
#     return render(request,'createcompany.html')

def createcompany(request):
    # st=States.objects.all()
    # country=Countries.objects.all()
    return render(request,'createcompany.html')

# def companycreate(request):
#     if request.method=='POST':
#         n=Companies()
#         n.name=request.POST['companyname']
#         b=Companies.objects.filter(name=n.name)
#         if b:
#             messages.info(request,'Company name already exists!!')
#             return redirect('createcompany')
#         n.mailing_name=request.POST['mailing_name']
#         n.address=request.POST['address']
#         n.state=request.POST['state']
#         n.country=request.POST['country']
#         n.pincode=request.POST['pincode']
#         n.telephone=request.POST['telephone']
#         n.mobile=request.POST['mobile']
#         n.fax=request.POST['fax']
#         n.email=request.POST['email']
#         n.website=request.POST['website']
#         n.fin_begin=request.POST['fyear']
#         n.books_begin=request.POST['byear']
#         n.currency_symbol=request.POST['currency']
#         n.formal_name=request.POST['formal']
#         n.password=random.randint(10000, 99999)
#         out=datetime.strptime (n.fin_begin,'%Y-%m-%d')+timedelta (days=364) 
#         n.fin_end=out.date()
#         n.save()
        
#         subject = 'Welcome Tally Prime'
#         message = 'Congratulations,\n' \
#         'You have successfully registered with our website.\n' \
#         'username :'+str(n.email)+'\n' 'password :'+str(n.password) + \
#         '\n' 'WELCOME '
#         recepient = str(n.email)
#         send_mail(subject, message, EMAIL_HOST_USER,
#                 [recepient], fail_silently=False)
#         msg_success = "Registration successfully Check Your Registered Mail"
#         messages.info(request,'Company created successfully(Enable the features as per your business needs)')
#         return render(request,'features.html',{'cmp':n,'msg_success':msg_success})
    
#     return render(request,'features.html')

def companycreate(request):
    if request.method=='POST':
        n=Companies()
        n.name=request.POST['companyname']
        b=Companies.objects.filter(name=n.name)
        if b:
            messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        n.mailing_name=request.POST['mailing_name']
        n.address=request.POST['address']
        n.state=request.POST['state']
        n.country=request.POST['country']
        n.pincode=request.POST['pincode']
        n.telephone=request.POST['telephone']
        n.mobile=request.POST['mobile']
        n.fax=request.POST['fax']
        n.email=request.POST['email']
        n.website=request.POST['website']
        n.fin_begin=request.POST['fyear']
        n.books_begin=request.POST['byear']
        n.currency_symbol=request.POST['currency']
        n.formal_name=request.POST['formal']
        n.password=random.randint(10000, 99999)
        out=datetime.strptime (n.fin_begin,'%Y-%m-%d')+timedelta (days=364) 
        n.fin_end=out.date()
        n.save()
        subject = 'Welcome Tally Prime'
        message = 'Congratulations,\n' \
        'You have successfully registered with our website.\n' \
        'username :'+str(n.email)+'\n' 'password :'+str(n.password) + \
        '\n' 'WELCOME '
        recepient = str(n.email)
        send_mail(subject, message, EMAIL_HOST_USER,
                [recepient], fail_silently=False)
        msg_success = "Registration successfully Check Your Registered Mail"
        messages.info(request,'Company created successfully(Enable the features as per your business needs)')
        return render(request,'features.html',{'cmp':n,'msg_success':msg_success})
    
    return render(request,'features.html')

def group1(request):
    # feature=Features.objects.get(company_id=pk)
    # cmp=Companies.objects.get(id=pk)
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request,'group1.html',{'tally':tally})
    return redirect("/")

def costcentre(request):
    # cmp=Companies.objects.get(id=pk)
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method == 'POST':
            # cmp=Companies.objects.get(id=pk)
            cname = request.POST['cname']
            alia = request.POST['alia']
            under = request.POST['under']
            costc=cost_centre.objects.filter(cname=cname)
            if costc:
                # messages.info(request,'Company name already exists!!')
                pass
            else:
                
                data = cost_centre(cname=cname,cost_alias=alia,under=under,company_id=t_id)
                data.save()
                return redirect('base')
        ccentre=cost_centre.objects.filter(company_id=t_id)
        return render(request,'costcentre.html',{'ccentre':ccentre})
    return redirect('/')

def costcentre2(request):
    # cmp=Companies.objects.get(id=pk)
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method == 'POST':
            # cmp=Companies.objects.get(id=pk)
            cname = request.POST['cname']
            alia = request.POST['alia']
            under = request.POST['under']
            costc=cost_centre.objects.filter(cname=cname)
            if costc:
                # messages.info(request,'Company name already exists!!')
                pass
            else:
                
                data = cost_centre(cname=cname,cost_alias=alia,under=under,company_id=t_id)
                data.save()
                return redirect('base')
        # ccentre=cost_centre.objects.filter(company_id=cmp)
        return render(request,'costcentre2.html',{'ccentre':tally})
    return redirect('/')

def ratesofexchange(request):
    # cmp=Companies.objects.get(id=pk)
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method == 'POST':
            # cmp=Companies.objects.get(id=pk)
            
            currencyName = request.POST['cr']
            stdrate = request.POST['stdrate']
            # sell_voucher_rate = request.POST['sell_voucher_rate']
            sell_specified_rate = request.POST['sell_specified_rate']
            # buy_voucher_rate = request.POST['buy_voucher_rate']
            buy_specified_rate = request.POST['buy_specified_rate']
            mdl = rateofexchange(
                currencyName=currencyName,
                stdrate=stdrate,
                # sell_voucher_rate=sell_voucher_rate,
                sell_specified_rate=sell_specified_rate,
                # buy_voucher_rate=buy_voucher_rate,
                buy_specified_rate=buy_specified_rate,
                company_id = t_id)
            mdl.save()
            return redirect('base')
        cur=currencyAlteration.objects.filter(company_id=t_id)
        return render(request,'ratesofexchange.html',{'tally':tally,'curr':cur})
    return redirect('/')


def currency1(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        symbol = request.POST['symbol']
        formal_name = request.POST['formal_name']
        currency_code = request.POST['currency_code']
        decimal_places = request.POST['decimal_places']
        show_in_millions = request.POST['show_in_millions']
        suffix_symbol = request.POST['suffix_symbol']
        symbol_and_amount = request.POST['symbol_and_amount']
        after_decimal = request.POST['after_decimal']
        amount_in_words = request.POST['amount_in_words']
        data = currencyAlteration(Symbol=symbol,FormalName=formal_name,ISOCurrency=currency_code,
                        DecimalPlace=decimal_places,showAmount=show_in_millions,
                        suffixSymbol=suffix_symbol,AddSpace=symbol_and_amount,
                        DecimalWords=after_decimal,wordRep=amount_in_words,company=cmp)
        data.save()
        return redirect('index1')
    return render(request,'currency1.html',{'cmp':cmp})

def creategroup(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['under']
        sub_ledger = request.POST['sub_ledger']
        gross = request.POST['gross']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']
        nature = request.POST['nature']
        grp=tally_group.objects.filter(group_name=gname)
        if grp:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            mdl = tally_group(
                group_name=gname,
                group_alias=alia,
                group_under=under,
                sub_ledger=sub_ledger,
                debit_credit=nett,
                calculation=calc,
                invoice=meth,
                nature=nature,
                gross_profit=gross,
                company=cmp
            )
            mdl.save()
            return redirect('index1')
    grup=tally_group.objects.filter(company_id=cmp)
    return render(request,'group1.html',{'cmp':cmp,'grup':grup})

def group2(request):
    # cmp=Companies.objects.get(id=pk)
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method == 'POST':
            # cmp=Companies.objects.get(id=pk)
            gname = request.POST['gname']
            alia = request.POST['alia']
            under = request.POST['under']
            sub_ledger = request.POST['sub_ledger']
            gross = request.POST['gross']
            nett = request.POST['nee']
            calc = request.POST['cal']
            meth = request.POST['meth']
            nature = request.POST['nature']
            mdl = tally_group(
                    group_name=gname,
                    group_alias=alia,
                    group_under=under,
                    sub_ledger=sub_ledger,
                    debit_credit=nett,
                    calculation=calc,
                    invoice=meth,
                    nature=nature,
                    gross_profit=gross,
                    company_id=t_id
                )
            mdl.save()
            return redirect('base')
        grup=tally_group.objects.filter(company_id=t_id)
        return render(request,'group2.html',{'tally':tally,'grup':grup})
    return redirect('/')


def altercompanyview(request):
    com=Companies.objects.all()
    return render(request,'altercompanyview.html',{'com':com})

def altercompany(request,pk):
    # com=States.objects.all()
    # cntry=Countries.objects.all()
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        comp.name=request.POST['name']
        comp.mailing_name=request.POST['mailing_name']
        comp.address=request.POST['address']
        
        comp.states=request.POST['state']
        comp.country=request.POST['country']
        
        comp.pincode=request.POST['pincode']
        comp.telephone=request.POST['telephone']
        comp.mobile=request.POST['mobile']
        comp.fax=request.POST['fax']
        comp.email=request.POST['email']
        comp.website=request.POST['website']
        comp.fin_begin=request.POST['fin_begin']
        comp.books_begin=request.POST['books_begin']
        comp.currency_symbol=request.POST['currency_symbol']
        comp.formal_name=request.POST['formal_name']
        comp.save()
        return redirect('altercompanyview')
    return render(request,'editcompany.html',{'comp':comp})



def selectcompany(request):
    com=Companies.objects.all()
    return render(request,'selectcompany.html',{'com':com})

def addstate(request):
    if request.method=='POST':
        name=request.POST['name']
        cntryid=request.POST['cname']
        st=States.objects.filter(name=name)
        countr=Countries.objects.filter(name=cntryid)
        if st:
            # messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        else:
            data=States(name=name, country=countr)
            data.save()
            return redirect('createcompany')
    return render(request,'createcompany.html')

def addstatenew(name):
    return "";

def addcountry(request):
    if request.method=='POST':
        name=request.POST['name']
        con=Countries.objects.filter(name=name)
        if con:
            # messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        else:
            data=Countries(name=name)
            data.save()
        return redirect('createcompany')
    return render(request,'createcompany.html')

def featurecompany(request,pk):
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        maintain_accounts=request.POST['maintain_accounts']
        ctg=features(maintain_accounts=maintain_accounts, company= comp)
        ctg.save()
    return render(request,'company2.html')

def features1(request, pk):
    feature=Features.objects.get(company_id=pk)
    c=Companies.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST['maintain_accounts'] == 'Yes':
            feature.maintain_accounts= 'True'
        else:
            feature.maintain_accounts= 'False'
        if request.POST['bill_wise_entry'] == 'Yes':
            feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['cost_centres'] == 'Yes':
            feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['interest_calc'] == 'Yes':
            feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['maintain_inventory'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['integrate_accounts'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['multiple_price_level'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['batches'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['expirydate_batches'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['joborder_processing'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        
        if request.POST['cost_tracking'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['job_costing'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['discount_invoices'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['Billed_Quantity'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['gst'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['tds'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['tcs'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['vat'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['excise'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['servicetax'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['payroll'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['multiple_addrss'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['vouchers'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        
        feature.save()
    return render(request,'features1.html',{'ctg':c, 'ft':feature})

def shutcompany(request):
    com=Companies.objects.all()
    return render(request,'shutcompany1.html',{'com':com})

def disable(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=False
    c.save()
    return redirect('/')

# def enable(request,pk):
#     c=Companies.objects.get(id=pk)
#     c.status=True
#     c.save()
#     return redirect('shutcompany')

def featurepage(request):
    comp=Companies.objects.all()
    return render(request,'featurepage.html',{'comp':comp})



#......................Neethu.......................

def create(request):
    Country=Countries.objects.all()
    return render(request,'company1.html',{'country':Country})

def companycreate1(request):
    
    if request.method=="POST":
        name=request.POST['companyname']
        print(name)
        mailing_name=request.POST['mailing_name']
        print(mailing_name)
        address=request.POST['address']
        print(address)
        state=request.POST['state']
        print(state)
        country=request.POST['country']
        print(country)
        pincode=request.POST['pincode']
        print(pincode)
        telephone=request.POST['telephone']
        print(telephone)
        mobile=request.POST['mobile']
        print(mobile)
        fax=request.POST['fax']
        print(fax)
        email=request.POST['email1']
        print(email)
        website=request.POST['website']
        print(website)
        fin_begin=request.POST['fyear']
        print(fin_begin)
        books_begin=request.POST['byear']
        print(books_begin)
        currency_symbol=request.POST['currency']
        print(currency_symbol)
        formal_name=request.POST['formal']
        print(formal_name)
        cmp=Companies.objects.filter(name=name)
        
        out=datetime.datetime.strptime (fin_begin,'%Y-%m-%d')+timedelta (days=364) 
        print(out)
        a=out.date()
        print(a)
        if cmp:
            messages.info(request,'Company name already exists!!')
            return redirect('create')
        else:
            ctg=Companies(name=name,mailing_name=mailing_name,address=address,state=state,country=country,
                pincode=pincode,telephone=telephone,mobile=mobile,fax=fax,email=email,website=website,fin_begin=fin_begin,
                books_begin=books_begin,currency_symbol=currency_symbol,formal_name=formal_name,fin_end=a)
                
            ctg.save()
            messages.info(request,'Company created successfully(Enable the features as per your business needs)')
            return render(request,'features2.html',{'ctg':ctg})


def gst_details(request,pk):
    company=Companies.objects.get(id=pk)
    return render(request,'gst_details1.html',{'companies':company})

def add_gstdetails(request,pk):
    id=Companies.objects.get(id=pk)
    comp=Companies.objects.get(id=pk)
    
    if request.method=="POST":
        state=request.POST['state']
        registration_type=request.POST['registration_type']
        assessee=request.POST['assessee']
        fdate=request.POST['fdate']
        gstin=request.POST['gstin']
        periodicity=request.POST['periodicity']
        alter_gst=request.POST['alter_gst']
        tax_liabilityadvance=request.POST['tax_liabilityadvance']
        tax_liability=request.POST['tax_liability']
        gst_classifications=request.POST['gst_classifications']
        bond_details=request.POST['bond_details']
        eway_bill=request.POST['eway_bill']
        applicable_from=request.POST['applicable_from']
        treshold_limit=request.POST['treshold_limit']
        treshold_limit1=request.POST['treshold_limit1']
        intrastate=request.POST['intrastate']
        treshold_limit2=request.POST['treshold_limit2']
        print_ewaybill=request.POST['print_ewaybill']
        e_invoicing=request.POST['e_invoicing']
        applicable_from=request.POST['applicable_from']
        bill_from_place=request.POST['bill_from_place']
        period=request.POST['period']
        send_eway=request.POST['send_eway']
        gst=GST(state= state,reg_type=registration_type,assessee= assessee,gst_applicable= fdate,gstin= gstin,periodicity= periodicity,
                        gst_rate_details= alter_gst,advance_receipts=tax_liabilityadvance,reverse_charge=tax_liability,gst_classification= gst_classifications,
                        bond_details=bond_details,eway_bill= eway_bill,applicable_form=applicable_from,threshold_includes= treshold_limit,
                         threshold_limit=treshold_limit1,intrastate=intrastate,threshold_limit2=treshold_limit2,print_eway=print_ewaybill,e_invoice= e_invoicing,app_from=applicable_from,billfrom_place=bill_from_place,dperiod=period,send_ewaybill=send_eway,company=id)
        gst.save()
        messages.info(request,'Gst details added..!!')
    return redirect(request.META.get('HTTP_REFERER'))    

def tds_deductor(request,pk):
    comp=Companies.objects.get(id=pk)
    return render(request,'tds_deductor.html',{'company':comp})

def person_details(request,pk):
    com=Companies.objects.get(id=pk)
    return render(request,'person_details.html',{'comp':com})  

def add_person(request,pk):
    id=Companies.objects.get(id=pk)
    if request.method=="POST":
        name=request.POST['name']
        fname=request.POST['fname']
        Designation=request.POST['Designation']
        pan=request.POST['pan']
        address=request.POST['address']
        bname=request.POST['bname']
        road=request.POST['road']
        area=request.POST['area']
        city=request.POST['city']
        pin=request.POST['pin']
        state=request.POST['state']
        mobile=request.POST['mobile']
        std=request.POST['std']
        telephone=request.POST['telephone']
        email=request.POST['email']
        
        person=tds_person(name=name,son_daughter=fname,designation=Designation,pan=pan,flat_no=address,building=bname,street=road,area=area,town=city,
                      pincode=pin,state=state,mobile=mobile,std=std,telephone=telephone,email=email,company=id)
        person.save()
        messages.info(request,'Person details added..!!')
    return redirect(request.META.get('HTTP_REFERER'))  

def add_tds(request,pk):
    id=Companies.objects.get(id=pk)
    if(request.method=="POST"):
        tan_number=request.POST['tan_number']
        tan=request.POST['tan']
        deductor=request.POST['deductor']
        branch=request.POST['branch']
        person_details=request.POST['person_details']
        exemption=request.POST['exemption']
        active_tds=request.POST['active_tds']
        tds=Tds_Details(tan_regno=tan_number,tan=tan,deductor_type=deductor,deductor_branch=branch,person_details= person_details,
                        ignore_it=exemption,active_tds=active_tds,company=id)
        tds.save()
        messages.info(request,'TDS details added..!!')
    return redirect(request.META.get('HTTP_REFERER'))    

def features2(request,pk):
    id=Companies.objects.get(id=pk)
    # feature=Features.objects.get(company=pk)
    print(id)
    if request.method == "POST":
        maintain_accounts=request.POST['maintain_accounts']
        bill_wise_entry=request.POST['bill_wise_entry']
        cost_centres=request.POST['cost_centres']
        interest_calc=request.POST['interest_calc']
        maintain_inventory=request.POST['maintain_inventory']
        integrate_accounts=request.POST['integrate_accounts']
        multiple_price_level=request.POST['multiple_price_level']
        batches=request.POST['batches']
        expirydate_batches=request.POST['expirydate_batches']
        joborder_processing=request.POST['joborder_processing']
        cost_tracking=request.POST['cost_tracking']
        job_costing=request.POST['job_costing']
        Discount_coloumn=request.POST['Discount_coloumn']
        billed_quantity=request.POST['billed_quantity']
        gst=request.POST['gst']
        
        tds=request.POST['tds']
        tcs=request.POST['tcs']
        vat=request.POST['vat']
        excise=request.POST['excise']
        service_tax=request.POST['service_tax']
        payroll=request.POST['payroll']
       
        multiple_address=request.POST['multiple_address']
        Modified_vouchers=request.POST['Modified_vouchers']
        feature=Features(maintain_accounts=maintain_accounts,bill_wise_entry=bill_wise_entry, cost_centres= cost_centres,interest_calc=interest_calc,
                         maintain_inventory= maintain_inventory,integrate_accounts=integrate_accounts, multiple_price_level= multiple_price_level,
                          batches= batches, expirydate_batches= expirydate_batches,joborder_processing=joborder_processing,cost_tracking= cost_tracking,
                          job_costing=job_costing,discount_invoices=Discount_coloumn,Billed_Quantity=billed_quantity,gst=gst,tds=tds,tcs=tcs,vat=vat,
                          excise=excise, servicetax=service_tax,payroll=payroll,multiple_addrss=multiple_address,
                           vouchers=Modified_vouchers,company=id)
        feature.save() 
        
        return redirect('dashboard')
    return render(request,'features2.html',{'ctg':id})

def dashboard(request):
    com=Companies.objects.filter(status=True)
    
       
    comp1=Companies.objects.first()
    comp1.status=True
   
    comp1.save()
    return render(request,'dashboard.html',{'comp1':comp1,'com1':com})

# def company_list(request):
#     com=Companies.objects.all()
#     return render(request,'company_list.html',{'comp':com})       

def select_company(request):
    comp=Companies.objects.all()
    
    return render(request,'select_company1.html',{'comp1':comp})

def dash_board(request,pk):
    comp=Companies.objects.get(id=pk)
    comp.status=True
    comp.save()
    com=Companies.objects.filter(status=True)  
    return render(request,'dashboard.html',{'comp1':comp,'com1':com})

def alter_company(request):
    comp=Companies.objects.all()
    return render(request,'alter_company.html',{'comp1':comp})

def edit_page(request,pk):
    country=Countries.objects.all()
    com=Companies.objects.get(id=pk)
    return render(request,'edit_company.html',{'com':com,'country':country})

def edit_companydetails(request,pk):
    com=Companies.objects.get(id=pk)
    if request.method=="POST":
        com.name=request.POST['companyname']
       
        com.mailing_name=request.POST['mailing_name']
       
        com.address=request.POST['address']
        
        com.state=request.POST['state']
      
        com.country=request.POST['country']
       
        com.pincode=request.POST['pincode']
        
        com.telephone=request.POST['telephone']
        
        com.mobile=request.POST['mobile']
        
        com.fax=request.POST['fax']
        
        com.email=request.POST['email']
       
        com.website=request.POST['website']
        
        com.fin_begin=request.POST['fyear']
        com.books_begin=request.POST['byear']
       
        com.currency_symbol=request.POST['currency']
        
        com.formal_name=request.POST['formal']
        com.save()
        return redirect('dashboard')

def change_company1(request):
    com=Companies.objects.filter(status=True) 
    return render(request,'change_company1.html',{'com':com})        

def shut_company(request):
    com=Companies.objects.filter(status=True) 
    return render(request,'shut_company.html',{'com':com})

def shut1(request,pk):
    com=Companies.objects.get(id=pk)
    com.status=False
    com.save()
    comp1=Companies.objects.first()
    com=Companies.objects.filter(status=True) 
    return render(request,'dashboard.html',{'com1':com,'comp1':comp1})

def date_change(request):
    return render(request,'date.html')

def print_config(request):
    return render(request,'print_config.html')

def add_country(request):
    if request.method=="POST":
        print("a")
        country=request.POST['country_name']
        print(country)
        countries=Countries(name=country)
        countries.save()
        return redirect('create') 

def addstates(request):
    
    state=States.objects.filter(country_id=id)
    print(state)
    return render(request,'company1.html',{'state':state})

def state_country(request):
    return render(request,'state_country.html')

def load_cities(request):
    country_id=request.POST['country_id']
    states=States.objects.filter(country_id=country_id)
    return render(request,'company1.html',{'states':states})

def  edit_features(request,pk):
    id=Companies.objects.get(id=pk)
    # feature=Features.objects.get(company=pk)
    print(id)
    if request.method == "POST":
        maintain_accounts=request.POST['maintain_accounts']
        bill_wise_entry=request.POST['bill_wise_entry']
        cost_centres=request.POST['cost_centres']
        interest_calc=request.POST['interest_calc']
        maintain_inventory=request.POST['maintain_inventory']
        integrate_accounts=request.POST['integrate_accounts']
        multiple_price_level=request.POST['multiple_price_level']
        batches=request.POST['batches']
        expirydate_batches=request.POST['expirydate_batches']
        joborder_processing=request.POST['joborder_processing']
        cost_tracking=request.POST['cost_tracking']
        job_costing=request.POST['job_costing']
        Discount_coloumn=request.POST['Discount_coloumn']
        billed_quantity=request.POST['billed_quantity']
        gst=request.POST['gst']
        
        tds=request.POST['tds']
        tcs=request.POST['tcs']
        vat=request.POST['vat']
        excise=request.POST['excise']
        service_tax=request.POST['service_tax']
        payroll=request.POST['payroll']
        
        multiple_address=request.POST['multiple_address']
        Modified_vouchers=request.POST['Modified_vouchers']
        feature=Features(maintain_accounts=maintain_accounts,bill_wise_entry=bill_wise_entry, cost_centres= cost_centres,interest_calc=interest_calc,
                         maintain_inventory= maintain_inventory,integrate_accounts=integrate_accounts, multiple_price_level= multiple_price_level,
                          batches= batches, expirydate_batches= expirydate_batches,joborder_processing=joborder_processing,cost_tracking= cost_tracking,
                          job_costing=job_costing,discount_invoices=Discount_coloumn,Billed_Quantity=billed_quantity,gst=gst,tds=tds,tcs=tcs,vat=vat,
                          excise=excise, servicetax=service_tax,payroll=payroll,multiple_addrss=multiple_address,
                           vouchers=Modified_vouchers,company=id)
        feature.save() 
        
        return redirect('dashboard')
    return render(request,'edit_features.html',{'ctg':id})

def edit_gst_details(request,pk):
    id=Companies.objects.get(id=pk)
    comp=Companies.objects.get(id=pk)
    gst=GST.objects.get(company_id=pk)
    
    return render(request,'edit_gst_details.html',{'gst':gst,'comp':comp})

def add_newgstdetails(request,pk):
    gst=GST.objects.get(company_id=pk)
    if request.method=="POST":
        gst.state=request.POST['state']
        gst.registration_type=request.POST['registration_type']
        gst.assessee=request.POST['assessee']
        gst.fdate=request.POST['fdate']
        gst.gstin=request.POST['gstin']
        gst.periodicity=request.POST['periodicity']
        gst.alter_gst=request.POST['alter_gst']
        gst.tax_liabilityadvance=request.POST['tax_liabilityadvance']
        gst.tax_liability=request.POST['tax_liability']
        gst.gst_classifications=request.POST['gst_classifications']
        gst.bond_details=request.POST['bond_details']
        gst.eway_bill=request.POST['eway_bill']
        gst.applicable_from=request.POST['applicable_from']
        gst.treshold_includes=request.POST['treshold_limit']
        gst.treshold_limit=request.POST['treshold_limit1']
        gst.intrastate=request.POST['intrastate']
        gst.treshold_limit2=request.POST['treshold_limit2']
        gst.print_ewaybill=request.POST['print_ewaybill']
        gst.e_invoicing=request.POST['e_invoicing']
        gst.app_from=request.POST['applicable_from']
        gst.billfrom_place=request.POST['bill_from_place']
        gst.dperiod=request.POST['period']
        gst.send_ewaybill=request.POST['send_eway']
        gst.save()
        messages.info(request,'Gst details updated..!!')
    return redirect(request.META.get('HTTP_REFERER'))

def edit_tds_deductor(request,pk):
    id=Companies.objects.get(id=pk)
    comp=Companies.objects.get(id=pk)
    tds=Tds_Details.objects.get(company_id=pk)
    
    return render(request,'edit_tds_details.html',{'tds':tds,'comp':comp})

def add_newtdsdetails(request,pk):
    tds=Tds_Details.objects.get(company_id=pk)
    if(request.method=="POST"):
        tds.tan_number=request.POST['tan_number']
        tds.tan=request.POST['tan']
        tds.deductor=request.POST['deductor']
        tds.branch=request.POST['branch']
        tds.person_details=request.POST['person_details']
        tds.exemption=request.POST['exemption']
        tds.active_tds=request.POST['active_tds']
        
        tds.save()
        messages.info(request,'TDS details updated..!!')
    return redirect(request.META.get('HTTP_REFERER'))   

def edit_person_details(request,pk):
    id=Companies.objects.get(id=pk)
    comp=Companies.objects.get(id=pk)
    person=tds_person.objects.get(company_id=pk)
    
    return render(request,'editperson_details.html',{'person':person,'comp':comp})

def add_newpersondetails(request,pk):
    person=tds_person.objects.get(company_id=pk)
    if request.method=="POST":
        person.name=request.POST['name']
        person.fname=request.POST['fname']
        person.Designation=request.POST['Designation']
        person.pan=request.POST['pan']
        person.address=request.POST['address']
        person.bname=request.POST['bname']
        person.road=request.POST['road']
        person.area=request.POST['area']
        person.city=request.POST['city']
        person.pin=request.POST['pin']
        person.state=request.POST['state']
        person.mobile=request.POST['mobile']
        person.std=request.POST['std']
        person.telephone=request.POST['telephone']
        person.email=request.POST['email']
        
       
        person.save()
        messages.info(request,'Person details Updated..!!')
    return redirect(request.META.get('HTTP_REFERER'))  

def company_list1(request):
    com=Companies.objects.all()
    return render(request,'company_list1.html',{'comp':com})  



#......................Rafi........................

# def stock_group(request):
#     und=CreateStockGrp.objects.all()
#     if request.method=='POST':
#         name=request.POST['name']
#         alias=request.POST['alias']
#         under_name=request.POST['under_name']
#         quantities=request.POST['quantities']
#         stockgrp=CreateStockGrp(name=name,alias=alias,under_name=under_name,quantities=quantities)
#         stockgrp.save()
#         return redirect('stock_group')
#     return render(request,'stock_group.html',{'und':und})

# def stock_group_secondary(request):
#     und=CreateStockGrp.objects.all()
#     if request.method=='POST':
#         name=request.POST['name']
#         alias=request.POST['alias']
#         under_name=request.POST['under_name']
#         quantities=request.POST['quantities']
#         stockgrp=CreateStockGrp(name=name,alias=alias,under_name=under_name,quantities=quantities)
#         stockgrp.save()
#         return redirect('stock_group')
#     return render(request,'stock_group(secondary).html',{'und':und})

def stock_category_creation(request):
    und=CreateStockCateg.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        stockCateg=CreateStockCateg(name=name,alias=alias,under_name=under_name)
        stockCateg.save()
    return render(request,'stock_category_creation.html',{'und':und})

def stock_category_secondary(request):
    und=CreateStockCateg.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        stockCateg=CreateStockCateg(name=name,alias=alias,under_name=under_name)
        stockCateg.save()
        return redirect('stock_category_creation')
    return render(request,'stock_category(secondary).html',{'und':und})

# def stock_items(request):
#     cat=CreateStockCateg.objects.all()
#     grp=CreateStockGrp.objects.all()
#     unt=UnitCrt.objects.all()
#     if request.method=='POST':
#         name=request.POST['name']
#         alias=request.POST['alias']
#         under=request.POST['under']
#         category=request.POST['category']
#         units=request.POST['units']
#         batches=request.POST['batches']
#         manufacturing_date=request.POST['manufacturing_date']
#         expiry_dates=request.POST['expiry_dates']
#         rate_of_duty=request.POST['rate_of_duty']
#         quantity=request.POST['quantity']
#         rate=request.POST['rate']
#         per=request.POST['per']
#         value=request.POST['value']
#         additional=request.POST['additional']
#         crt=stock_item_crt(name=name,alias=alias,under=under,category=category,units=units,batches=batches,
#                            manufacturing_date=manufacturing_date,expiry_dates=expiry_dates,
#                            rate_of_duty=rate_of_duty,quantity=quantity,rate=rate,per=per,value=value,additional=additional)
#         crt.save()
#     return render(request,'stock_items.html',{'cat':cat,'grp':grp,'unt':unt})


# def unit_creation(request):
#     unit=UnitCrt.objects.all()
#     if request.method=='POST':
#         type=request.POST['type']
#         symbol=request.POST['symbol']
#         formal_name=request.POST['formal_name']
#         uqc=request.POST['uqc']
#         decimal=request.POST['decimal']
#         first_unit=request.POST['first_unit']
#         conversion=request.POST['conversion']
#         second_unit=request.POST['second_unit']
#         crt=UnitCrt(type=type,symbol=symbol,formal_name=formal_name,uqc=uqc,decimal=decimal,first_unit=first_unit,conversion=conversion,second_unit=second_unit)
#         crt.save()
#     return render(request,'unit1.html',{'unit':unit})

def uqc(request):
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        uqc=request.POST['uqc']
        crt=UnitCrt(uqc=uqc)
        crt.save()
        return redirect('unit_creation')
    return render(request,'uqc.html')

# def unit_creation_secondary(request):
#     unit=UnitCrt.objects.all()
#     if request.method=='POST':
#         type=request.POST['type']
#         symbol=request.POST['symbol']
#         formal_name=request.POST['formal_name']
#         uqc=request.POST['uqc']
#         decimal=request.POST['decimal']
#         first_unit=request.POST['first_unit']
#         conversion=request.POST['conversion']
#         second_unit=request.POST['second_unit']
#         crt=UnitCrt(type=type,symbol=symbol,formal_name=formal_name,uqc=uqc,decimal=decimal,first_unit=first_unit,conversion=conversion,second_unit=second_unit)
#         crt.save()
#     return render(request,'unit_creation(secondary).html',{'unit':unit})

def uqc_secondary(request):
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        uqc=request.POST['uqc']
        crt=UnitCrt(uqc=uqc)
        crt.save()
        return redirect('unit_creation')
    return render(request,'uqc.html')

def godown_alteration(request):
    gd=CreateGodown.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        gdcrt=CreateGodown(name=name,alias=alias,under_name=under_name)
        gdcrt.save()
    return render(request,'godown_alteration.html',{'gd':gd})

# def godown_secondary(request):
#     gd=CreateGodown.objects.all()
#     if request.method=='POST':
#         name=request.POST['name']
#         alias=request.POST['alias']
#         under_name=request.POST['under_name']
#         gdcrt=CreateGodown(name=name,alias=alias,under_name=under_name)
#         gdcrt.save()
#         return redirect('godown_alteration')
#     return render(request,'godown(secondary).html',{'gd':gd})

def employee_group_creation(request):
    emp=CreateEmployeeGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        crt=CreateEmployeeGrp(name=name,alias=alias,under_name=under_name)
        crt.save()
    return render(request,'employee_group_creation.html',{'emp':emp})

def emloyee_group_secondary(request):
    emp=CreateEmployeeGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        crt=CreateEmployeeGrp(name=name,alias=alias,under_name=under_name)
        crt.save()
    return render(request,'employee_group(secondary).html',{'emp':emp})


def employee_creation(request):
    grp=CreateEmployeeGrp.objects.all()
    emp=employee_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        doj=request.POST['doj']
        salary=request.POST['salary']
        empno=request.POST['empno']
        designation=request.POST['designation']
        function_name=request.POST['function_name']
        location=request.POST['location']
        gender=request.POST['gender']
        dob=request.POST['dob']
        bld_grp=request.POST['bld_grp']
        father_mother=request.POST['father_mother']
        spouse=request.POST['spouse']
        address=request.POST['address']
        phn=request.POST['phn']
        email=request.POST['email']
        bank=request.POST['bank']
        incometax=request.POST['incometax']
        adhar=request.POST['adhar']
        uan=request.POST['uan']
        pf=request.POST['pf']
        pr=request.POST['pr']
        esi=request.POST['esi']
        crt=employee_crt(name=name,alias=alias,under_name=under_name,doj=doj,salary=salary,empno=empno,designation=designation,
                         function_name=function_name,location=location,gender=gender,dob=dob,bld_grp=bld_grp,father_mother=father_mother,
                         spouse=spouse,address=address,phn=phn,email=email,bank=bank,incometax=incometax,adhar=adhar,uan=uan,pf=pf,pr=pr,esi=esi)
        crt.save()
        request.session["name"]=name            
    return render(request,'employee_creation.html',{'emp':emp,'grp':grp})
    
def price_levels(request):
    if request.method=="POST":
        number=request.POST['number']
        crt=Price_level_crt(number=number)
        crt.save()
        return redirect('price_levels')
    price=Price_level_crt.objects.all()
    return render(request,'price_levels.html',{"price":price})

def pan_cin(request):
    pc=pancin.objects.all()
    if request.method=='POST':
        pan=request.POST['pan']
        cin=request.POST['cin']
        crt=pancin(pan=pan,cin=cin)
        crt.save()
    return render(request,'pan_cin.html')

def pay_head(request):
    att=attendance_crt.objects.all()
    pay=payhead_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        payhead_type=request.POST['payhead_type']
        under_name=request.POST['under_name']
        net_salary=request.POST['net_salary']
        pay_slip_name1=request.POST['pay_slip_name']
        currency_ledger=request.POST['currency_ledger']
        calculation_type=request.POST['calculation_type']
        attendance_type=request.POST['attendance_type']
        production_type=request.POST['production_type']
        crt=payhead_crt(name=name,alias=alias,payhead_type=payhead_type,under_name=under_name,net_salary=net_salary,pay_slip_name=pay_slip_name1,currency_ledger=currency_ledger,calculation_type=calculation_type
                        ,attendance_type=attendance_type,production_type=production_type)
        crt.save()
    return render(request,'pay_head.html',{'att':att,'pay':pay})


def load(request):
    did=request.GET.get("id")
    obj=payhead_crt.objects.get(name=did)
    return render(request,"load.html",{"obj":obj})

def load_calculation(request):
    did=request.GET.get("id")
    obj=payhead_crt.objects.get(name=did)
    return render(request,"load_calculation.html",{"obj":obj})

def bank(request):
    emp=CreateEmployeeGrp.objects.all()
    if request.method=='POST':
        accno=request.POST['accno']
        ifsc_Code=request.POST['ifsc_Code']
        bank_name=request.POST['bank_name']
        branch=request.POST['branch']
        crt=bank_crt(accno=accno,ifsc_Code=ifsc_Code,bank_name=bank_name,branch=branch)
        crt.save
        return redirect('employee_creation')
    return render(request,'bank_details1.html',{'emp':emp})


def payroll(request):
    if request.method=='POST':
        name=request.POST['name']
        allias=request.POST['allias']
        voucher_type=request.POST['voucher_type']
        abbreviation=request.POST['abbreviation']
        activate_voucher=request.POST['activate_voucher']
        voucher_numbering_method=request.POST['voucher_numbering_method']
        effective_dates=request.POST['effective_dates']
        narration_voucher=request.POST['narration_voucher']
        print_voucher=request.POST['print_voucher']
        classs=request.POST['classs']
        crt=payroll_crt(name=name,allias=allias,voucher_type=voucher_type,abbreviation=abbreviation,activate_voucher=activate_voucher,
                        voucher_numbering_method=voucher_numbering_method,effective_dates=effective_dates,
                        narration_voucher=narration_voucher,
                        print_voucher=print_voucher,classs=classs)
        crt.save()
        
        
    return render(request,'payroll_voucher_type.html')


def attendance(request):
    att=attendance_crt.objects.all()
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        attendance=request.POST['attendance']
        period=request.POST['period']
        units=request.POST['units']
        crt=attendance_crt(name=name,alias=alias,under_name=under_name,attendance=attendance,period=period,units=units,company_id=t_id)
        crt.save()
    return render(request,'attendance.html',{'att':att,'unit':unit})

def attendance_seconday(request):
    att=attendance_crt.objects.all()
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        attendance=request.POST['attendance']
        period=request.POST['period']
        units=request.POST['units']
        crt=attendance_crt(name=name,alias=alias,under_name=under_name,attendance=attendance,period=period,units=units)
        crt.save()
    return render(request,'attendance(secondary).html',{'att':att,'unit':unit})

def salary_details(request):
    pay=payhead_crt.objects.all()
    sal=salary_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        date=request.POST['date']
        pay_head_name=request.POST['pay_head_name']
        rate=request.POST['rate']
        pay_head_type=request.POST['pay_head_type']
        calculation_type=request.POST['calculation_type']
        crt=salary_crt(name=name,alias=alias,date=date,pay_head_name=pay_head_name,pay_head_type=pay_head_type,rate=rate,calculation_type=calculation_type)
        crt.save()
    return render(request,'salary_details.html',{'pay':pay,'sal':sal})

def stock_item_allocations(request):
    gd=CreateGodown.objects.all()
    if request.method=="POST":
        allocate=request.POST['allocate']
        for_allocate=request.POST['for_allocate']
        godown=request.POST['godown']
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        per=request.POST['per']
        amount=request.POST['amount']
        crt=allocate_stock(allocate=allocate,for_allocate=for_allocate,godown=godown,
                           quantity=quantity,rate=rate,per=per,amount=amount)
        crt.save()
        return redirect("stock_items")
    return render(request,'allocation_stock_item.html',{'gd':gd})


#......................Ann........................

def disp_more_reports(request):#ann
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        com=Companies.objects.filter(id=t_id)
        return render(request,'dispmorereprt.html',{'com':com})
    return redirect('/')

def salesregister(request):#ann
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cmp=Companies.objects.get(id=t_id)
    
        credit=Sales.objects.all().annotate(month=TruncMonth('sales_date')).values('month').annotate(total=Sum('total')).order_by('month').values("month", "total")      
        sales=Sales.objects.all()                     
        a=sales.filter(sales_date__month='04')
        april= sum(a.values_list('total',flat=True))
        ma=sales.filter(sales_date__month='05')
        may= sum(ma.values_list('total',flat=True))
        ju=sales.filter(sales_date__month='06')
        june= sum(ju.values_list('total',flat=True))
        jl=sales.filter(sales_date__month='07')
        july= sum(jl.values_list('total',flat=True))
        au=sales.filter(sales_date__month='08')
        august= sum(au.values_list('total',flat=True))
        sep=sales.filter(sales_date__month='09')
        september= sum(sep.values_list('total',flat=True))
        oct=sales.filter(sales_date__month='10')
        october= sum(oct.values_list('total',flat=True))
        nov=sales.filter(sales_date__month='11')
        november= sum(nov.values_list('total',flat=True))
        dec=sales.filter(sales_date__month='12')
        december= sum(dec.values_list('total',flat=True))
        jan=sales.filter(sales_date__month='01')
        january= sum(jan.values_list('total',flat=True))
        feb=sales.filter(sales_date__month='02')
        febuary= sum(feb.values_list('total',flat=True))
        m=sales.filter(sales_date__month='03')
        march= sum(m.values_list('total',flat=True))
        data={}
        data['april']=april
        data['june']=june
        data['july']=july
        data['august']=august
        data['september']=september
        data['october']=october
        data['november']=november
        data['december']=december
        data['january']=january
        data['febuary']=febuary
        data['march']=march 
        data['may']=may
        data['cmp']=cmp
        total1=sum(sales.values_list('total',flat=True)) 
        return render(request,'salesregister.html',{'total1':total1,'data':data})         

def purchaseregister(request):#ann
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cmp=Companies.objects.get(id=t_id)
    P=Purchase.objects.all()
    a=P.filter(purchase_date__month='04')
    april= sum(a.values_list('total',flat=True))
    ma=P.filter(purchase_date__month='05')
    may= sum(ma.values_list('total',flat=True))
    ju=P.filter(purchase_date__month='06')
    june= sum(ju.values_list('total',flat=True))
    jl=P.filter(purchase_date__month='07')
    july= sum(jl.values_list('total',flat=True))
    au=P.filter(purchase_date__month='08')
    august= sum(au.values_list('total',flat=True))
    sep=P.filter(purchase_date__month='09')
    september= sum(sep.values_list('total',flat=True))
    oct=P.filter(purchase_date__month='10')
    october= sum(oct.values_list('total',flat=True))
    nov=P.filter(purchase_date__month='11')
    november= sum(nov.values_list('total',flat=True))
    dec=P.filter(purchase_date__month='12')
    december= sum(dec.values_list('total',flat=True))
    jan=P.filter(purchase_date__month='01')
    january= sum(jan.values_list('total',flat=True))
    feb=P.filter(purchase_date__month='02')
    febuary= sum(feb.values_list('total',flat=True))
    m=P.filter(purchase_date__month='03')
    march= sum(m.values_list('total',flat=True))
    data={}
    data['april']=april
    data['june']=june
    data['july']=july
    data['august']=august
    data['september']=september
    data['october']=october
    data['november']=november
    data['december']=december
    data['january']=january
    data['febuary']=febuary
    data['march']=march 
    data['may']=may
    data['cmp']=cmp
    
    total1 = sum(P.values_list('total', flat=True))  
    return render(request,'purchaseregister.html',{'total1':total1,'data':data}) 

def journalregister(request):#ann
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cmp=Companies.objects.get(id=t_id)
    P=Journal.objects.all()
    april=P.filter(journal_date__month='04').count()
    may=P.filter(journal_date__month='05').count()
    june=P.filter(journal_date__month='06').count()
    july=P.filter(journal_date__month='07').count()
    august=P.filter(journal_date__month='08').count()
    september=P.filter(journal_date__month='09').count()
    october=P.filter(journal_date__month='10').count()
    november=P.filter(journal_date__month='11').count()
    december=P.filter(journal_date__month='12').count()
    january=P.filter(journal_date__month='01').count()
    febuary=P.filter(journal_date__month='02').count()
    march=P.filter(journal_date__month='03').count()
    data={}
    data['april']=april
    data['june']=june
    data['july']=july
    data['august']=august
    data['september']=september
    data['october']=october
    data['november']=november
    data['december']=december
    data['january']=january
    data['febuary']=febuary
    data['march']=march 
    data['may']=may
    data['cmp']=cmp
    return render(request,'journal_report.html',{'data':data})  

def listofsalesvoucher(request,pk):#ann
   # s=Sales.objects.all()
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cmp=Companies.objects.get(id=t_id)
    m=pk
    s= Sales.objects.filter(sales_date__year='2022', 
                     sales_date__month=m)
 
    total1 = sum(s.values_list('total', flat=True))               
       
    if m==1:
            msg1="1-Jan-22  to 31-Jan-22"
    elif m==2:
            msg1="1-Feb-22  to 28-Feb-22"
    elif m ==3:
            msg1="1-March-22  to 31-March-22"
    elif m ==4:
        
             msg1="1-April-22 to 30-April-22"
    elif m ==5:
             msg1="1-May-22  to 31-May-22"
    elif m ==6:
            msg1="1-June-22 to 30-June-22"
    elif m ==7:
            msg1="1-July-22  to 31-July-22"
    elif m ==8:
             msg1="1-Aug-22  to 31-Aug-22"  
    elif m==9:
            msg1="1-Sep-22  to 30-Sep-22"
    elif m ==10:
             msg1="1-Oct-22 to 31-Oct-22"
    elif m ==11:
            msg1="1-Nov-22 to 30-Nov-22" 
    elif m ==12:
             msg1="1-Dec-22 to 31-Dec-22"     
    else:
        msg1="01-July-22 to 31-July-22" 
    return render(request,'listofsalesvouchers.html',{'sales':s,'msg1':msg1,'total1':total1,'cmp':cmp})  


def listofpurchasevoucher(request,pk):#ann
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cmp=Companies.objects.get(id=t_id)
    m=pk
    p= Purchase.objects.filter(purchase_date__year='2022', 
                     purchase_date__month=m)   
    total1 = sum(p.values_list('total', flat=True))                             
    if m==1:
            msg1="1-Jan-22  to 31-Jan-22"
    elif m==2:
            msg1="1-Feb-22  to 28-Feb-22"
    elif m ==3:
            msg1="1-March-22  to 31-March-22"
    elif m ==4:
             msg1="1-April-22 to 30-April-22"
    elif m ==5:
             msg1="1-May-22  to 31-May-22"
    elif m ==6:
            msg1="1-June-22 to 30-June-22"
    elif m ==7:
            msg1="1-July-22  to 31-July-22"
    elif m ==8:
             msg1="1-Aug-22  to 31-Aug-22"  
    elif m==9:
            msg1="1-Sep-22  to 30-Sep-22"
    elif m ==10:
             msg1="1-Oct-22 to 31-Oct-22"
    elif m ==11:
            msg1="1-Nov-22 to 30-Nov-22" 
    elif m ==12:
             msg1="1-Dec-22 to 31-Dec-22"      
    else:
        msg1="01-July-22 to 31-July-22"      
    print(p)         
    return render(request,'listofpurchasevouchers.html',{'purchase':p,'msg1':msg1,'total1':total1,'cmp':cmp})

def listjournalvouchers(request,pk):#ann 
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cmp=Companies.objects.get(id=t_id)
    m=pk
    j= Journal.objects.filter(journal_date__year='2022', 
                     journal_date__month=m)   
    total1 = sum(j.values_list('total', flat=True))                       
    if m==1:
            msg1="1-Jan-22  to 31-Jan-22"
    elif m==2:
            msg1="1-Feb-22  to 28-Feb-22"
    elif m ==3:
            msg1="1-March-22  to 31-March-22"
    elif m ==4:
             msg1="1-April-22 to 30-April-22"
    elif m ==5:
             msg1="1-May-22  to 31-May-22"
    elif m ==6:
            msg1="1-June-22 to 30-June-22"
    elif m ==7:
            msg1="1-July-22  to 31-July-22"
    elif m ==8:
             msg1="1-Aug-22  to 31-Aug-22"  
    elif m==9:
            msg1="1-Sep-22  to 30-Sep-22"
    elif m ==10:
             msg1="1-Oct-22 to 31-Oct-22"
    elif m ==11:
            msg1="1-Nov-22 to 30-Nov-22" 
    elif m ==12:
             msg1="1-Dec-22 to 31-Dec-22"      
    else:
        msg1="01-July-22 to 31-July-22"                        
    return render(request,'listjournalvouchers.html',{'journal':j,'msg1':msg1,'cmp':cmp,'total1':total1})


#......................Niyas........................

# def liststockviews(request):
#     data=stock_item_crt.objects.all()
#     context={'data':data}
#     return render(request, 'liststock.html',context)

# def liststockgroupviews(request):
#     data=CreateStockGrp.objects.all()
#     context={'data':data}
#     return render(request, 'liststockgroup.html',context)

# def singlestockgroupanalysisview(request,pk):
#     data1=CreateStockGrp.objects.get(id=pk)
#     data2=stock_item_crt.objects.get(under=data1)
#     data=analysis_view.objects.filter(particular=data2)
#     sum1 = 0
#     sum2 = 0
#     sum3 = 0
#     sum4 = 0
#     sum5 = 0
#     sum6 = 0
#     for a in data:
#         sum1 += a.iquantity
#     for b in data:
#         sum2 += b.ieff_rate
#     for c in data:
#         sum3 += c.ivalue
#     for d in data:
#         sum4 += d.oquantity
#     for e in data:
#         sum5 += e.oeff_rate
#     for f in data:
#         sum6 += f.ovalue
#     context={'data':data,'data1':data1,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum5':sum5,'sum6':sum6}
#     return render(request, 'singlestockgroupanalysis.html',context)


# def itemmovementanalysisview(request):
#     data1=purchase_model.objects.all()
#     data2=sale_model.objects.all()
#     context={'data1':data1,'data2':data2}
#     return render(request, 'itemmovementanalysis.html',context)


# def querystockview(request,pk):
#     data=stock_item_crt.objects.get(id=pk)
#     # ndata=CreateGodown.objects.all()
#     ndata=CreateGodown.objects.filter(itm=data)
#     total_sum = 0
#     for item in ndata:
#         total_sum += item.itm.quantity
#     # sums=CreateGodown.objects.filter(ndata).sum()
#     # purchase=purchase_model.objects.all()
#     purchase=purchase_model.objects.filter(itm=data)
#     # sale=sale_model.objects.all()
#     sale=sale_model.objects.filter(itm=data)
#     # cat=CreateStockCateg.objects.all()
#     cat=CreateStockCateg.objects.filter(itm=data)
    
#     context={'data':data,'ndata':ndata,'purchase':purchase,'sale':sale,'cat':cat,'total_sum':total_sum}
#     return render(request, 'querystocks.html',context)


# def purchasevoucheranalysisview(request,pk):
#     data=purchase_model.objects.get(id=pk)
#     context={'data':data}
#     return render(request, 'purchasevoucheranalysis.html',context)

# def salevoucheranalysisview(request,pk):
#     data=sale_model.objects.get(id=pk)
#     context={'data':data}
#     return render(request, 'salevoucheranalysis.html',context)


# def stockgroupanalysisview(request):
#     data=analysis_view.objects.all()
#     # var1=analysis_view.objects.get(ivalue)
#     # list1=list(var1)
#     # sums=sum(list1)
#     # for ivalue in data:
#     #     list1=sum(ivalue)
#     #     print(list1)
#     # sums=analysis_view.objects.aggregate(Sum('ivalue'))
#     # ModelName.objects.filter(field_name__isnull=True).aggregate(Sum('field_name'))
#     sum1 = 0
#     sum2 = 0
#     for a in data:
#         sum1 += a.ivalue
#     for b in data:
#         sum2 += b.ovalue
#     context={'data':data,'sum1':sum1,'sum2':sum2}
#     return render(request, 'stockgroupanalysis.html',context)

def stockitmecreateview(request):
    data=CreateStockGrp.objects.all()
    context={'data':data}
    return render(request, 'stockitemcreation.html',context) 

def savestockgroup1(request):
    if request.method == 'POST':
        gpname=request.POST['name']
        gpalias=request.POST['alias']
        gpunder=request.POST.get('und')
        gpquantity=request.POST.get('qty')
        data=CreateStockGrp(name=gpname,alias=gpalias,under=gpunder,quantities=gpquantity)
        data.save()
        return redirect('liststockgroupviews')

def savestockitem(request):
    if request.method == 'POST':
        iname=request.POST['name']
        ialias=request.POST['alias']
        iunder=request.POST['under']
        und=CreateStockGrp.objects.get(id=iunder)
        iunitr=request.POST.get('unit')
        igst=request.POST.get('gst')
        isupply=request.POST.get('supply')
        iduty=request.POST.get('rduty')
        iquantity=request.POST.get('qnt')
        irate=request.POST.get('rate')
        iper=request.POST.get('per')
        ivalue=request.POST.get('value')
        data=stock_item_crt(name=iname,alias=ialias,under=und,gst=igst,supply=isupply,rduty=iduty,quantity=iquantity,rate=irate,per=iper,value=ivalue)
        data.save()
        
        return redirect('liststockviews')


#......................Jerin........................

def receivabl(request):
    rec=receivable.objects.all()
    return render (request,'receivable.html',{'rec':rec}) 

def payabl(request):
    pay=payable.objects.all()
    return render(request,'payable.html',{'pay':pay})  

def creategroup1(request):
    grp=GroupModel.objects.all()
    return render (request,'creategroup.html1',{'grp':grp})     


def create_group1(request):
    if request.method == 'POST':
        group_name = request.POST['group_name']

       
        group_alias = request.POST['group_alias']
        
        group_under = request.POST['group_under']
        nature=request.POST['nature']

        gross_profit=request.POST['gross_profit']


        sub_ledger = request.POST['sub_ledger']
        debit_credit = request.POST['debit_credit']
        calculation = request.POST['calculation']
        invoice = request.POST['invoice']

        mdl = GroupModel(
            group_name=group_name,
            group_alias=group_alias,
            group_under=group_under,
            nature=nature,
            gross_profit=gross_profit,
            sub_ledger=sub_ledger,
            debit_credit=debit_credit,
            calculation=calculation,
            invoice=invoice,
        )
        mdl.save()
        return redirect('createledger')
        

def grcreate(request):
    gr=GroupModel.objects.all()
    return render(request,'grcreate.html',{'gr':gr})    

def createledger(request):
    grp=GroupModel.objects.all()
    return render (request,'createledger.html',{'grp':grp})     

def credit(request):
    cre=cred.objects.all()
    return render(request,'credit.html',{'cre':cre})

def debi(request):
    debi=debit.objects.all()
    return render(request,'debit.html',{'debi':debi})   

def ledgerlist(request):
    ledg=ledgercreation.objects.all()
    return render(request,'ledgerlist.html',{'ledg':ledg})    

def ledgercreations(request):
    if request.method == 'POST':
        
        name=request.POST['name']

        alias=request.POST['alias']
        under=request.POST['under']
        bank_details=request.POST['bank_details']
        
        ac_holder_nm=request.POST['ac_holder_nm']

        acc_no=request.POST['acc_no']
        if acc_no=="":
            acc_no=None

        ifsc_code=request.POST['ifsc_code']
        if ifsc_code=="":
            ifsc_code=None

        swift_code=request.POST['swift_code']
        if swift_code=="":
            swift_code=None

        bank_name=request.POST['bank_name']
        branch=request.POST['branch']
        SA_cheque_bk=request.POST['SA_cheque_bk']
        Echeque_p=request.POST['Echeque_p']

        occ_set_odl=request.POST['occ_set_odl']
        occ_ac_holder_nm=request.POST['occ_ac_holder_nm']
        occ_acc_no=request.POST['occ_acc_no']
        if occ_acc_no=="":
            occ_acc_no=None

        occ_ifsc_code=request.POST['occ_ifsc_code']
        if occ_ifsc_code=="":
            occ_ifsc_code=None

        occ_swift_code=request.POST['occ_swift_code']    
        if occ_swift_code=="":
            occ_swift_code=None

        occ_bank_name=request.POST['occ_bank_name']   
        occ_branch=request.POST['occ_branch']
        occ_SA_cheque_bk=request.POST['occ_SA_cheque_bk']
        occ_Echeque_p=request.POST['occ_Echeque_p']

        od_set_odl=request.POST['od_set_odl']
        od_ac_holder_nm=request.POST['od_ac_holder_nm']
        od_acc_no=request.POST['od_acc_no']
        if od_acc_no=="":
            od_acc_no=None

        od_ifsc_code=request.POST['od_ifsc_code']  
        if od_ifsc_code=="":
            od_ifsc_code=None

        od_swift_code=request.POST['od_swift_code']
        if od_swift_code=="":
            od_swift_code=None

        od_bank_name=request.POST['od_bank_name']
        if od_bank_name=="":
            od_bank_name=None

        od_branch=request.POST['od_branch']
        od_SA_cheque_bk=request.POST['od_SA_cheque_bk']
        od_Echeque_p=request.POST['od_Echeque_p']






        mname=request.POST['mname']
        address=request.POST['address']
        country=request.POST['country']
        state=request.POST['state']

        pincode=request.POST['pincode']
        if pincode=="":
            pincode=None

        pan_no=request.POST['pan_no']
        if pan_no=="":
            pan_no=None

        registration_type=request.POST['registration_type']    

        gst_uin=request.POST['gst_uin']
        if gst_uin=="":
            gst_uin=None

        set_alter_gstdetails=request.POST['set_alter_gstdetails']

        statutory_details=request.POST['statutory_details']

        type_of_ledger=request.POST['type_of_ledger']
        rounding_method=request.POST['rounding_method']
        rounding_limit=request.POST['rounding_limit']
        if rounding_limit=="":
            rounding_limit=None
        GST_Applicable=request.POST['GST_Applicable']
        Alter_GST_Details=request.POST['Alter_GST_Details']
        Appropriate=request.POST['Appropriate']
        Types_of_supply=request.POST['Types_of_supply']

        type_duty_tax=request.POST['type_duty_tax']
        tax_type=request.POST['tax_type']
        percentage_of_calcution=request.POST['percentage_of_calcution']
        rond_method=request.POST['rond_method']
        rond_limit=request.POST['rond_limit']
        if rond_limit=="":
            rond_limit=None
        balance_billbybill=request.POST['balance_billbybill']
        credit_period=request.POST['credit_period']
        creditdays_voucher=request.POST['creditdays_voucher']
      




        led=ledgercreation(
            name=name,
            alias=alias,
            under=under,
            bank_details=bank_details,
            ac_holder_nm=ac_holder_nm,
            acc_no=acc_no,
            ifsc_code=ifsc_code,
            swift_code=swift_code,
            bank_name=bank_name,
            branch=branch,
            SA_cheque_bk=SA_cheque_bk,
            Echeque_p=Echeque_p,
            mname=mname,
            address=address,
            country=country,
            state=state,
            pincode=pincode,
            pan_no=pan_no,
            registration_type=registration_type,
            gst_uin=gst_uin,
            set_alter_gstdetails=set_alter_gstdetails,
            type_of_ledger=type_of_ledger,
            rounding_method=rounding_method,
            rounding_limit=rounding_limit,
            GST_Applicable=GST_Applicable,
            Alter_GST_Details=Alter_GST_Details,
            Appropriate=Appropriate,
            Types_of_supply=Types_of_supply,
            type_duty_tax=type_duty_tax,
            tax_type=tax_type,
            percentage_of_calcution=percentage_of_calcution,
            rond_method=rond_method,
            rond_limit=rond_limit,
            balance_billbybill=balance_billbybill,
            credit_period=credit_period,
            creditdays_voucher=creditdays_voucher,
            statutory_details=statutory_details,
            occ_set_odl=occ_set_odl,
            occ_acc_no=occ_acc_no,
            occ_bank_name=occ_bank_name,
            occ_ac_holder_nm=occ_ac_holder_nm,
            occ_branch=occ_branch,
            occ_Echeque_p=occ_Echeque_p,
            occ_ifsc_code=occ_ifsc_code,
            occ_SA_cheque_bk=occ_SA_cheque_bk,
            occ_swift_code=occ_swift_code,
            od_ac_holder_nm=od_ac_holder_nm,
            od_acc_no=od_acc_no,
            od_bank_name=od_bank_name,
            od_branch=od_branch,
            od_Echeque_p=od_Echeque_p,
            od_SA_cheque_bk=od_SA_cheque_bk,
            od_ifsc_code=od_ifsc_code,
            od_set_odl=od_set_odl,
            od_swift_code=od_swift_code

        )
        led.save()
        return redirect('ledgerlist')

def nw(request):
    ledi=led.objects.all()
    return render(request,'nw.html',{'ledg':ledi})


    # ......................... Jisha (New Work) ...................

def godown_alt(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        gd=CreateGodown.objects.all()
        return render(request,'godown_alt.html',{'gd':gd,'tally':tally})
    return redirect('/')

def stockgroup_alt(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        und=stockgroupcreation.objects.all()
        return render(request,'stockgroup_alt.html',{'und':und,'tally':tally})
    return redirect('/')

def stockcate_alt(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        cagy=stockcatagorycreation.objects.all()
        return render(request,'stockcate_alt.html',{'cagy':cagy,'tally':tally})
    return redirect('/')

def unitcreate_alt(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request,'unitcreate_alt.html',{'tally':tally})
    return redirect('/')

def load_stock_group(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        # und=stockgroupcreation.objects.all()
        und=stockgroupcreation.objects.filter(company=t_id)
	    # com=Companies.objects.get(id=pk) 
        return render(request,'stock_group_1.html',{'und':und,'tally':tally})
    return redirect('/')

def stock_groupcreation(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        und=stockgroupcreation.objects.all()
        if request.method=='POST':
            name=request.POST['name']
            alias=request.POST['alias']
            under_name=request.POST['under_name']
            quantities=request.POST['quantities']
            stockgrp=stockgroupcreation(name=name,alias=alias,under=under_name,quantities=quantities)
            stockgrp.save()
            return redirect('stock_groupcreation')
        return render(request,'stock_group_1.html',{'und':und,'tally':tally})
    return redirect('/')

def load_stock_catagory(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        cagy=stockcatagorycreation.objects.all()
	    # com=Companies.objects.get(id=pk) 
        return render(request,'stock_catagory.html',{'cagy':cagy,'tally':tally})
    return redirect('/')

def stock_catagory(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        cagy=stockcatagorycreation.objects.all()
        if request.method=='POST':
            name=request.POST['name']
            alias=request.POST['alias']
            under_name=request.POST['under_name']

            stockcagy=stockcatagorycreation(name=name,alias=alias,under=under_name)
            stockcagy.save()
            return redirect('stock_catagory')
        return render(request,'stock_catagory.html',{'cagy':cagy,'tally':tally})
    return redirect('/')

def load_unit_creation(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        u=uqcs.objects.all()
        return render(request,'unit_creation.html',{'u': u,'tally':tally})
    return redirect('/')

def unit_sim(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        u=uqcs.objects.all()
        if request.method=='POST':
            typ=request.POST['type']
            sym=request.POST['symb']
            formal_name=request.POST['fname']
            uqc=request.POST['uqc']
            decimal=request.POST['decimal']
            sim=unit_simple(type=typ,symbol=sym,formal_name=formal_name,uqc=uqc,decimal=decimal)
            sim.save()
            return redirect('unit_sim')
        return render(request,'unit_creation.html',{'u': u,'tally':tally})
    return redirect('/')

def new_uqcs(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            uqc = request.POST['uqc_name']
            uq=uqcs(uqc_name = uqc)
            uq.save()
            return redirect('new_uqcs')
        return render(request,'unit_uqc.html',{'tally':tally})
    return redirect('/')

def load_unit_compound(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        c=unit_simple.objects.all()
        return render(request,'unit_compound.html',{'c':c,'tally':tally})
    return redirect('/')

def unit_com(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        c=unit_simple.objects.all()
        if request.method=='POST':
            typ=request.POST['compound']
            con=request.POST['conversion']
            sunit=request.POST['s_unit']
            funit=request.POST['f_unit']
            comp=unit_compound(typ=typ,f_unit=funit,conversion=con,s_unit=sunit)
            comp.save()
            return redirect('unit_com')
        return render(request,'unit_compound.html',{'c':c,'tally':tally})
    return redirect('/')

def load_stock_item_creation(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        # grp=stockgroupcreation.objects.all()
        grp=stockgroupcreation.objects.filter(company=t_id)
        unt=unit_compound.objects.all()
        u=unit_simple.objects.all()
	    # com=Companies.objects.get(id=pk) 
        return render(request,'stock_item_creation.html',{'grp':grp,'unt':unt,'u':u,'tally':tally})
    return redirect('/')

def stock_items_creation(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        grp=stockgroupcreation.objects.all()
        unt=unit_compound.objects.all()
        u=unit_simple.objects.all()
        if request.method=='POST':
            nm=request.POST['name']
            alias=request.POST['alias']
            under=request.POST['under']
            units=request.POST['units']
            batches=request.POST['batches']
            trackdate=request.POST['trackdate']
            expirydate=request.POST['expirydate']
            gst_applicable=request.POST['gst_applicable']
            set_alter=request.POST['set_alter']
            typ_sply=request.POST['typ_sply']
            rate_of_duty=request.POST['rate_of_duty']
            quantity=request.POST['quantity']
            rate=request.POST['rate']
            per=request.POST['per']
            value=request.POST['value']
            
            crt=stock_itemcreation(name=nm,alias=alias,under=under,units=units,batches=batches,trackdate=trackdate,expirydate=expirydate,typ_sply=typ_sply,
            gst_applicable=gst_applicable,set_alter=set_alter,rate_of_duty=rate_of_duty,quantity=quantity,rate=rate,per=per,value=value)
            crt.save()
            return redirect('load_stock_item_creation')
        return render(request,'stock_item_creation.html',{'grp':grp,'unt':unt,'u':u,'tally':tally})
    return redirect('/')
    
def stock_accuracy(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        gd=CreateGodown.objects.all()
        return render(request,'stock_accuracy.html',{'gd':gd,'tally':tally})
    return redirect('/')

def stock_accuracy1(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        gd=CreateGodown.objects.all()
        return render(request,'stock_accuracy1.html',{'gd':gd,'tally':tally})
    return redirect('/')

def stock_accuracy2(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        gd=CreateGodown.objects.all()
        return render(request,'stock_accuracy2.html',{'gd':gd,'tally':tally})
    return redirect('/')

def load_company_price(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        pr=Price_level.objects.all()
        return render(request,'company_price.html',{'pr':pr,'tally':tally})
    return redirect('/')

def price_levels(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        pr=Price_level.objects.all()
        if request.method=="POST":
            number=request.POST['number']
            crt=Price_level(number=number)
            crt.save()
            return redirect('price_levels')
        return render(request,'company_price.html',{'pr':pr,'tally':tally})
    return redirect('/')

def load_pan_cin(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request,'pan_cin_1.html',{'tally':tally})
    return redirect('/')

def pan_cin(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            pan=request.POST['pan']
            cin=request.POST['cin']
            crt=pancin(pan=pan,cin=cin)
            crt.save()
        return render(request,'pan_cin_1.html',{'tally':tally})
    return redirect('/')

def godown_creation(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        gd=CreateGodown.objects.all()
	    # com=Companies.objects.get(id=pk) 
        return render(request,'godown.html',{'gd':gd,'tally':tally})
    return redirect('/')

def godown(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        gd=CreateGodown.objects.all()
        if request.method=='POST':
            name=request.POST['name']
            alias=request.POST['alias']
            under_name=request.POST['under_name']
            gdcrt=CreateGodown(name=name,alias=alias,under_name=under_name)
            gdcrt.save()
            return redirect('godown')
        return render(request,'godown.html',{'gd':gd,'tally':tally})
    return redirect('/')  

def load_rev(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request,'revised.html',{'tally':tally})
    return redirect('/')

def revised(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            appl_from=request.POST['appl_from']
            r=revised_applicability(appl_from=appl_from)
            r.save()
            return redirect('revised')
        return render(request,'revised.html',{'tally':tally})
    return redirect('/')

def load_rev_c(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request,'revised_composition.html',{'tally':tally})
    return redirect('/')

def revised_composition(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            appl_from_composition=request.POST['appl_from_composition']
            re=revised_applicability_composition(appl_from_c=appl_from_composition)
            re.save()
            return redirect('revised_composition')
        return render(request,'revised_composition.html',{'tally':tally})
    return redirect('/')

def gst_stock_item(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request,'gst_stock_item.html',{'tally':tally})
    return redirect('/')

def gst_stock(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            calc_typ=request.POST['calc_typ']
            taxability=request.POST['taxability']
            g=gst_stockitem(taxability=taxability,calc_typ=calc_typ)
            g.save()
            return redirect('gst_stock')
        return render(request,'gst_stock_item.html',{'tally':tally})
    return redirect('/')

def load_tds(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request,'tds_details.html',{'tally':tally})
    return redirect('/')

def tds_d(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            tan_reg_no=request.POST['tan_reg_no']
            acc_no=request.POST['acc_no']
            d_typ=request.POST['d_typ']
            d_branch=request.POST['d_branch']
            set_alter=request.POST['set_alter']
            it_tds=request.POST['it_tds']
            act_tds=request.POST['act_tds']
            t=Tds_Details(tan_regno=tan_reg_no,tan=acc_no,deductor_type=d_typ,deductor_branch=d_branch,person_details=set_alter,ignore_it=it_tds,active_tds=act_tds)
            t.save()
            return redirect('tds_d')
        return render(request,'tds_details.html',{'tally':tally})
    return redirect('/')

def load_person_res(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request,'person_res.html',{'tally':tally})
    return redirect('/')

def person_res(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            name=request.POST['name']
            son=request.POST['son']
            designation=request.POST['designation']
            pan=request.POST['pan']
            flat_no=request.POST['flat_no']
            name_bul=request.POST['name_bul']
            road=request.POST['road']
            location=request.POST['location']
            city=request.POST['city']
            state=request.POST['state']
            pincode=request.POST['pincode']
            mob_no=request.POST['mob_no']
            std=request.POST['std']
            tele_phn=request.POST['tele_phn']
            email=request.POST['email']
            p=tds_person(name=name,son_daughter=son,designation=designation,pan=pan,flat_no=flat_no,building=name_bul,street=road,area=location,town=city,
            state=state,pincode=pincode,mobile=mob_no,std=std,telephone=tele_phn,email=email)
            p.save()
            return redirect('person_res')
        return render(request,'person_res.html',{'tallt':tally})
    return redirect('/')

def load_gst_d(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request,'gst_d.html',{'tally':tally})
    return redirect('/')

def gst_d(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            state=request.POST['state']
            reg_typ=request.POST['reg_typ']
            assess_of_teritory=request.POST['assess_of_teritory']
            gst_application=request.POST['gst_application']
            uin=request.POST['uin']
            periodicity=request.POST['periodicity']
            flood_access=request.POST['flood_access']
            applicable_from=request.POST['applicable_from']
            set_alter=request.POST['set_alter']
            tax_liability_advance=request.POST['tax_liability_advance']
            tax_liability_reverse=request.POST['tax_liability_reverse']
            gst_clss=request.POST['gst_clss']
            lut_but=request.POST['lut_but']
            tax_cal=request.POST['tax_cal']
            tax_rate_turnover=request.POST['tax_rate_turnover']
            tax_rate_purchase=request.POST['tax_rate_purchase']
            e_way_bill=request.POST['e_way_bill']
            appl_from=request.POST['appl_from']
            th_limlit_in=request.POST['th_limlit_in']
            th_limit=request.POST['th_limit']
            appl_intrastate=request.POST['appl_intrastate']
            thr_limit=request.POST['thr_limit']
            p_e_way=request.POST['p_e_way']
            e_invoice=request.POST['e_invoice']
            appli_frm=request.POST['appli_frm']
            bill_from_place=request.POST['bill_from_place']
            period_report=request.POST['period_report']
            send_eway_bill=request.POST['send_eway_bill']
            g=GST(state=state,reg_type=reg_typ,assessee=assess_of_teritory,gst_applicable=gst_application,gstin=uin,periodicity=periodicity,flood_cess=flood_access,
            applicable_from=applicable_from,gst_rate_details=set_alter, advance_receipts= tax_liability_advance,reverse_charge=tax_liability_reverse,
            gst_classification=gst_clss,bond_details=lut_but,tax_calc=tax_cal,tax_rate=tax_rate_turnover,tax_purchase=tax_rate_purchase, eway_bill=e_way_bill,
            applicable_form=appl_from,threshold_includes=th_limlit_in,threshold_limit=th_limit,intrastate=appl_intrastate,threshold_limit2=thr_limit, print_eway= p_e_way,e_invoice=e_invoice,
            app_from=appli_frm,billfrom_place=bill_from_place,dperiod=period_report,send_ewaybill=send_eway_bill)
            g.save()
            return redirect('gst_d')
        return render(request,'gst_d.html',{'tally':tally})
    return redirect('/')

def load_lut_bond(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request,'lut_bond A.html',{'tally':tally})
    return redirect('/')

def lutbond(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            lut_no=request.POST['lut_no']
            appl_from=request.POST['appl_frm']
            appl_to=request.POST['appl_to']
            l=gst_lutbond(lutbond=lut_no,validity_from=appl_from,validity_to=appl_to)
            l.save()
            return redirect('lutbond')
        return render(request,'lut_bond A.html',{'tally':tally})
    return redirect('/')

def load_gst_details_c(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request,'gst_details_c.html',{'tally':tally})
    return redirect('/')

def gst_details_c(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            taxability=request.POST['taxability']
            tax=request.POST['tax']
            cess=request.POST['cess']
            kerela_fc=request.POST['flood_cess']
            g=gst_taxability(taxability=taxability,integrated_tax=tax,cess=cess,flood_cess=kerela_fc)
            g.save()
            return redirect('gst_details_c')
        return render(request,'gst_details_c.html',{'tally':tally})
    return redirect('/')

def aaa(request):
    return render(request,'aaa.html')
def aa1(request):
    return render(request,'aa1.html')

# NIYAS 

# def stock_group(request):
#     und=CreateStockGrp.objects.all()
#     if 't_id' in request.session:
#         if request.session.has_key('t_id'):
#             t_id = request.session['t_id']
#         else:
#             return redirect('/')
#         if request.method=='POST':
#             # company=Companies.objects.get(id=request.companycreate)
#             company=Companies.objects.get(id=t_id)
#             name=request.POST['name']
#             alias=request.POST['alias']
#             under_name=request.POST['under_name']
#             quantities=request.POST['quantities']
#             stockgrp=CreateStockGrp(name=name,alias=alias,under_name=under_name,quantities=quantities,comp=company)
#             stockgrp.save()
#             return redirect('stock_group')
#         return render(request,'stock_group.html',{'und':und})
#     return redirect("/")

def stock_group(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        und=stockgroupcreation.objects.all()
        if request.method=='POST':
            name=request.POST['name']
            alias=request.POST['alias']
            under_name=request.POST['under_name']
            quantities=request.POST['quantities']
            stockgrp=stockgroupcreation(name=name,alias=alias,under=under_name,quantities=quantities,company_id=t_id)
            stockgrp.save()
            return redirect('stock_group')
        return render(request,'stock_group_1.html',{'und':und,'tally':tally})
    return redirect('/')

def stock_group_secondary(request):
    # company=Companies.objects.all()
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
            und=CreateStockGrp.objects.filter(comp=t_id)
        else:
            return redirect('/')
        if request.method=='POST':
            
            # company=Companies.objects.get(id=request.companycreate)
            company=Companies.objects.get(id=t_id)
            name=request.POST['name']
            alias=request.POST['alias']
            under_name=request.POST['under_name']
            quantities=request.POST['quantities']
            stockgrp=CreateStockGrp(name=name,alias=alias,under_name=under_name,quantities=quantities,comp=company)
            stockgrp.save()
            return redirect('stock_group')
        return render(request,'stock_group(secondary).html',{'und':und})
    return redirect("/")

def unit_creation(request):
    unit=UnitCrt.objects.all()
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        if request.method=='POST':
            company=Companies.objects.get(id=t_id)
            type=request.POST['type']
            symbol=request.POST['symbol']
            formal_name=request.POST['formal_name']
            crt=UnitCrt(type=type,symbol=symbol,formal_name=formal_name,comp=company)
            crt.save()
        return render(request,'unit1.html',{'unit':unit})
    return redirect("/")

def unit_creation_secondary(request):
    unit=UnitCrt.objects.all()
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        if request.method=='POST':
            company=Companies.objects.get(id=t_id)
            type=request.POST['type']
            symbol=request.POST['symbol']
            formal_name=request.POST['formal_name']
            crt=UnitCrt(type=type,symbol=symbol,formal_name=formal_name,comp=company)
            crt.save()
        return render(request,'unit_creation(secondary).html',{'unit':unit})
    return redirect("/")

def createcategory(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cat=CreateStockCateg.objects.filter(id=t_id)
        con={'cat':cat} 
        return render(request, 'createcategory.html',con) 
    return redirect("/")

def savestockcategory(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        if request.method=='POST':
            company=Companies.objects.get(id=t_id)
            catname=request.POST['name']
            abr=request.POST['alias']
            cat=request.POST.get('u')
            sc=CreateStockCateg(name=catname,alias=abr,under_name=cat,comp=company)
            sc.save()
        return redirect('catgroupsummary')
    return redirect("/")

def catgroupsummary(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
            cat=CreateStockCateg.objects.filter(id=t_id)
        else:
            return redirect('/')
        # cat=CreateStockCateg.objects.filter(id=t_id)
        con={'cat':cat} 
        return render(request,'catgroupsummary.html',con)
    return redirect("/")

def liststockgroupviews(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        # data=stockgroupcreation.objects.all()
        data=stockgroupcreation.objects.filter(company=t_id)
        context={'data':data}
        return render(request, 'liststockgroup.html',context)

def stock_items(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cat=CreateStockCateg.objects.filter(id=t_id)
        # cat=CreateStockCateg.objects.all()
        grp=CreateStockGrp.objects.filter(id=t_id)
        unt=UnitCrt.objects.filter(id=t_id)
        company=Companies.objects.get(id=t_id)
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        category=request.POST['category']
        units=request.POST['units']
        batches=request.POST['batches']
        manufacturing_date=request.POST['manufacturing_date']
        expiry_dates=request.POST['expiry_dates']
        rate_of_duty=request.POST['rate_of_duty']
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        per=request.POST['per']
        value=request.POST['value']
        additional=request.POST['additional']
        crt=stock_item_crt(name=name,alias=alias,under=under,category=category,units=units,batches=batches,
                           manufacturing_date=manufacturing_date,expiry_dates=expiry_dates,
                           rate_of_duty=rate_of_duty,quantity=quantity,rate=rate,per=per,value=value,additional=additional,comp=company)
        crt.save()
    return render(request,'stock_items.html',{'cat':cat,'grp':grp,'unt':unt})

def liststockviews(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        # data=stock_itemcreation.objects.all()
        data=stock_itemcreation.objects.filter(company=t_id)
        context={'data':data}
        return render(request, 'liststock.html',context)

def godown_secondary(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
            gd=stock_item_crt.objects.filter(comp=t_id)
        else:
            return redirect('/')
        # gd=CreateGodown.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        company=Companies.objects.get(id=t_id)   
        gdcrt=CreateGodown(name=name,alias=alias,under_name=under_name,comp=company)
        gdcrt.save()
    return render(request,'godown(secondary).html',{'gd':gd})

def singlestockgroupanalysisview(request,pk):
    data1=stockgroupcreation.objects.get(id=pk)
    itm=data1.id
    data2=stock_itemcreation.objects.all()
    # data=analysis_view.objects.filter(particular=data2)
    data=analysis_view.objects.filter(particular = itm)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    for a in data:
        sum1 += a.iquantity
    for b in data:
        sum2 += b.ieff_rate
    for c in data:
        sum3 += c.ivalue
    for d in data:
        sum4 += d.oquantity
    for e in data:
        sum5 += e.oeff_rate
    for f in data:
        sum6 += f.ovalue
    context={'data':data,'data1':data1,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum5':sum5,'sum6':sum6}
    return render(request, 'singlestockgroupanalysis.html',context)

def itemmovementanalysisview(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
            data1=purchase_model.objects.filter(comp=t_id)
            data2=sale_model.objects.filter(comp=t_id)
        else:
            return redirect('/')
        # data1=purchase_model.objects.all()
        # data2=sale_model.objects.all()
        context={'data1':data1,'data2':data2}
        return render(request, 'itemmovementanalysis.html',context)
    return redirect("/")

def purchasevoucheranalysisview(request,pk):
    data=purchase_model.objects.get(id=pk)
    context={'data':data}
    return render(request, 'purchasevoucheranalysis.html',context)

def salevoucheranalysisview(request,pk):
    data=sale_model.objects.get(id=pk)
    context={'data':data}
    return render(request, 'salevoucheranalysis.html',context)

def querystockview(request,pk):
    data=stock_itemcreation.objects.get(id=pk)
    ndata=CreateGodown.objects.all()
    total_sum = 0
    purchase=purchase_model.objects.filter(itm=data)
    sale=sale_model.objects.filter(itm=data)
    cat=CreateStockCateg.objects.filter(name=data)    
    context={'data':data,'ndata':ndata,'purchase':purchase,'sale':sale,'cat':cat}
    return render(request, 'querystocks.html',context)

def stockgroupanalysisview(request):
    data=analysis_view.objects.all()
    sum1 = 0
    sum2 = 0
    for a in data:
        sum1 += a.ivalue
    for b in data:
        sum2 += b.ovalue
    context={'data':data,'sum1':sum1,'sum2':sum2}
    return render(request, 'stockgroupanalysis.html',context)

# noufal 

def ledgercreate(request):
    data=ledgercreatemodel.objects.all()
    cnt=countrymodel.objects.all()
    st=statemodel.objects.all()
    context={'data':data,'cnt':cnt,'st':st}
    return render(request,'ledgercreate.html',context)

def createledgerviews(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
    if request.method=='POST':
        lpname=request.POST['name']
        lpalias=request.POST['alias']
        lpunder=request.POST['under']
        lpmname=request.POST['mname']
        lpaddress=request.POST['address']
        lpstate=request.POST['state']
        lpcountry=request.POST['contry']
        lppincode=request.POST['pincode']
        lpbank=request.POST['bank']
        lppan=request.POST['pan']
        lpreg=request.POST['registrations']
        company=Companies.objects.get(id=t_id) 
        data=ledgercreatemodel(lname=lpname,lalias=lpalias,
                                lunder=lpunder,lmname=lpmname,
                                laddress=lpaddress,lstate=lpstate,
                                lcountry=lpcountry,lpincode=lppincode,
                                lbank=lpbank,lpan=lppan,lreg=lpreg,comp=company)
        data.save()
        return redirect('ledgercreate')

def selectledgerpage(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
    # data=tally_ledger.objects.all()
    data=tally_ledger.objects.filter(company=t_id)
    context={'data':data}
    return render(request,'selectledger.html',context)

def ledgerpage(request,pk):
    ndata=tally_ledger.objects.get(id=pk)
    data=ledgeranalysismodel.objects.filter(lpert=ndata)
    sum1=0
    sum2=0
    for a in data:
        sum1+=a.lpvalue
    for b in data:
        sum2+=b.svalue
    return render(request,'ledgeranalisys.html',{'data':data,'sum1':sum1,'sum2':sum2})


def ledgeritem(request,pk):
    ndata=ledgeranalysismodel.objects.get(id=pk)
    data=purchaseledgervouchermodel.objects.filter(lstockitem=ndata)
    sdata=salesledgervouchermodel.objects.filter(lstockitem=ndata)
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    for a in data:
        sum1+=a.lquantity
    for b in data:
        sum2+=b.lbasicrate
    for c in data:
        sum3+=c.lbasicvalue
    for d in data:
        sum4+=d.laddlcost
    for e in data:
        sum5+=e.ltotalvalue
    for f in data:
        sum6+=f.lefsrate
    sum7=0
    sum8=0
    sum9=0
    sum10=0
    sum11=0
    sum12=0
    for g in sdata:
        sum7+=g.lquantity
    for h in sdata:
        sum8+=h.lbasicrate
    for i in sdata:
        sum9+=i.lbasicvalue
    for j in sdata:
        sum10+=j.laddlcost
    for k in sdata:
        sum11+=k.ltotalvalue
    for l in sdata:
        sum12+=l.lefsrate
    return render(request,'ledgeritem.html',{'data':data,'ndata':ndata,'sdata':sdata,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum5':sum5,'sum6':sum6,'sum7':sum7,'sum8':sum8,'sum9':sum9,'sum10':sum10,'sum11':sum11,'sum12':sum12})

def grouppage(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        # data=tally_group.objects.all()
        data=tally_group.objects.filter(company=t_id)
        context={'data':data}
        return render(request,'selectgroup.html',context)

def Create_Group(request):
    data=tally_group.objects.all()
    context={'data':data}
    return render(request,'groupcreate.html',context)

def creategroupviews(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
            gd=stock_item_crt.objects.filter(comp=t_id)
        else:
            return redirect('/')
    if request.method=='POST':
        gpname=request.POST['name']
        gpalias=request.POST['alias']
        gpunder=request.POST['under']
        gpbehaves=request.POST['behaves']
        gpallocate=request.POST['allocate']  
        data=groupcreatemodel(gname=gpname,galias=gpalias,gunder=gpunder,gbehaves=gpbehaves,gallocate=gpallocate)
        data.save()
        return redirect('grouppage')

def groupanalisys(request,pk):
    ndata=tally_group.objects.get(id=pk)
    data=groupanalysismodel.objects.filter(pert=ndata)
    sum1=0
    sum2=0
    for a in data:
        sum1+=a.pvalue
    for b in data:
        sum2+=b.svalue
    context={'data':data,'sum1':sum1,'sum2':sum2}
    return render(request,'groupanalisys.html',context)

def groupitem(request,pk):
    ndata=groupanalysismodel.objects.get(id=pk)
    data=purchasevouchermodel.objects.filter(stockitem=ndata)
    sdata=salevouchermodel.objects.filter(stockitem=ndata)
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    for a in data:
        sum1+=a.quantity
    for b in data:
        sum2+=b.basicrate
    for c in data:
        sum3+=c.basicvalue
    for d in data:
        sum4+=d.addlcost
    for e in data:
        sum5+=e.totalvalue
    for f in data:
        sum6+=f.efsrate
    sum7=0
    sum8=0
    sum9=0
    sum10=0
    sum11=0
    sum12=0
    for g in sdata:
        sum7+=g.quantity
    for h in sdata:
        sum8+=h.basicrate
    for i in sdata:
        sum9+=i.basicvalue
    for j in sdata:
        sum10+=j.addlcost
    for k in sdata:
        sum11+=k.totalvalue
    for l in sdata:
        sum12+=l.efsrate
    return render(request,'groupitem.html',{'data':data,'ndata':ndata,'sdata':sdata,
                                            'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,
                                            'sum5':sum5,'sum6':sum6,'sum7':sum7,'sum8':sum8,
                                            'sum9':sum9,'sum10':sum10,'sum11':sum11,'sum12':sum12})




# payroll masters #praveen

def employe_category(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)

        return render(request,'employe_category.html',{'tally':tally})   
    return redirect('/')
    

def employe_category_secondary(request):
    return render(request,'employe_category_secondary.html')   

def employe_category_form(request):
    
    if request.method == 'POST':
        name= request.POST['name']
        alias = request.POST['alias']
        relocate = request.POST['locate']
        relocate= request.POST['locate2']

        std= emp_category(
            cat_name =name,
            cat_alias=alias,
            revenue_items=relocate,
            non_revenue_items=relocate,   
        )
        std.save()
       # messages.success(request,'employee group add successfully !!!')
        return redirect('emp_grp')
    return render(request,'employe_category.html')

def emp_grp(request):
    

    std=Create_employeegroup.objects.all()
    empc=emp_category.objects.all()

    return render(request,'employegroup.html',{'std':std,'empc':empc})


def addemp_group(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    empc=emp_category.objects.all()
    if request.method == 'POST':
        name= request.POST['name']
        alias = request.POST['alias']
        under = request.POST['under']
        sal= request.POST['sal']

        std= Create_employeegroup(
            name =name,
            alias=alias,
            under=under,
            define_salary=sal,   
            company_id=t_id,)
        std.save()
       # messages.success(request,'employee group add successfully !!!')
        return redirect('emp_grp')
    return render(request,'employegroup.html',{'tally':tally,'empc':empc})


def emp_grp2(request):
    std=Create_employeegroup.objects.all()
    return render(request,'employegroup_secondary.html',{'std':std})


def employee(request):
    std=Create_employeegroup.objects.all()
    return render(request,'employe.html',{'std':std})  

def uqcform(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        uqname= request.POST['uqcname']
        u=unitQuantityCode(new_uqc=uqname)
        u.save()
    return render(request,'uqcform.html',{'tally':tally})   


def addemployee(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        
        namee = request.POST['name']
        aliass = request.POST['alias']
        underr = request.POST['under']
        join = request.POST['join']
        sal = request.POST['sal']
        empname = request.POST['empname']
        desig = request.POST['desig']
        fn = request.POST['fn']
        loc = request.POST['loc']
        gen = request.POST['gen']
        dob = request.POST['dob']
        bloodd = request.POST['blood']
        prnts = request.POST['prnts']
        spouse = request.POST['spouse']
        adrs = request.POST['adrs']
        phone = request.POST['phone']
        email = request.POST['email']
        taxno = request.POST['taxno']
        aadhar = request.POST['aadhar']
        uan = request.POST['uan']
        pfn = request.POST['pfn']
        pran = request.POST['pran']
        esin = request.POST['esin']
        bank = request.POST['bank']
        #Bank
        
        acount=request.POST['acount']
        ifsc_code=request.POST['ifsc']
        bankname=request.POST['bank_name']
        branch=request.POST['branch_name']
        transaction_type=request.POST['Transaction_type']
        #E-found transfer
        acount_num=request.POST['acnumber']
        ifsc=request.POST['ifsccode']
        bankname2=request.POST['bank_name2']
        cheque=request.POST['cheque']


        
        
        std = Employee(

            name =namee,
            alias=aliass,
            under=underr,
            date_join=join,
            defn_sal =sal,
            emp_name = empname,
            emp_desg=desig ,
            fnctn = fn,
            location =loc,
            gender =gen,
            dob =dob,
            blood=bloodd,
            parent_name =prnts,
            spouse_name = spouse,
            address = adrs,
            number = phone,
            email = email,
            inc_tax_no = taxno,
            aadhar_no = aadhar,
            uan = uan,
            pfn = pfn,
            pran = pran,
            esin = esin,
            bankdtls = bank,
            company_id=t_id, 
            



        )

        std.save()
        idd=std

        std2=add_bank(employee_id=idd,
                      Acount_No=acount,
                      IFSC_code=ifsc_code,
                      Bank_name=bankname,
                      Branch_name=branch,
                      Transaction_type=transaction_type,
        )
        std2.save()

        std3=E_found_trasfer(employee_id=idd,
                             Acount_No=acount_num,
                             IFSC_code=ifsc,
                             Bank_name=bankname2,
                             Cheque=cheque,
                            
        )
        std3.save()
        return render(request,'employe.html')


def addemp_group2(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    std=Create_employeegroup.objects.all()
    if request.method == 'POST':
        name= request.POST['name']
        alias = request.POST['alias']
        under = request.POST['under']
        sal= request.POST['sal']

        std= Create_employeegroup(
            name =name,
            alias=alias,
            under=under,
            define_salary=sal,   
        )
        std.save()
        #messages.success(request,'employee group add successfully !!!')
        return redirect('employee')
    return render(request,'emp_group3.html',{'std':std,'tally':tally})   


def salary1(request):
    
    pk=create_payhead.objects.all()
    if request.method=='POST':
        name1=request.POST['name']
        under=request.POST['under']
        effect=request.POST['effective']
        pay=request.POST['payhead']
        rate=request.POST['rate']
        per=request.POST['per']
        payhead=request.POST['payheaad_type']
        calculation=request.POST['calculation_type']
        #save salary
        std=salary(name=name1,
                   under=under,
                   effective=effect,
                   payhead=pay,
                   rate=rate,
                   per=per,
                   pay_type=payhead,
                   cal_type=calculation,
        )
        std.save()
        return redirect('salary1')
    return render(request,'salary.html',{'pk':pk}) 

def load(request):
    did=request.GET.get("id")
    obj=create_payhead.objects.get(name=did)
    return render(request,"load.html",{"obj":obj})

def load_calculation(request):
    did=request.GET.get("id")
    obj=create_payhead.objects.get(name=did)
    return render(request,"load_calculation.html",{"obj":obj})

def payhead2(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           
        )
        std.save()
        idd=std

        std2=compute_information(Pay_head_id=idd,
                                 compute=compute,
                                 effective_from=effective_from,
                                #  amount_greater=amount_greaterthan,
                                 amount_upto=amount_upto,
                                 value=value,
        )
        std2.save()

        std3=Rounding(pay_head_id=idd,
                     Rounding_Method=round_method,
                     Round_limit=limit,
        )
        std3.save()

        std4=gratuity(pay_head_id=idd,
                     days_of_months=days_of_months,
                     number_of_months_from=from_date,
                     to=to,
                     calculation_per_year=calculation_per_year,
        )
        std4.save()
        messages.success(request,'successfully Added !!!')
        return redirect('salary1')
    return render(request,'payhead_secondary.html')     


def stunits(request):   
    uq=unitQuantityCode.objects.all()
    ps=units.objects.all()
    return render(request,'stunits.html',{'ps':ps,'uq':uq}) 

def stunits2(request):
    ps=units.objects.all()
    uq=unitQuantityCode.objects.all()
    return render(request,'stunits2.html',{'ps':ps,'uq':uq}) 

def add_units(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        std=units()
        std.type=request.POST.get('type')
        std.symbol=request.POST.get('symbol')  
        std.formal_name=request.POST.get('formal')
        std.uqc1=request.POST.get('uqc1')
        std.number_of_decimal_places=request.POST.get('decimal') 
        std.first_unit=request.POST.get('ft')
        std.conversion=request.POST.get('con')
        std.second_unit=request.POST.get('sec')
        std.company_id=t_id 
        std.save()
        print('hai')
        return redirect('stunits')
    return render(request,'stunits2.html',{'tally':tally}) 


def attendence(request):
    std=Create_attendence.objects.all()
    pk=units.objects.all()
    return render(request,'attendence.html',{'std':std,'pk':pk})   

def emp_attendence(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method == 'POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        type=request.POST['type']
        period=request.POST['period']
        units1=request.POST['units']
        
        std=Create_attendence(
            name =name,
            alias=alias,
            under=under,
            type=type,
            period=period,
            units=units1,
            company_id=t_id,)
        std.save()
        messages.success(request,'successfully Added !!!')
        return redirect('attendence')
    return render(request,'attendence.html',{'tally':tally})  

def attendence2(request):
    std=Create_attendence.objects.all()
    pk=units.objects.all()
    return render(request,'attendence_secondary.html',{'std':std,'pk':pk}) 

def add_payhead(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           company_id=t_id,
        )
        std.save()
        idd=std

        std2=compute_information(Pay_head_id=idd,
                                 compute=compute,
                                 effective_from=effective_from,
                                #  amount_greater=amount_greaterthan,
                                 amount_upto=amount_upto,
                                 value=value,
        )
        std2.save()

        std3=Rounding(pay_head_id=idd,
                     Rounding_Method=round_method,
                     Round_limit=limit,
        )
        std3.save()

        std4=gratuity(pay_head_id=idd,
                     days_of_months=days_of_months,
                     number_of_months_from=from_date,
                     to=to,
                     calculation_per_year=calculation_per_year,
        )
        std4.save()
        messages.success(request,'successfully Added !!!')
        return redirect('payheads')
    return render(request,'payheads.html',{'tally':tally})   


def payheads(request):
    ph=Create_attendence.objects.filter(type="Attendance/Leave with pay")
    ph2=Create_attendence.objects.filter(type="Production")
    std=Create_attendence.objects.all()
    return render(request,'payheads.html',{'std':std,'ph':ph,'ph2':ph2})   


def payvoucher(request):
    return render(request,'payroll.html')   

def add_voucher(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method == 'POST':
        Vname = request.POST['name']
        alias = request.POST['alias']
        vtype = request.POST['type']
        abbre = request.POST['abber']
        activ_vou_typ = request.POST['active']  
        meth_vou_num = request.POST['numbering']
        useadv = request.POST.get('config', False)
        prvtdp = request.POST.get('prevent', False)
       
        use_effct_date = request.POST['effect']  
        allow_zero_trans = request.POST['trans']  
        allow_naration_in_vou = request.POST['narr']  
        optional = request.POST['optical'] 
        provide_narr = request.POST['ledg']  
        print = request.POST['print']  
        
        std = create_VoucherModels(voucher_name=Vname ,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_effective_date=use_effct_date,
            use_adv_conf = useadv,
            prvnt_duplictes =prvtdp,
            allow_zero_value_trns=allow_zero_trans,
            allow_naration_in_voucher=allow_naration_in_vou,
            make_optional=optional,
            provide_naration=provide_narr,
            print_voucher=print,
            company_id=t_id,
        )
        std.save()
        return redirect('payvoucher')

    return render(request, 'payroll.html',{'tally':tally})  

def employe_category(request):
    return render(request,'employe_category.html')   

def employe_category_secondary(request):
    
    return render(request,'employe_category_secondary.html')   

def employe_category_form(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method == 'POST':
        name= request.POST['name']
        alias = request.POST['alias']
        relocate = request.POST['locate']
        relocate= request.POST['locate2']

        std= emp_category(
            cat_name =name,
            cat_alias=alias,
            revenue_items=relocate,
            non_revenue_items=relocate,   
        )
        std.save()
       # messages.success(request,'employee group add successfully !!!')
        return redirect('emp_grp')
    return render(request,'employe_category_secondary.html',{'tally':tally})



def emp_grp1(request):
    
    return render(request,'employegroup2.html')     





 

def pan2(request):
    return render(request,'pan.html')  

def attendence1(request):
    data=Create_attendence1.objects.all()
    return render(request,'attendence2.html',{'p':data})

def unit2(request):
    return render(request,'unit2.html')

def payroll1(request):
    return render(request,'load_payroll.html')



    #employeegroup


def emp_grp2_2(request):
    data=empgroup2.objects.all()
    return render(request,'create_employegroup.html',{'p':data})  


def emp_add(request):
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        
        tut=empgroup2(groupname=name,groupalias=alias,groupunder=under)
        
        tut.save()
       

        return redirect('emp_add2')
    return render(request,'employegroup2.html')   

def emp_add2(request):
    emp=empgroup2.objects.all()
    return render(request,'employegroup2.html',{'data':emp})  

def emp_gredit(request,pk):
    data=empgroup2.objects.get(id=pk)
    data2=empgroup2.objects.all()
    context={'p':data,
    'p2':data2}
    return render(request,'gredit.html',context) 

def emp_gredit2(request,pk):
    if request.method=='POST':
        datas=empgroup2.objects.get(id=pk)
        datas.groupname =request.POST.get('name')
        datas.groupalias = request.POST.get('alias')
        datas.groupunder = request.POST.get('under')
        

        datas.save()
        return redirect('emp_add2')




  





    #payheads



def payheads1(request):
    data=create_payhead1.objects.all()
    return render(request,'payheads2.html',{'p':data})  

def payheads2(request):
    data=Create_attendence1.objects.all()
    return render(request,'load_payheads.html',{'p':data})   


def add_payheads(request):
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']
       

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        slabtype=request.POST['slab_type']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead1(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           
        )
        std.save()
        idd=std

        std2=compute_information1(Pay_head_id=idd,
                                 compute=compute,
                                 effective_from=effective_from,
                                #  amount_greater=amount_greaterthan,
                                 amount_upto=amount_upto,
                                 slab_type=slabtype,
                                 value=value,
        )
        std2.save()

        std3=Rounding1(pay_head_id=idd,
                     Rounding_Method=round_method,
                     Round_limit=limit,
        )
        std3.save()

        std4=gratuity1(pay_head_id=idd,
                     days_of_months=days_of_months,
                     number_of_months_from=from_date,
                     to=to,
                     calculation_per_year=calculation_per_year,
        )
        std4.save()
        messages.success(request,'successfully Added !!!')
        return redirect('payheads1')


def payhead_edit2(request,pk):
    if request.method=='POST':
        data=create_payhead1.objects.get(id=pk)
        data.name=request.POST.get('name')
        data.alias=request.POST.get('alias')
        data.pay_type=request.POST.get('payhead')
        data.income_type=request.POST.get('income')
        data.under=request.POST.get('under')
        data.affect_net=request.POST.get('netsalary')
        data.payslip=request.POST.get('payslip')
        data.calculation_of_gratuity=request.POST.get('caltype')
        data.cal_type=request.POST.get('ctype')
        data.calculation_period=request.POST.get('caltype')
        data.leave_withpay=request.POST.get('attendence with pay')
        data.leave_with_out_pay=request.POST.get('Attendance with out pay')
        data.production_type=request.POST.get('ptype')
        data.opening_balance=request.POST.get('balance')
        data.save()

        idd=data

        data2=compute_information1.objects.get(id=pk)
        data2.compute=request.POST.get('compute')
        data2.effective_from=request.POST.get('effective_from')
        data2.amount_upto=request.POST.get('amount_upto')
        data2.slab_type=request.POST.get('slab_type')
        data2.value=request.POST.get('value')
        data2.Pay_head_id=idd

        data2.save()


        data3=Rounding1.objects.get(id=pk)
        data3.Rounding_Method=request.POST.get('roundmethod')
        data3.Round_limit=request.POST.get('limit')
        data3.pay_head_id=idd
        data3.save()

        data4=gratuity1.objects.get(id=pk)
        data4.days_of_months=request.POST.get('days_of_months')
        data4.number_of_months_from=request.POST.get('from')
        data4.to=request.POST.get('to')
        data4.calculation_per_year=request.POST.get('eligiibility')
        data4.pay_head_id=idd
        data4.save()
        return redirect('payheads1')
    return render(request,'payhead_edit.html')
    

def payhead_edit(request,pk):
    data=create_payhead1.objects.get(id=pk)
    data2=compute_information1.objects.get(id=pk)
    data3=Rounding1.objects.get(id=pk)
    data4=gratuity1.objects.get(id=pk)
    context={'p':data,'p2':data2,
    'p3':data3,'p4':data4
    }
    return render(request,'payhead_edit.html',context) 



        
    
    #attendence 



def attendence4(request):
    return render(request,'attendence(sec).html')


def attendence2_2(request):
    data=Create_attendence1.objects.all()
    data2=units1.objects.all()

    context={'p':data,
    'p2':data2}
    return render(request,'load_attendence.html',context)

def attendence3(request):
    if request.method == 'POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        type=request.POST['type']
        
        std=Create_attendence1(
            name =name,
            alias=alias,
            under=under,
            type=type,
           )
        std.save()
        messages.success(request,'successfully Added !!!')
        return redirect('attendence')


def attendence_edit(request,pk):
    data=Create_attendence1.objects.get(id=pk)
    data2=Create_attendence1.objects.all()
    context={'p':data,
    'p2':data2}
    return render(request,'attendence_edit.html',context) 

def attendence_edit2(request,pk):
    if request.method == 'POST':
        data=Create_attendence1.objects.get(id=pk)
        data.name=request.POST.get('name')
        data.alias=request.POST.get('alias')
        data.under=request.POST.get('under')
        data.type=request.POST.get('type')
        data.save()
        return redirect('attendence')



    #employee

def employee1(request):
    p3=Employee1.objects.all()
    context={'data':p3}
    return render(request,'employe2.html',context)   

def employee2(request):
    obj=bank3.objects.all()
    data=Employee1.objects.all()
    data2=empgroup2.objects.all()
    context={'std':data,
    'p':obj,'p3':data2}
    return render(request,'list_of_employe.html',context)

def addemployee1(request):
    if request.method=='POST':
        
        namee = request.POST['name']
        aliass = request.POST['alias']
        underr = request.POST['underr']
        join = request.POST['join']
        sal = request.POST['sal']
        empname = request.POST['empname']
        desig = request.POST['desig']
        fn = request.POST['fn']
        loc = request.POST['loc']
        gen = request.POST['gen']
        dob = request.POST['dob']
        bloodd = request.POST['blood']
        prnts = request.POST['prnts']
        spouse = request.POST['spouse']
        adrs = request.POST['adrs']
        phone = request.POST['phone']
        email = request.POST['email']
        taxno = request.POST['taxno']
        aadhar = request.POST['aadhar']
        uan = request.POST['uan']
        pfn = request.POST['pfn']
        pran = request.POST['pran']
        esin = request.POST['esin']
        bank = request.POST['bank']
        #Bank
        acount=request.POST['acount']
        ifsc_code=request.POST['ifsc']
        bankname=request.POST['bank_name']
        branch=request.POST['branch_name']
        transaction_type=request.POST['Transaction_type']
        #E-found transfer
        acount_num=request.POST['acnumber']
        ifsc=request.POST['ifsccode']
        bankname2=request.POST['bank_name2']
        cheque=request.POST['cheque']


        
        
        std = Employee1(

            name =namee,
            alias=aliass,
            under=underr,
            date_join=join,
            defn_sal =sal,
            emp_name = empname,
            emp_desg=desig ,
            fnctn = fn,
            location =loc,
            gender =gen,
            dob =dob,
            blood=bloodd,
            parent_name =prnts,
            spouse_name = spouse,
            address = adrs,
            number = phone,
            email = email,
            inc_tax_no = taxno,
            aadhar_no = aadhar,
            uan = uan,
            pfn = pfn,
            pran = pran,
            esin = esin,
            bankdtls = bank,
            
            



        )

        std.save()
        idd=std

        std2=add_bank1(employee_id=idd,
                      Acount_No=acount,
                      IFSC_code=ifsc_code,
                      Bank_name=bankname,
                      Branch_name=branch,
                      Transaction_type=transaction_type,
        )
        std2.save()

        std3=E_found_trasfer1(employee_id=idd,
                             Acount_No=acount_num,
                             IFSC_code=ifsc,
                             Bank_name=bankname2,
                             Cheque=cheque 
        )
        std3.save()
        return redirect('employee1')




#payrolvoucher



def add_voucher1(request):
    if request.method == 'POST':
        Vname = request.POST['name']
        alias = request.POST['alias']
        vtype = request.POST['type']
        abbre = request.POST['abber']
        activ_vou_typ = request.POST['active']  
        meth_vou_num = request.POST['numbering']
        useadv = request.POST.get('config', False)
        prvtdp = request.POST.get('prevent', False)
       
        allow_zero_trans = request.POST['trans']  
        print = request.POST['print']  
        
        std = create_VoucherModels1(voucher_name=Vname ,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_adv_conf = useadv,
            prvnt_duplictes =prvtdp,
            allow_zero_value_trns=allow_zero_trans,
            print_voucher=print,

        )
        std.save()
        return redirect('add_voucher2')

    return render(request, 'load_payroll.html')  


def add_voucher2(request):
    emp=create_VoucherModels1.objects.all()
    return render(request,'payroll2.html',{'data':emp}) 

def add_voucher3(request):
    emp=create_VoucherModels1.objects.all()
    return render(request,'load_payroll.html',{'data':emp}) 

def add_voucher_edit(request,pk):
    emp=create_VoucherModels1.objects.get(id=pk)
    data2=create_VoucherModels1.objects.all()
    context={'p':emp,
    'data':data2}
    return render(request,'payrolledit.html',context) 

def add_voucher_edit2(request,pk):
    emp=create_VoucherModels1.objects.get(id=pk)
    emp.voucher_name=request.POST.get('name')
    emp.alias=request.POST.get('alias')
    emp.voucher_type=request.POST.get('type')
    emp.abbreviation=request.POST.get('abber')
    emp.active_this_voucher_type=request.POST.get('active')
    emp.method_voucher_numbering=request.POST.get('numbering')
    emp.use_adv_conf=request.POST.get('config', False)
    emp.prvnt_duplictes=request.POST.get('prevent', False)
    emp.allow_zero_value_trns=request.POST.get('trans')
    emp.provide_naration=request.POST.get('ledg')
    emp.print_voucher=request.POST.get('print')
    emp.save()
    return redirect('add_voucher2')


    #unit




def unit(request):
    p=units1.objects.all()
    return render(request, 'unit.html',{'p2':p})

def unit2(request):
    p=units1.objects.all()
    return render(request,'unit2.html',{'data':p})

def unit3(request):
    p=units1.objects.all()
    return render(request,'unit3.html',{'data':p})

def add_unit(request):
    if request.method=='POST':
        type = request.POST['type']
        symbol = request.POST['symbol']
        formal_name = request.POST['formal']
        number_of_decimal_places = request.POST['decimal']
        first_unit = request.POST['ft']  
        conversion = request.POST['con'] 
        second_unit = request.POST['sec'] 

        std=units1(type=type,symbol=symbol,formal_name=formal_name,number_of_decimal_places=number_of_decimal_places,first_unit=first_unit,conversion=conversion,second_unit=second_unit)
        std.save()
        return redirect('unit2')


def unit_edit(request,pk):
    data=units1.objects.get(id=pk)
    return render(request,'unit_edit.html',{'p':data})

def unit_edit2(request,pk):
    std=units1.objects.get(id=pk)
    std.type=request.POST.get('type')
    std.symbol=request.POST.get('symbol')  
    std.formal_name=request.POST.get('formal')
    std.number_of_decimal_places=request.POST.get('decimal') 
    std.first_unit=request.POST.get('ft')
    std.conversion=request.POST.get('con')
    std.second_unit=request.POST.get('sec')  
    std.save()
    return redirect('unit2')
    






    #pan


def panadd(request):
    if request.method == 'POST':
        tax2=request.POST['tax']
        no2=request.POST['no']

        std = pan(tax3 = tax2,
        no = no2)
        std.save()
        return redirect('pan2')
    return render(request, 'pan.html')




    #gst


def gst3(request):
    return render(request,'load_gst.html') 


def gst2(request):
    if request.method == 'POST':
        state=request.POST['state']
        type=request.POST['type']
        teretory = request.POST['teretory']
        uin = request.POST['uin']
        gstr1 = request.POST['gstr1']
        kerala = request.POST['kerala']
        set = request.POST['set']
        enable = request.POST['enable']
        enable2 = request.POST['enable2']
        enable3 = request.POST['enable3']
        bond = request.POST['bond']
        taxrate = request.POST['taxrate']
        basistax = request.POST['basistax']
        purchase = request.POST['purchase']
        eway = request.POST['eway']
        applicable = request.POST['applicable']
        thresholt = request.POST['thresholt']
        limit = request.POST['limit']
        infrastate = request.POST['infrastate']
        thresholt2 = request.POST['thresholt2']
        invoice = request.POST['invoice']
        einvoice = request.POST['einvoice']

        std=gst1(state=state,type=type,teretory=teretory,uin=uin,gstr1=gstr1,kerala=kerala,set=set,enable=enable,
        enable2=enable2,enable3=enable3,bond=bond,taxrate=taxrate,basistax=basistax,purchase=purchase,
        eway=eway,applicable=applicable,thresholt=thresholt,limit=limit,infrastate=infrastate,thresholt2=thresholt2,
        invoice=invoice,einvoice=einvoice)

        std.save()
        return redirect('gst3')
        



#salary



# def salary(request):
#     p=create_payhead1.objects.all()
#     return render(request,'load_salary.html',{'pay':p}) 

def salary2(request):
    data2=empgroup2.objects.all()
    return render(request,'salary2.html',{'data':data2}) 

def salary3(request):
    pk=create_payhead1.objects.all()
    if request.method=='POST':
        name2=request.POST['name']
        under=request.POST['under']
        effect=request.POST['effective']
        pay=request.POST['payhead']
        rate=request.POST['rate']
        per=request.POST['per']
        payhead=request.POST['payheaad_type']
        calculation=request.POST['calculation_type']
        #save salary
        std=create_salary(name=name2,
                   under=under,
                   effective=effect,
                   payhead=pay,
                   rate=rate,
                   per=per,
                   payheaad_type=payhead,
                   calculation_type=calculation,
        )
        std.save()
        return redirect('salary')
    return render(request,'load_salary.html',{'pk':pk})






def load(request):
    did=request.GET.get("id")
    print("id")
    obj=create_payhead1.objects.get(name=did)
    return render(request,"load_load.html",{"obj":obj})

def load_calculation(request):
    did=request.GET.get("id")
    obj=create_payhead1.objects.get(name=did)
    return render(request,"load_load_calculation.html",{"obj":obj})





def bank(request):
    obj=bank3.objects.all()
    return render(request,"bank.html",{"p":obj})

def add_bank3(request):
    obj=bank3.objects.all()
    if request.method=="POST":
        nam=request.POST['name']
        std=bank3(name=nam)
        std.save()
        return redirect('employee2')
   
#---------------------------------------------Reshma-----------------------------------------------
def index(request):
    return render(request, 'Statistics.html')

def Statements_accounts(request):

        return render(request,'Statements_accounts.html')
   

def statistics(request):
    
    
    groups_count = tally_group.objects.all().count()
    centres_count= cost_centre.objects.all().count()
    ledgers_count = tally_ledger.objects.all().count()
    
    sgtotal=stockgroupcreation.objects.count()
    sitotal=stock_itemcreation.objects.count()
    vt_total=Voucher.objects.count()

    att1=Create_attendence.objects.count()
    uni1=unit_simple.objects.count()
    uni2=unit_compound.objects.count()
    uni3=uni1+uni2
    cur3=currencyAlteration.objects.count()
    empg=Create_employeegroup.objects.count()
    emp=Employee.objects.count()
    voucher =statistics_Vouchers.objects.all().order_by('Vouchers_name')
    accounts = statistics_Accounts.objects.all()
    sum=0
    total1= statistics_Total_Voucher.objects.all()
    for i in total1:
        if i.Total:
            sum+=i.Total

    
    context={
       'groups_count':groups_count,
       'centres_count':centres_count,
       'ledgers_count':ledgers_count,
        'vt_total':vt_total,
        'sgtotal':sgtotal,
        'sitotal':sitotal,
        'voucher':voucher,
        'sum':sum,
        'accounts':accounts,
        'att1':att1,
        'uni3':uni3,
        'cur3':cur3,
        'empg':empg,
        'emp':emp,
    }
    return render(request, 'Statistics.html',context)


  

def Statistics_list_of_ledger(request):
    grup=tally_group.objects.all()
    groups_count1 = tally_group.objects.all().count()
    ledg=tally_ledger.objects.all()
  
    ledgers_count1 = tally_ledger.objects.all().count()
    
    led=tally_ledger.objects.filter(status=0)

    context={
       
        "led":led,
        "grup":grup,
        "ledg":ledg,
        "groups_count1":groups_count1,
        "ledgers_count1" : ledgers_count1
    
    }
   
    return render(request,'Statistics_LedgersList.html',context)

# return redirect('/') '''

def Statistics_list_of_groups(request):
    grup=tally_group.objects.all()

    groups_count2 = tally_group.objects.all().count()
    

    context={
        
        'grup':grup,

        "groups_count2": groups_count2,
        
        }
     
    return render(request,'Statistics_GroupsList.html',context)

def Statistics_list_of_cost_centers(request):
   
    cst=cost_centre.objects.all()
    cost_centre_count=cost_centre.objects.all().count()
    context={
                    'cst':cst,
                    'cost_centre_count':cost_centre_count,
                   

        }
    return render(request,'Statistics_CostCentresList.html',context)


#-------------------------Anandha Krishnan --------------------------------
def Statistics_voucher_monthly_register(request,id):
    mo = Months.objects.all()

    vch = statistics_Vouchers.objects.get(id=id)
    count = statistics_Voucher_count.objects.filter(Voucher=id)
    total=0
    for i in count:
        if i.Total_Voucher:
            total+=i.Total_Voucher

    if statistics_Total_Voucher.objects.filter(Voucher=id):
        to=statistics_Total_Voucher.objects.get(Voucher=id)
        to.Voucher=vch
        to.Total=total
        to.save()
    else:
        to=statistics_Total_Voucher()
        to.Voucher=vch
        to.Total=total
        to.save()
   


    context = {
        'mo':mo,
        'vch':vch,
        'count':count,
        'total':total,
        
        
        
        

    }

    
    return render(request,'statistics_voucher_monthly_register.html',context)

def Statistics_voucher_register(request,id,pk):
    voucher = statistics_Voucher_Register.objects.filter(Month=id,Voucher=pk)
    vch = statistics_Vouchers.objects.get(id=pk)
    

    total_debit=0
    total_credit=0

    for i in voucher:
        if i.Debit_Amount:
            total_debit +=i.Debit_Amount
        if i.Credit_Amount:
            total_credit +=i.Credit_Amount


    v=statistics_Vouchers.objects.get(id=pk)
    m=Months.objects.get(id=id)
    count = voucher.count()
    if statistics_Voucher_count.objects.filter(Month=id,Voucher=pk):
        total= statistics_Voucher_count.objects.get(Month=id,Voucher=pk)
        
        total.Voucher=v
        total.Month=m
        total.Total_Voucher=count
        


        total.save()
    else:
        total= statistics_Voucher_count()
        total.Voucher=v
        total.Month=m
        total.Total_Voucher=count
        


        total.save()


    context = {
        'voucher':voucher,
        'total_debit':total_debit,
        'total_credit':total_credit,
        'vch':vch,
        'm':m,

    }

    
    return render(request,'statistics_voucher_register.html',context)




def Statistics_voucher_Delete(request,id,pk,de):
    voucher = statistics_Voucher_Register.objects.get(id=de)
    voucher.delete()
    

    return redirect(Statistics_voucher_register,id,pk)

#------------------------------------------Rehanas---------------------------------------------
#  units------

def statistics_units(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    sunits=unit_simple.objects.all()
    cunits=unit_compound.objects.all()
    uni1=unit_simple.objects.count()
    uni2=unit_compound.objects.count()
    uni3=uni1+uni2
    context={'sunits':sunits,'cunits':cunits,'uni3':uni3}
    return render(request,'st_units.html',context) 

def statistics_unit_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    uni=unit_simple.objects.filter(id=pk)
    context={'uni':uni}
    return render(request,'st_unit_alter.html',context)   

def statistics_su_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        sgrp =unit_simple.objects.get(id=pk)
        sgrp.symbol = request.POST.get('symbol')
        sgrp.formal_name = request.POST.get('formal_name')
        sgrp.decimal = request.POST.get('decimal')
        sgrp.uqc = request.POST.get('uqc')
        sgrp.save()
        return redirect('statistics_units')
    return render(request, 'st_units.html')     

def statistics_cunit_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    uni=unit_compound.objects.filter(id=pk)
    uuu=unit_simple.objects.all()
    context={'uni':uni,'uuu':uuu}
    return render(request,'st_unitalteration.html',context)     

def statistics_cu_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        cmp =unit_compound.objects.get(id=pk)
        cmp.f_unit = request.POST.get('first_unit')
        cmp.conversion = request.POST.get('conversion')
        cmp.s_unit = request.POST.get('second_unit')
        cmp.save()
        return redirect('statistics_units')
    return render(request, 'st_units.html')   



#  currencies-----           

def statistics_currencies(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    currencyd=currencyAlteration.objects.filter(id=1)
    currencydff=currencyAlteration.objects.all().exclude(id=1)
    currency=Currency_alt.objects.all()
    cur3=currencyAlteration.objects.count()
    context={'currencyd':currencyd,'cur3':cur3,'currency':currency,'currencydff':currencydff}
    return render(request,'st_currencies.html',context)  

def statistics_curr_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    curr=currencyAlteration.objects.filter(id=pk)
    context={'curr':curr}
    return render(request,'st_curr_alter.html',context)    

def statistics_cdef_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        cur =currencyAlteration.objects.get(id=pk)
        cur.Symbol = request.POST.get('c_symbl')
        cur.FormalName = request.POST.get('fname')
        cur.ISOCurrency = request.POST.get('isocode')
        cur.DecimalPlace = request.POST.get('decimal_p')
        cur.showAmount = request.POST.get('show_amt')
        cur.suffixSymbol = request.POST.get('suffix')
        cur.AddSpace = request.POST.get('add_space')
        cur.wordRep = request.POST.get('word_rep')
        cur.DecimalWords = request.POST.get('no_decimal')
        cur.save()
        return redirect('statistics_currencies')
    return render(request, 'st_currencies.html')       

def statistics_curr_alter2(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    curr=currencyAlteration.objects.filter(id=pk)
    curr1=Currency_alt.objects.filter(currencyAlteration_id=pk)
    context={'curr':curr,'curr1':curr1}
    return render(request,'st_currency_alter2.html',context)    



def statistics_curr_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        curr = currencyAlteration.objects.get(id=pk)
        curr.Symbol=request.POST.get('symbol')
        curr.FormalName=request.POST.get('name')
        curr.ISOCurrency=request.POST.get('iso')
        curr.DecimalPlace=request.POST.get('numdec')
        curr.showAmount=request.POST.get('amount')
        curr.suffixSymbol=request.POST.get('suffix')
        curr.AddSpace=request.POST.get('symam')
        curr.wordRep=request.POST.get('amodec')
        curr.DecimalWords=request.POST.get('decwo')

        curr.stddate=request.POST.get('standate')
        curr.stdrate=request.POST.get('stdrate')
        curr.selldate=request.POST.get('selldate')
        curr.selvorate=request.POST.get('selvrate')
        curr.sellrate=request.POST.get('selsrate')
        curr.buydate=request.POST.get('buydate')
        curr.buyvorate=request.POST.get('buyvrate')
        curr.buyrate=request.POST.get('buysrate')
         
        curr.save()                     
        return redirect('statistics_currencies')
    return render(request,'currencies.html')      

#  Attendence / Production types -----       

def statistics_atten_prod(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    attendance=Create_attendence.objects.all()
    att1=Create_attendence.objects.count()
    context={'att1':att1,'attendance':attendance}
    return render(request,'st_attend_prod.html',context)   

def statistics_atten_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    att=Create_attendence.objects.filter(id=pk)
    attendance=Create_attendence.objects.all()
    context={'att':att,'attendance':attendance}
    return render(request,'st_attendance_alter.html',context)    

def statistics_atten_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        attend =Create_attendence.objects.get(id=pk)
        attend.name = request.POST.get('name')
        attend.alias = request.POST.get('alias')
        attend.under = request.POST.get('under_name')
        attend.type = request.POST.get('attendance')
        attend.period = request.POST.get('period')
        attend.units = request.POST.get('units')
        attend.save()
        return redirect('statistics_atten_prod')
    return render(request, 'st_attend_prod.html')    

def statistics_att_create(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    aaa = Create_attendence.objects.all()
    context = {'aaa':aaa}
    return render(request,'st_attend_create.html',context)    

def statistics_add_attend(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        name = request.POST.get('name')
        alias = request.POST.get('alias')
        under_name = request.POST.get('show_amt')
        attendance = request.POST.get('attendance')
        period = request.POST.get('period')
        atten = Create_attendence(name=name,
                                   alias=alias,
                                   under=under_name,
                                   type=attendance,
                                   period=period)
        atten.save()
        return redirect('statistics_atten_prod')
    return render(request, 'st_attend_prod.html')


#  Employee Groups---------

def statistics_emp_groups(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    p_cost=emp_category.objects.all()
    empg=Create_employeegroup.objects.all()
    cost=emp_category.objects.count()
    empg1=Create_employeegroup.objects.count()
    context={'p_cost':p_cost,'empg':empg,'empg1':empg1,'cost':cost}
    return render(request,'st_employee_group.html',context)  

  
def statistics_p_cost(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    pcos=emp_category.objects.filter(id=pk)
    context={'pcos':pcos}
    return render(request,'st_pcost_alter.html',context)  

def statistics_pcost_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        pcost =emp_category.objects.get(id=pk)
        pcost.cat_name = request.POST.get('name')
        pcost.cat_alias = request.POST.get('alias')
        pcost.revenue_items = request.POST.get('revenue')
        pcost.non_revenue_items = request.POST.get('non_revenue')
        pcost.save()
        return redirect('statistics_emp_groups')
    return render(request, 'st_employee_group.html')      
     

def statistics_eg_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    empalter=Create_employeegroup.objects.filter(id=pk)
    emp=Create_employeegroup.objects.all()
    context={'empalter':empalter,'emp':emp}
    return render(request,'st_emp_group_alter.html',context)    

def statistics_empgrp_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        empga =Create_employeegroup.objects.get(id=pk)
        empga.name = request.POST.get('name')
        empga.alias = request.POST.get('alias')
        empga.under_name = request.POST.get('under_name')
        empga.salary_details = request.POST.get('salary')
        empga.save()
        return redirect('statistics_emp_groups')
    return render(request, 'st_employee_group.html')      

def statistics_empg_dtls(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    empgd=Create_employeegroup.objects.filter(id=pk)
    epay=create_payhead.objects.all()
    if request.method=='POST':
        name1=request.POST['name']
        under=request.POST['under']
        effect=request.POST['effective']
        pay=request.POST['payhead']
        rate=request.POST['rate']
        per=request.POST['per']
        payhead=request.POST['payheaad_type']
        calculation=request.POST['calculation_type']
        #save salary
        std=salary(name=name1,
                   under=under,
                   effective=effect,
                   payhead=pay,
                   rate=rate,
                   per=per,
                   pay_type=payhead,
                   cal_type=calculation,
        )
        std.save()
        return redirect('statistics_emp_groups')
    return render(request,'st_empg_details.html',{'epay':epay,'empgd':empgd}) 


def statistics_create_payhd(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    ph=Create_attendence.objects.filter(type="Attendance/Leave with pay")
    ph2=Create_attendence.objects.filter(type="Production")
    std=Create_attendence.objects.all()
    return render(request,'st_pay_head.html',{'std':std,'ph':ph,'ph2':ph2}) 


def statistics_add_payhead(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           
        )
        std.save()
        idd=std

        std2=compute_information(Pay_head_id=idd,
                                 compute=compute,
                                 effective_from=effective_from,
                                #  amount_greater=amount_greaterthan,
                                 amount_upto=amount_upto,
                                 value=value,
        )
        std2.save()

        std3=Rounding(pay_head_id=idd,
                     Rounding_Method=round_method,
                     Round_limit=limit,
        )
        std3.save()

        std4=gratuity(pay_head_id=idd,
                     days_of_months=days_of_months,
                     number_of_months_from=from_date,
                     to=to,
                     calculation_per_year=calculation_per_year,
        )
        std4.save()
        return redirect('/')
    return render(request,'st_pay_head.html')  

def statistics_add_salaryd(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        empga =Create_employeegroup.objects.get(id=pk)
        empga.name = request.POST.get('name')
        empga.alias = request.POST.get('alias')
        empga.under_name = request.POST.get('under_name')
        empga.salary_details = request.POST.get('salary')
        empga.save()
        return redirect('statistics_emp_groups')
    return render(request, 'st_employee_group.html')   


def statistics_empg_create(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    aaa = Create_employeegroup.objects.all()
    context = {'aaa':aaa}
    return render(request,'st_create_empg.html',context)     

def statistics_add_empg(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        name = request.POST.get('name')
        alias = request.POST.get('alias')
        under_name = request.POST.get('show_amt')
        salary_details = request.POST.get('salary')
        atten = Create_attendence(name=name,
                                   alias=alias,
                                   under=under_name,
                                   type=salary_details)
        atten.save()
        return redirect('statistics_emp_groups')
    return render(request, 'st_employee_group.html')    



# Employee -------


def statistics_employee(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    p_cost=emp_category.objects.all()
    empg=Create_employeegroup.objects.all()
    emp=Employee.objects.all()
    cost=emp_category.objects.count()
    empg1=Create_employeegroup.objects.count()
    empg2=Employee.objects.count()
    context={'p_cost':p_cost,'empg':empg,'emp':emp,'cost':cost,'empg1':empg1,'empg2':empg2}
    return render(request,'st_employee.html',context)

    
def statistics_emp_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    emm=Employee.objects.filter(id=pk)
    empg=Create_employeegroup.objects.all()
    context={'emm':emm,'empg':empg}
    return render(request,'st_employee_alter.html',context)  

  
def statistics_employee_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        empp =Employee.objects.get(id=pk)
        empp.name =request.POST.get('name')
        empp.alias=request.POST.get('alias')
        empp.under=request.POST.get('under')
        empp.defn_sal=request.POST.get('sal')
        empp.emp_name=request.POST.get('empname')
        empp.emp_desg=request.POST.get('desig')
        empp.fnctn=request.POST.get('fn')
            

        empp.location=request.POST.get('loc')
        empp.gender=request.POST.get('gen')
        empp.blood=request.POST.get('blood')
        empp.parent_name=request.POST.get('prnts')
        empp.spouse_name=request.POST.get('spouse')
        empp.address=request.POST.get('adrs')
        empp.number=request.POST.get('phone')

        empp.email=request.POST.get('email')
        empp.bankdtls=request.POST.get('bank')
        empp.inc_tax_no=request.POST.get('incno')
        empp.aadhar_no=request.POST.get('adhar')
        empp.uan=request.POST.get('uan')
        empp.pfn=request.POST.get('pf')
        empp.pran=request.POST.get('pr')
        empp.esin=request.POST.get('esi')

 
            
        empp.save()
        return redirect('statistics_employee')
    return render(request,'st_employee.html')  

    #----------------------------------------Mohammed Arif --------------------------------------------
    # stkgrp ---------------

def Statistics_Stock_Groups(request):
    sgdata=stockgroupcreation.objects.all()
    # SGdata=stock_itemcreation.objects.all()
    sqtotal=stockgroupcreation.objects.count()
    # swtotal=stock_itemcreation.objects.count()
    context={'sgdata':sgdata,'sqtotal':sqtotal}
    return render(request,'stockgroup.html',context)

def Statistics_Stock_Group_Creation_Page(request):
    sg_data=stockgroupcreation.objects.all()
    context={'sg_data':sg_data}
    return render(request,'stockgrpcreationpage.html',context)

def Statistics_Stock_Group_Creation(request):
    if request.method =='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        quantities=request.POST['quantities']

        data=stockgroupcreation(name=name,alias=alias,under=under_name,quantities=quantities)
        data.save()
        return redirect("Statistics_Stock_Groups")

def Statistics_Stock_Group_Edit_Page(request,pk):
    sg_data=stockgroupcreation.objects.all()
    sgedit=stockgroupcreation.objects.get(id=pk)
    context={'sgedit':sgedit,'sg_data':sg_data}
    return render(request,"editstockgroup.html",context)

def Statistics_Edit_Stock_Group(request,pk):
    if request.method =='POST':
        sgdata=stockgroupcreation.objects.get(id=pk)
        sgdata.name=request.POST['name']
        sgdata.alias=request.POST['alias']
        sgdata.under=request.POST['under_name']
        sgdata.quantities=request.POST['quantities']

        sgdata.save()
        return redirect('Statistics_Stock_Groups')
    return render(request,'editstockgroup.html')

def Statistics_Delete_Stock_Group(request,pk):
    stk=stockgroupcreation.objects.get(id=pk)
    stk.delete()
    return redirect('Statistics_Stock_Groups')

# syk item--------------------

def Statistics_Stock_Items(request):
    sgdata=stockgroupcreation.objects.all()
    sidata=stock_itemcreation.objects.all()
    sgtotal=stockgroupcreation.objects.count()
    sitotal=stock_itemcreation.objects.count()
    context={'sgdata':sgdata,'sgtotal':sgtotal,'sidata':sidata,'sitotal':sitotal}
    return render(request,'stockitem.html',context)

def Statistics_Stock_Item_Creation_Page(request):
    si_data=stock_itemcreation.objects.all()
    grp=stockgroupcreation.objects.all()
    unt=unit_compound.objects.all()
    u=unit_simple.objects.all()
    context={'si_data':si_data,"grp":grp,'u':u,'unt':unt}
    return render(request,'stockitemcreationpage.html',context)


def Statistics_Stock_Item_Creation(request):
    if request.method=='POST':
        nm=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        units=request.POST['units']
        gst_applicable=request.POST['gst_applicable']
        set_alter=request.POST['set_alter']
        typ_sply=request.POST['typ_sply']
        rate_of_duty=request.POST['rate_of_duty']
        
        crt=stock_itemcreation(name=nm,alias=alias,under=under,units=units,typ_sply=typ_sply,
        gst_applicable=gst_applicable,set_alter=set_alter,rate_of_duty=rate_of_duty)
        crt.save()
        
        return redirect('Statistics_Stock_Items')



def Statistics_Stock_Item_Edit_Page(request,pk):
    si_data=stock_itemcreation.objects.all()
    grp=stockgroupcreation.objects.all()
    unt=unit_compound.objects.all()
    u=unit_simple.objects.all()
    sidata=stock_itemcreation.objects.get(id=pk)
    context={'edit':sidata,"si_data":si_data,'grp':grp,'unt':unt,'u':u}
    return render(request,"editstockitem.html",context)

def Statistics_Edit_Stock_Item(request,pk):
    if request.method =='POST':
        sidata=stock_itemcreation.objects.get(id=pk)
        sidata.name=request.POST['name']
        sidata.alias=request.POST['alias']
        sidata.under=request.POST['under']
        sidata.units=request.POST['units']
        sidata.gst_applicable=request.POST['gst_applicable']
        sidata.set_alter=request.POST['set_alter']
        sidata.typ_sply=request.POST['typ_sply']
        sidata.rate_of_duty=request.POST['si_data']
        sidata.quantity=request.POST['quantity']
        sidata.rate=request.POST['rate']
        sidata.per=request.POST['per']
        sidata.value=request.POST['value']

        sidata.save()
        return redirect('Statistics_Stock_Items')
    return render(request,'editstockitem.html')

def Statistics_Delete_Stock_Item(request,pk):
    stk=stock_itemcreation.objects.get(id=pk)
    stk.delete()
    return redirect('Statistics_Stock_Items')

# vchr typ ---------------------

def Statistics_Voucher_Types(request):
    vt_data=Voucher.objects.all()
    vt_total=Voucher.objects.count()
    context={'vt_data':vt_data,'vt_total':vt_total}
    return render(request,'vouchertype.html',context)

def Statistics_Voucher_Type_Creation_Page(request):
    data=Voucher.objects.all()
    context={'data':data}
    return render(request,'vouchertypecreationpage.html',context)

def Statistics_Voucher_Type_Creation(request):
        if request.method=='POST':
            nm=request.POST['vname']
            als=request.POST['alias']
            vtp=request.POST['vouch_type']
            abbr=request.POST['Abbreviation']
            actp=request.POST['activate_Vtype']
            mvno=request.POST['method_Vno']
            prnt=request.POST['prevent']
            acn=request.POST['advance_con']
            use=request.POST['use_EDV']
            zero=request.POST['zero_val']
            mvd=request.POST['mVoptional_defualt']
            anar=request.POST['allow_nar']
            prvdl=request.POST['provide_L']
            jrnl=request.POST['manu_jrnl']
            track=request.POST['track_purchase']
            enbl=request.POST['enable_acc']
            prntva=request.POST['prnt_VA_save']
            prntfml=request.POST['prnt_frml']
            juri=request.POST['jurisdiction']
            tprint=request.POST['title_print']
            setaltr=request.POST['set_alter']
            posinv=request.POST['pos_invoice']
            msg1=request.POST['msg_1']
            msg2=request.POST['msg_2']
            dbank=request.POST['default_bank']
            nc=request.POST['name_class']

            vhr=Voucher(voucher_name=nm,
                        alias = als,
                        voucher_type = vtp,
                        abbreviation = abbr,
                        voucherActivate = actp,
                        voucherNumber = mvno,
                        preventDuplicate = prnt,
                        advance_con = acn,
                        voucherEffective = use,
                        transaction = zero,
                        make_optional = mvd,
                        voucherNarration = anar,
                        provideNarration = prvdl,
                        manu_jrnl = jrnl,
                        track_purchase = track,
                        enable_acc = enbl,
                        prnt_VA_save = prntva,
                        prnt_frml = prntfml,
                        jurisdiction = juri,
                        title_print = tprint,
                        set_alter = setaltr,
                        pos_invoice = posinv,
                        msg_1 = msg1,
                        msg_2 = msg2,
                        default_bank = dbank,
                        name_class = nc,)          
            vhr.save()
            return redirect('Statistics_Voucher_Types')

def Statistics_Voucher_Type_Edit_Page(request,pk):
    vt_edit=Voucher.objects.get(id=pk)
    edit=Voucher.objects.all()
    context={'vt_edit':vt_edit,'edit':edit}
    return render(request,'vouchertypeeditpage.html',context)

def Statistics_Edit_Voucher_Types(request,pk):
    if request.method =='POST':
        vchrdata=Voucher.objects.get(id=pk)
        vchrdata.voucher_name=request.POST['vname']
        vchrdata.alias=request.POST['alias']
        # vchrdata.voucher_type=request.POST['vouch_type']
        vchrdata.abbreviation=request.POST['Abbreviation']
        vchrdata.voucherActivate=request.POST['activate_Vtype']
        vchrdata.voucherNumber=request.POST['method_Vno']
        vchrdata.preventDuplicate=request.POST['prevent']
        vchrdata.advance_con=request.POST['advance_con']
        vchrdata.voucherEffective=request.POST['use_EDV']
        vchrdata.transaction=request.POST['zero_val']
        vchrdata.make_optional=request.POST['mVoptional_defualt']
        vchrdata.voucherNarration=request.POST['allow_nar']
        vchrdata.provideNarration=request.POST['provide_L']
        vchrdata.manu_jrnl=request.POST['manu_jrnl']
        vchrdata.track_purchase=request.POST['track_purchase']
        vchrdata.enable_acc=request.POST['enable_acc']
        vchrdata.prnt_VA_save=request.POST['prnt_VA_save']
        vchrdata.prnt_frml=request.POST['prnt_frml']
        vchrdata.jurisdiction=request.POST['jurisdiction']
        vchrdata.title_print=request.POST['title_print']
        vchrdata.set_alter=request.POST['set_alter']
        vchrdata.pos_invoice=request.POST['pos_invoice']
        vchrdata.msg_1=request.POST['msg_1']
        vchrdata.msg_2=request.POST['msg_2']
        vchrdata.default_bank=request.POST['default_bank']
        vchrdata.name_class=request.POST['name_class']

    vchrdata.save()
    return redirect('Statistics_Voucher_Types')

def Statistics_Delete_Voucher_Type(request,pk):
    vt=Voucher.objects.get(id=pk)
    vt.delete()
    return redirect('Statistics_Voucher_Types')

#--------------------------------------------Jerin-------------------------------------------
def receivabl(request):
    rec=receivable.objects.all()
    return render (request,'receivable.html',{'rec':rec})    


def payabl(request):
    pay=payable.objects.all()
    return render(request,'payable.html',{'pay':pay})   

def creategroup(request):
    grp=GroupModel.objects.all()
    return render (request,'creategroup.html',{'grp':grp})     



        

def grcreate(request):
    gr=GroupModel.objects.all()
    return render(request,'grcreate.html',{'gr':gr})    

def createledger(request):
    grp=GroupModel.objects.all()
    return render (request,'createledger.html',{'grp':grp})        

def credit(request):
    cre=cred.objects.all()
    return render(request,'credit.html',{'cre':cre})

def debi(request):
    debi=debit.objects.all()
    return render(request,'debit.html',{'debi':debi})    

def ledgerlist(request):
    ledg=ledgercreation.objects.all()
    return render(request,'ledgerlist.html',{'ledg':ledg})    



def ledgercreations(request):
    if request.method == 'POST':
        
        name=request.POST['name']

        alias=request.POST['alias']
        under=request.POST['under']
        bank_details=request.POST['bank_details']
        
        ac_holder_nm=request.POST['ac_holder_nm']

        acc_no=request.POST['acc_no']
        if acc_no=="":
            acc_no=None

        ifsc_code=request.POST['ifsc_code']
        if ifsc_code=="":
            ifsc_code=None

        swift_code=request.POST['swift_code']
        if swift_code=="":
            swift_code=None

        bank_name=request.POST['bank_name']
        branch=request.POST['branch']
        SA_cheque_bk=request.POST['SA_cheque_bk']
        Echeque_p=request.POST['Echeque_p']

        occ_set_odl=request.POST['occ_set_odl']
        occ_ac_holder_nm=request.POST['occ_ac_holder_nm']
        occ_acc_no=request.POST['occ_acc_no']
        if occ_acc_no=="":
            occ_acc_no=None

        occ_ifsc_code=request.POST['occ_ifsc_code']
        if occ_ifsc_code=="":
            occ_ifsc_code=None

        occ_swift_code=request.POST['occ_swift_code']    
        if occ_swift_code=="":
            occ_swift_code=None

        occ_bank_name=request.POST['occ_bank_name']   
        occ_branch=request.POST['occ_branch']
        occ_SA_cheque_bk=request.POST['occ_SA_cheque_bk']
        occ_Echeque_p=request.POST['occ_Echeque_p']

        od_set_odl=request.POST['od_set_odl']
        od_ac_holder_nm=request.POST['od_ac_holder_nm']
        od_acc_no=request.POST['od_acc_no']
        if od_acc_no=="":
            od_acc_no=None

        od_ifsc_code=request.POST['od_ifsc_code']  
        if od_ifsc_code=="":
            od_ifsc_code=None

        od_swift_code=request.POST['od_swift_code']
        if od_swift_code=="":
            od_swift_code=None

        od_bank_name=request.POST['od_bank_name']
        if od_bank_name=="":
            od_bank_name=None

        od_branch=request.POST['od_branch']
        od_SA_cheque_bk=request.POST['od_SA_cheque_bk']
        od_Echeque_p=request.POST['od_Echeque_p']






        mname=request.POST['mname']
        address=request.POST['address']
        country=request.POST['country']
        state=request.POST['state']

        pincode=request.POST['pincode']
        if pincode=="":
            pincode=None

        pan_no=request.POST['pan_no']
        if pan_no=="":
            pan_no=None

        registration_type=request.POST['registration_type']    

        gst_uin=request.POST['gst_uin']
        if gst_uin=="":
            gst_uin=None

        set_alter_gstdetails=request.POST['set_alter_gstdetails']

        statutory_details=request.POST['statutory_details']

        type_of_ledger=request.POST['type_of_ledger']
        rounding_method=request.POST['rounding_method']
        rounding_limit=request.POST['rounding_limit']
        if rounding_limit=="":
            rounding_limit=None
        GST_Applicable=request.POST['GST_Applicable']
        Alter_GST_Details=request.POST['Alter_GST_Details']
        Appropriate=request.POST['Appropriate']
        Types_of_supply=request.POST['Types_of_supply']

        type_duty_tax=request.POST['type_duty_tax']
        tax_type=request.POST['tax_type']
        percentage_of_calcution=request.POST['percentage_of_calcution']
        rond_method=request.POST['rond_method']
        rond_limit=request.POST['rond_limit']
        if rond_limit=="":
            rond_limit=None
        balance_billbybill=request.POST['balance_billbybill']
        credit_period=request.POST['credit_period']
        creditdays_voucher=request.POST['creditdays_voucher']
      




        led=ledgercreation(
            name=name,
            alias=alias,
            under=under,
            bank_details=bank_details,
            ac_holder_nm=ac_holder_nm,
            acc_no=acc_no,
            ifsc_code=ifsc_code,
            swift_code=swift_code,
            bank_name=bank_name,
            branch=branch,
            SA_cheque_bk=SA_cheque_bk,
            Echeque_p=Echeque_p,
            mname=mname,
            address=address,
            country=country,
            state=state,
            pincode=pincode,
            pan_no=pan_no,
            registration_type=registration_type,
            gst_uin=gst_uin,
            set_alter_gstdetails=set_alter_gstdetails,
            type_of_ledger=type_of_ledger,
            rounding_method=rounding_method,
            rounding_limit=rounding_limit,
            GST_Applicable=GST_Applicable,
            Alter_GST_Details=Alter_GST_Details,
            Appropriate=Appropriate,
            Types_of_supply=Types_of_supply,
            type_duty_tax=type_duty_tax,
            tax_type=tax_type,
            percentage_of_calcution=percentage_of_calcution,
            rond_method=rond_method,
            rond_limit=rond_limit,
            balance_billbybill=balance_billbybill,
            credit_period=credit_period,
            creditdays_voucher=creditdays_voucher,
            statutory_details=statutory_details,
            occ_set_odl=occ_set_odl,
            occ_acc_no=occ_acc_no,
            occ_bank_name=occ_bank_name,
            occ_ac_holder_nm=occ_ac_holder_nm,
            occ_branch=occ_branch,
            occ_Echeque_p=occ_Echeque_p,
            occ_ifsc_code=occ_ifsc_code,
            occ_SA_cheque_bk=occ_SA_cheque_bk,
            occ_swift_code=occ_swift_code,
            od_ac_holder_nm=od_ac_holder_nm,
            od_acc_no=od_acc_no,
            od_bank_name=od_bank_name,
            od_branch=od_branch,
            od_Echeque_p=od_Echeque_p,
            od_SA_cheque_bk=od_SA_cheque_bk,
            od_ifsc_code=od_ifsc_code,
            od_set_odl=od_set_odl,
            od_swift_code=od_swift_code

            


        )
        led.save()
        return redirect('ledgerlist')


def nw(request):
    ledi=led.objects.all()
    return render(request,'nw.html',{'ledg':ledi})

def outstanding(request):
    return render(request,'outstd.html')

#Maneesha

def creditnoteregister(request):
    
     if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cmp=Companies.objects.get(id=t_id)
        credit=creditreg.objects.all()
        months = [i.month for i in creditreg.objects.values_list('date', flat=True)]
        april=creditreg.objects.filter(date__month='04').count()
        may=creditreg.objects.filter(date__month='05').count() 
        june=creditreg.objects.filter(date__month='06').count()
        july=creditreg.objects.filter(date__month='07').count()
        august=creditreg.objects.filter(date__month='08').count()
        september=creditreg.objects.filter(date__month='09').count()
        october=creditreg.objects.filter(date__month='10').count()
        november=creditreg.objects.filter(date__month='11').count() 
        december=creditreg.objects.filter(date__month='12').count()
        january=creditreg.objects.filter(date__month='01').count()
        february=creditreg.objects.filter(date__month='02').count()
        march=creditreg.objects.filter(date__month='03').count()
        data={}
        data['april']=april
        data['may']=may
        data['june']=june
        data['july']=july
        data['august']=august
        data['september']=september
        data['october']=october
        data['november']=november
        data['december']=december
        data['january']=january
        data['february']=february
        data['march']=march
        data['cmp']=cmp
        return render(request,'creditnoteregister.html',data)

def debitnoteregister(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cmp=Companies.objects.get(id=t_id)
        print(cmp)
        april=debitnote.objects.filter(date__month='04').count()
        may=debitnote.objects.filter(date__month='05').count() 
        june=debitnote.objects.filter(date__month='06').count()
        july=debitnote.objects.filter(date__month='07').count()
        august=debitnote.objects.filter(date__month='08').count()
        september=debitnote.objects.filter(date__month='09').count()
        october=debitnote.objects.filter(date__month='10').count()
        november=debitnote.objects.filter(date__month='11').count() 
        december=debitnote.objects.filter(date__month='12').count()
        january=debitnote.objects.filter(date__month='01').count()
        february=debitnote.objects.filter(date__month='02').count()
        march=debitnote.objects.filter(date__month='03').count()
        data={}
        data['april']=april
        data['may']=may
        data['june']=june
        data['july']=july
        data['august']=august
        data['september']=september
        data['october']=october
        data['november']=november
        data['december']=december
        data['january']=january
        data['february']=february
        data['march']=march
        data['cmp']=cmp
        return render(request,'debitnoteregister.html',data)

def voucherregister(request,pk):
    m=pk
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cmp=Companies.objects.get(id=t_id)
        print(pk)
        voucher=creditreg.objects.filter(date__month=pk)
        print(voucher)
        total=sum(voucher.values_list('creditamount',flat=True))
#    total=creditenote.objects.filter(date__month=pk).aggregate(TOTAL=sum('creditamount'))['TOTAL']
        cont=creditreg.objects.filter(date__month=pk).count()
    if m==1:
        msg1="1-Jan-22  to 31-Jan-22"
    elif m==2:
        msg1="1-Feb-22  to 28-Feb-22"
    elif m ==3:
        msg1="1-March-22  to 31-March-22"
    elif m ==4:
        msg1="1-April-22 to 30-April-22"
    elif m ==5:
        msg1="1-May-22  to 31-May-22"
    elif m ==6:
        msg1="1-June-22  to  30-June-22"
    elif m ==7:
        msg1="1-July-22  to 31-July-22"
    elif m ==8:
        msg1="1-Aug-22  to 31-Aug-22"  
    elif m==9:
        msg1="1-Sep-22  to 30-Sep-22"
    elif m ==10:
        msg1="1-Oct-22 to 31-Oct-22"
    elif m ==11:
        msg1="1-Nov-22 to 30-Nov-22" 
    elif m ==12:
        msg1="1-Dec-22 to 31-Dec-22"      
    else:
        msg1="01-July-22 to 31-July-22"               
          
    
    return render(request,'voucherregister.html',{'voucher':voucher,'total':total,'cmp':cmp,'msg1':msg1})

def voucherregisterdebit(request,pk):
    m=pk
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cmp=Companies.objects.get(id=t_id)
        print(pk)
        voucher=debitnote.objects.filter(date__month=pk)
        print(voucher)
        total=sum(voucher.values_list('debitamount',flat=True))
#    total=creditenote.objects.filter(date__month=pk).aggregate(TOTAL=sum('creditamount'))['TOTAL']
        if m==1:
            msg1="1-Jan-22  to 31-Jan-22"
        elif m==2:
            msg1="1-Feb-22  to 28-Feb-22"
        elif m ==3:
            msg1="1-March-22  to 31-March-22"
        elif m ==4:
             msg1="1-April-22 to 30-April-22"
        elif m ==5:
             msg1="1-May-22  to 31-May-22"
        elif m ==6:
            msg1="1-June-22 to 30-June-22"
        elif m ==7:
            msg1="1-July-22  to 31-July-22"
        elif m ==8:
             msg1="1-Aug-22  to 31-Aug-22"  
        elif m==9:
            msg1="1-Sep-22  to 30-Sep-22"
        elif m ==10:
             msg1="1-Oct-22 to 31-Oct-22"
        elif m ==11:
            msg1="1-Nov-22 to 30-Nov-22" 
        elif m ==12:
             msg1="1-Dec-22 to 31-Dec-22"      
        else:
            msg1="01-July-22 to 31-July-22"               
        

        return render(request,'voucherregisterdebit.html',{'voucher':voucher,'total':total,'cmp':cmp,'msg1':msg1})

# ananthakrishnan

def account_books_ledger(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        # ledger = tally_ledger.objects.all()
        ledger = tally_ledger.objects.filter(company=t_id)
        context = {'ledger' :ledger}
        return render(request,'account_books_ledger.html',context) 

def account_books_create_ledger(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        # group = tally_ledger.objects.all()
        group = tally_ledger.objects.filter(company=t_id)
        context = {'group':group}
        return render(request,'account_books_ledger_load_create_ledger.html',context) 

def account_create_ledger(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        ledger=tally_ledger.objects.all()
        if request.method=='POST':
            nm=request.POST.get('name')
            als=request.POST.get('alias')
            under=request.POST.get('under')
            mname=request.POST.get('mailingname')
            adr=request.POST.get('address')
            st=request.POST.get('state')
            cntry=request.POST.get('country')
            pin=request.POST.get('pincode')
            pno=request.POST.get('pan_no')
            bdetls=request.POST.get('bank_details')
            rtype=request.POST.get('registration_type')
            gst_uin=request.POST.get('gst_uin')
            opnbn=request.POST.get('opening_blnc')
            type = request.POST['Type']
            spdl=request.POST.get('set_odl')
            achnm=request.POST.get('ac_holder_nm')
            acno=request.POST.get('acc_no')
            ifsc=request.POST.get('ifsc_code')
            scode=request.POST.get('swift_code')
            bn=request.POST.get('bank_name')
            brnch=request.POST.get('branch')
            sacbk=request.POST.get('SA_cheque_bk')
            ecp=request.POST.get('Echeque_p')
            sacpc=request.POST.get('SA_chequeP_con')
            typofled=request.POST.get('type_of_ledger')
            rometh=request.POST.get('rounding_method')
            rolmt=request.POST.get('rounding_limit')
            typdutytax=request.POST.get('type_duty_tax')
            taxtyp=request.POST.get('tax_type')
            valtype=request.POST.get('valuation_type')
            rateperu=request.POST.get('rate_per_unit')
            percalc=request.POST.get('percentage_of_calcution')
            rondmethod=request.POST.get('rond_method')
            roimlit=request.POST.get('rond_limit')
            gstapplicbl=request.POST.get('gst_applicable')
            sagatdet=request.POST.get('setalter_gstdetails')
            typsupply=request.POST.get('type_of_supply')
            asseval=request.POST.get('assessable_value')
            appropto=request.POST.get('appropriate_to')
            methcalcu=request.POST.get('method_of_calculation')
            balbillbybill=request.POST.get('balance_billbybill')
            credperiod=request.POST.get('credit_period')
            creditdaysvouch=request.POST.get('creditdays_voucher')        
            ldr=tally_ledger(name=nm,alias=als,under=under,mname=mname,address=adr,state=st,country=cntry,
                            pincode=pin,pan_no=pno,bank_details=bdetls,registration_type=rtype,gst_uin=gst_uin,
                            opening_blnc=opnbn,
                            opening_blnc_type=type,
                            set_odl=spdl,ac_holder_nm=achnm,acc_no=acno,ifsc_code=ifsc,swift_code=scode,
                            bank_name=bn,branch=brnch,SA_cheque_bk=sacbk,Echeque_p=ecp,SA_chequeP_con=sacpc,
                            type_of_ledger=typofled,rounding_method=rometh,rounding_limit=rolmt,type_duty_tax=typdutytax,tax_type=taxtyp,
                            valuation_type=valtype,rate_per_unit=rateperu,percentage_of_calcution=percalc,rond_method=rondmethod,rond_limit=roimlit,
                            gst_applicable=gstapplicbl,setalter_gstdetails=sagatdet,type_of_supply=typsupply,assessable_value=asseval,
                            appropriate_to=appropto,method_of_calculation=methcalcu,balance_billbybill=balbillbybill,credit_period=credperiod,
                            creditdays_voucher=creditdaysvouch,company_id=t_id)
                
            ldr.save()
            group_under = Account_Books_Group_under.objects.all()
            ad =""
            for i in group_under:
                if i.group_under_Name == under:
                    ad = under
                    gup=Account_Books_Group_under.objects.get(group_under_Name=under)
                    account_book_ledger = Account_Books_Ledger()
                    account_book_ledger.ledger_name = nm
                    account_book_ledger.group_under = gup
                    account_book_ledger.ledger_opening_bal = opnbn
                    account_book_ledger.ledger_opening_bal_type = type
                    account_book_ledger.save()
            if ad != under:
                account_book_group_under = Account_Books_Group_under()
                account_book_group_under.group_under_Name =under
                account_book_group_under.save()
                account_book_ledger = Account_Books_Ledger()
                account_book_ledger.ledger_name = nm
                gu =Account_Books_Group_under.objects.get(id=account_book_group_under.id)
                account_book_ledger.group_under = gu
                account_book_ledger.ledger_opening_bal = opnbn
                account_book_ledger.ledger_opening_bal_type = type
                account_book_ledger.save()
                return render(request,'account_books_ledger.html',{'ledger':ledger})
            return redirect('/')

def account_books_ledger_show2(request,id):
    voucher = Account_books_Ledger_Voucher.objects.filter(ledger=id)
    ledger = Account_Books_Ledger.objects.filter(id=id)
    le = Account_Books_Ledger.objects.get(id=id)


    total_debit=0
    total_credit=0
    total_balance1=0
    total_balance2 =0
    closing_balance =0


    for i in voucher:
        if i.Debit :

            total_debit +=  i.Debit
        if i.Credit :
            total_credit = total_credit + i.Credit

    total_balance1 = le.ledger_opening_bal+total_debit

    total_balance2 = le.ledger_opening_bal+total_credit

    if le.ledger_opening_bal_type =="Dr":
            closing_balance = total_balance1 - total_credit
            if (closing_balance < 0):
                closing_balance = -1*closing_balance
            type2="Dr"    
    else:
        closing_balance = total_balance1 - total_credit
        if (closing_balance < 0):
            closing_balance = -1*closing_balance
        type2="Cr"     



            


    context={
        'voucher' : voucher,
        'ledger' :ledger,
        
        'total_debit':total_debit,
        'total_credit':total_credit,
        'closing_balance':closing_balance,
        'type2':type2,
        'le':le
        
        
        
     }  


    return render(request,'account_books_ledger_show2.html',context) 

def cash_bank_books_cash_bank_summary(request):
    group = Account_Books_Group_under.objects.all()
    balance = cash_bank_books_Group_Under_closing_balance.objects.all()
    total_debit=0
    total_credit=0
    for i in balance:
        if i.total_closing_balance_debit:
            total_debit += i.total_closing_balance_debit
        if  i.total_closing_balance_credit:  
            total_credit += i.total_closing_balance_credit
    context = { 'group':group,  'total_debit':total_debit, 'total_credit':total_credit,}
    return render(request,'cash_bank_books_cash_bank_summary.html',context)

def cash_bank_books_group_summary(request,id):
    ledger = Account_Books_Ledger.objects.filter(group_under=id)
    
    total_debit=0
    total_credit=0

    for i in ledger:
        if i.ledger_opening_bal_type == 'Dr':
            clo =cash_bank_books_TotalClosing_balance.objects.filter(ledger= i.id)
            for j in clo:
                if j.type =="Dr":
                    if j.Total_Closing_balance :
                        total_debit += j.Total_Closing_balance
                else:
                    if j.Total_Closing_balance :
                        total_credit += j.Total_Closing_balance


                
        else:
            clo =cash_bank_books_TotalClosing_balance.objects.filter(ledger= i.id)
            for j in clo:
                if j.type =="Cr":
                    if j.Total_Closing_balance :
                        total_credit += j.Total_Closing_balance
                else:
                    if j.Total_Closing_balance :
                        total_debit += j.Total_Closing_balance    


         

    if cash_bank_books_Group_Under_closing_balance.objects.filter(group_under=id):

        gp = cash_bank_books_Group_Under_closing_balance.objects.get(group_under=id)
        group = Account_Books_Group_under.objects.get(id=id)
        gp.group_under= group
        gp.total_closing_balance_debit = total_debit
        gp.total_closing_balance_credit =  total_credit
        gp.save()

       
        
    else:
        gp = cash_bank_books_Group_Under_closing_balance()
        group = Account_Books_Group_under.objects.get(id=id)
        gp.group_under= group
        gp.total_closing_balance_debit = total_debit
        gp.total_closing_balance_credit =  total_credit
        gp.save()


        

    

    context ={
        'ledger' :ledger,
        'total_debit':total_debit,
        'total_credit':total_credit,
        


    }



    return render(request,'cash_bank_books_cash_bank_summary2.html',context)   

def cash_bank_books_ledger_monthly_summary(request,id):
    le = Account_Books_Ledger.objects.get(id=id)
    voucher = Account_books_Ledger_Voucher.objects.filter(ledger=le)
    ledger = Account_Books_Ledger.objects.filter(id=le.id)
    
    ledger_n = le.ledger_name

   
    le_id = le.id
    mo = Months.objects.all()
    lemo = cash_bank_books_Leger_Month_closing.objects.filter(Ledger=le)

   
    total_debit=0 
    total_credit=0 
    total_balance1 =0
    total_balance2 =0
    current_total1 = 0
    current_total2 =0
    open_balance = 0
    closing_balance=0
    closing_balance_debit=0
    closing_balance_credit=0


    for i in lemo:
        if i.debit :

            total_debit +=  i.debit
        if i.credit :
            total_credit = total_credit + i.credit

        if i.Closing_balance :
            if i.type == "Dr":
                closing_balance_debit += i.Closing_balance
            else:
                closing_balance_credit += i.Closing_balance

    closing_balance  =  closing_balance_debit - closing_balance_credit 

     
    

    open_balance = le.ledger_opening_bal

    
    type =le.ledger_opening_bal_type
    
    if cash_bank_books_TotalClosing_balance.objects.filter(ledger=le_id):

        tc = cash_bank_books_TotalClosing_balance.objects.get(ledger=le_id)
        
        tcl = Account_Books_Ledger.objects.get(id=id)
        tc.ledger=tcl
        
        if closing_balance < 0:
            closing_balance = -1*closing_balance
            print(closing_balance)  
            tc.Total_Closing_balance = closing_balance
            tc.type="Cr"
        else:
            tc.Total_Closing_balance = closing_balance
            print(closing_balance)
            tc.type="Dr"

        tc.save()
        

        
    else:
        tc = cash_bank_books_TotalClosing_balance()
        tcl = Account_Books_Ledger.objects.get(id=id)
        tc.ledger=tcl
        if closing_balance == - closing_balance:
            closing_balance = -1*closing_balance
            tc.Total_Closing_balance = closing_balance
            tc.type="Cr"
        else:
            tc.Total_Closing_balance = closing_balance
            tc.type="Dr"

        tc.save()
          
    tc_type = cash_bank_books_TotalClosing_balance.objects.get(ledger=le_id)
    type1 = tc_type.type 
    


    context={
        'voucher' : voucher,
        'ledger' :ledger,
        'ledger_name':ledger_n,
        'total_debit':total_debit,
        'total_credit':total_credit,
        'current_total1':current_total1,
        'current_total2':current_total2,
        'open_balance':open_balance,
        'le_id' :le_id,
        'type':type,
        'mo':mo,
        'lemo':lemo,
        'le':le,
        'closing_balance':closing_balance,
        'type1':type1


    }

    

    return render(request,'cash_bank_books_ledger_monthly_summary.html',context) 

def cash_bank_books_ledger_show(request,id,pk):
    
    le = Account_Books_Ledger.objects.get(id=id)
    voucher = Account_books_Ledger_Voucher.objects.filter(ledger=le,month=pk)
    ledger = Account_Books_Ledger.objects.filter(id=le.id)
    
    ledger_n = le.ledger_name

    total_debit=0 
    total_credit=0 
    total_balance1 =0
    total_balance2 =0
    current_total1 = 0
    current_total2 =0
    for i in voucher:
        if i.Debit :

            total_debit +=  i.Debit
        if i.Credit :
            total_credit = total_credit + i.Credit


    total_balance1 = le.ledger_opening_bal+total_debit

    total_balance2 = le.ledger_opening_bal+total_credit

    
    if total_debit or total_credit!=0:
        if le.ledger_opening_bal_type =="Dr":
            current_total1 = total_balance1 - total_credit
            if (current_total1 < 0):
                current_total1 = -1*current_total1
                if cash_bank_books_Leger_Month_closing.objects.filter(Ledger=le,month=pk):
                    cl = cash_bank_books_Leger_Month_closing.objects.get(Ledger=le,month=pk)
                    cl.Ledger = le
                    mon = Months.objects.get(id=pk)
                    cl.month = mon 
                    cl.Closing_balance = current_total1
                    if total_balance1 >total_credit:
                        cl.type = 'Dr'
                    else:
                        cl.type = 'Cr'

                    cl.debit = total_debit
                    cl.credit =total_credit
                    cl.save()
                else:
                    cl = cash_bank_books_Leger_Month_closing()
                    cl.Ledger = le
                    mon = Months.objects.get(id=pk)
                    cl.month = mon 
                    cl.Closing_balance = current_total1
                    if total_balance1 >total_credit:
                        cl.type = 'Dr'
                    else:
                        cl.type = 'Cr'
                    cl.debit = total_debit
                    cl.credit =total_credit
                    cl.save()
            else:
                if cash_bank_books_Leger_Month_closing.objects.filter(Ledger=le,month=pk):
                    cl = cash_bank_books_Leger_Month_closing.objects.get(Ledger=le,month=pk)
                    cl.Ledger = le
                    mon = Months.objects.get(id=pk)
                    cl.month = mon 
                    cl.Closing_balance = current_total1
                    if total_balance1 >total_credit:
                        cl.type = 'Dr'
                    else:
                        cl.type = 'Cr'
                    cl.debit = total_debit
                    cl.credit =total_credit
                    cl.save()
                else:
                    cl = cash_bank_books_Leger_Month_closing()
                    cl.Ledger = le
                    mon = Months.objects.get(id=pk)
                    cl.month = mon 
                    cl.Closing_balance = current_total1
                    if total_balance1 >total_credit:
                        cl.type = 'Dr'
                    else:
                        cl.type = 'Cr'
                    cl.debit = total_debit
                    cl.credit =total_credit
                    cl.save() 
        else:
            if le.ledger_opening_bal_type =="Cr":
                current_total2 = total_balance2 - total_debit
                if (current_total2 < 0):
                    current_total2 = -1*current_total2
                    if cash_bank_books_Leger_Month_closing.objects.filter(Ledger=le,month=pk):
                        cl = cash_bank_books_Leger_Month_closing.objects.get(Ledger=le,month=pk)
                        cl.Ledger = le
                        mon = Months.objects.get(id=pk)
                        cl.month = mon 
                        cl.Closing_balance = current_total2
                        if total_balance2 >total_debit:
                            cl.type = 'Cr'
                        else:
                            cl.type = 'Dr'
                        cl.debit = total_debit
                        cl.credit =total_credit
                        cl.save()
                    else:
                        cl = cash_bank_books_Leger_Month_closing()
                        cl.Ledger = le
                        mon = Months.objects.get(id=pk)
                        cl.month = mon 
                        cl.Closing_balance = current_total2
                        if total_balance2 >total_debit:
                            cl.type = 'Cr'
                        else:
                            cl.type = 'Dr'
                        cl.debit = total_debit
                        cl.credit =total_credit
                        cl.save()
                else:
                    if cash_bank_books_Leger_Month_closing.objects.filter(Ledger=le,month=pk):
                        cl = cash_bank_books_Leger_Month_closing.objects.get(Ledger=le,month=pk)
                        cl.Ledger = le
                        mon = Months.objects.get(id=pk)
                        cl.month = mon 
                        cl.Closing_balance = current_total2
                        if total_balance2 >total_debit:
                            cl.type = 'Cr'
                        else:
                            cl.type = 'Dr'
                        cl.debit = total_debit
                        cl.credit =total_credit
                        cl.save()
                    else:
                        cl = cash_bank_books_Leger_Month_closing()
                        cl.Ledger = le
                        mon = Months.objects.get(id=pk)
                        cl.month = mon 
                        cl.Closing_balance = current_total2
                        if total_balance2 >total_debit:
                            cl.type = 'Cr'
                        else:
                            cl.type = 'Dr'
                        cl.debit = total_debit
                        cl.credit =total_credit
                        cl.save()





                
    type =""
    closing_balance =0
    if cash_bank_books_Leger_Month_closing.objects.filter(Ledger=le,month=pk):
        tcl1 = cash_bank_books_Leger_Month_closing.objects.get(Ledger=le,month=pk)
        type = tcl1.type
        closing_balance = tcl1.Closing_balance 


    context={
        'voucher' : voucher,
        'ledger' :ledger,
        'ledger_name':ledger_n,
        'total_debit':total_debit,
        'total_credit':total_credit,
        'current_total1':current_total1,
        'current_total2' :current_total2,
        "type1":type,
        'closing_balance':closing_balance,
        


    }
    

    return render(request,'cash_bank_books_ledger_show.html',context)  

# arif 

def Select_Group_Voucher(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
    # display=tally_group.objects.all()
        display=tally_group.objects.filter(company=t_id)
        context={'display':display}
        return render(request,'select_grp_vchr.html',context)

def Creat_Group_Voucher(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        # display=tally_group.objects.all()
        display=tally_group.objects.filter(company=t_id)
        context={'display':display}
        return render(request,'crt_grp_voucher.html',context)

def Group_Voucher_Create(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        if request.method =='POST':
            gname=request.POST['gname']
            galias=request.POST['alias']
            under=request.POST['group']
            nature=request.POST['group_nature']
            gross=request.POST['gorss_profit']
            ledg=request.POST['ledger']
            cred=request.POST['debit/credit']
            calc=request.POST['calculation']
            invc=request.POST['invoice']
            grp=tally_group(group_name=gname,
                group_alias=galias,
                group_under=under,
                nature=nature,
                gross_profit=gross,
                sub_ledger=ledg,
                debit_credit=cred,
                calculation=calc,
                invoice=invc,
                company_id=t_id
                )          
            grp.save()
            return redirect("Select_Group_Voucher")

def Group_Voucher(request,pk):
    display=Group_Voucher_Model.objects.filter(id=pk)
    sum1=0
    sum2=0
    sum3=0
    for i in display:
        sum1+=i.DEBIT
    for i in display:
        sum2+=i.Credit   
    for i in display:
        sum3+=i.Open_Balance
    sum4=sum3-(sum1-sum2)
    context={'display':display,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4}
    return render(request,'grp_voucher.html',context)

def Group_Voucher_Summary(request,pk):
    display=tally_group.objects.get(id=pk)
    data=First_Voucher_Summary_Model.objects.filter(Voucher_Name=display)
    sum1=0
    sum2=0
    for i in data:
        sum1+=i.Credit
    for i in data:
        sum2+=i.Debit
    context={'data':data,'display':display,'sum1':sum1,'sum2':sum2}
    return render(request,'grp_summary2.html',context)

def Voucher_Group_Summary(request,pk):
    display=First_Voucher_Summary_Model.objects.get(id=pk)
    data=Second_Voucher_Summary_Model.objects.filter(FVoucher_Name=display)
    sum1=0
    sum2=0
    for i in data:
        sum1+=i.Credit
    for i in data:
        sum2+=i.Debit
    context={'data':data,'display':display,'sum1':sum1,'sum2':sum2}
    return render(request,'vchr_grp_summary.html',context)

def Stock_Group_Summary(request,pk):
    display=tally_group.objects.all()
    data=Stock_Group_Summary_Model.objects.filter(id=pk)
    total=0
    for i in data:
        total+=i.Value
    context={"data":data,'display':display,'total':total}
    return render(request,'stock_grp_summary.html',context)

def Stock_Group_Summary_Product(request,pk):
    display=Stock_Group_Summary_Model.objects.get(id=pk)
    data=Product_Stock_Group_Summary_Model.objects.filter(PStock_Voucher_Forgn=display)
    total=0
    for i in data:
        total+=i.Value
    context={"data":data,'display':display,'total':total}
    return render(request,'stock_grp_summary2.html',context)

def Stock_Item_Monthly_Summary(request,pk):
    display=Product_Stock_Group_Summary_Model.objects.get(id=pk)
    data=Stock_Item_Monthly_Summary_Model.objects.filter(Pro_Stock_Voucher_Forgn=display)
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    sum7=0
    sum8=0
    mon1=('April')
    mon2=('May')
    mon3=('June')
    mon4=('July')
    mon5=('August')
    mon6=('Septemper')
    mon7=('October')
    mon8=('November')
    mon9=('December')
    mon10=('January')
    mon11=('Februery')
    mon12=('March')
    for  i in data:
        if i.Particular == mon1:
            mon1 = ''
        if i.Particular == mon2:
            mon2 = ''
        if i.Particular == mon3:
            mon3 = ''
        if i.Particular == mon4:
            mon4 = ''
        if i.Particular == mon5:
            mon5 = ''
        if i.Particular == mon6:
            mon6 = ''
        if i.Particular == mon7:
            mon7 = ''
        if i.Particular == mon8:
            mon8 = ''
        if i.Particular == mon9:
            mon9 = ''
        if i.Particular == mon10:
            mon10 = ''
        if i.Particular == mon11:
            mon11 = ''
        if i.Particular == mon12:
            mon12 = ''
    for i in data:
        sum1+=i.Open_Balance_Qty
    for i in data:
        sum2+=i.Open_Balance_Value
    for i in data:
        sum3+=i.Inwards_Qty
    for i in data:
        sum4+=i.Inwards_Vlu
    for i in data:
        sum5+=i.Outwards_Qty
    for i in data:
        sum6+=i.Outwards_Vlu
    for i in data:
        sum7+=i.Closing_Bal_Qty
    for i in data:
        sum8+=i.Closing_Bal_Vlu
    context={"data":data,'display':display,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum5':sum5,'sum6':sum6,'sum7':sum7,'sum8':sum8,'mon1':mon1,
            'mon2':mon2,
            'mon3':mon3,
            'mon4':mon4,
            'mon5':mon5,
            'mon6':mon6,
            'mon7':mon7,
            'mon8':mon8,
            'mon9':mon9,
            'mon10':mon10,
            'mon11':mon11,
            'mon12':mon12}
    return render(request,'stk_itm_mntly_sumry.html',context)

def Stock_Item_Voucher(request,pk):
    display=Stock_Item_Monthly_Summary_Model.objects.get(id=pk)
    data=Stock_Item_Voucher_Model.objects.filter(Pro_Stock_Forgn=display)
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    for i in data:
        sum1+=i.Inwards_Qty
    for i in data:
        sum2+=i.Inwards_Vlu
    for i in data:
        sum3+=i.Outwards_Qty
    for i in data:
        sum4+=i.Outwards_Vlu
    for i in data:
        sum5+=i.Pro_Stock_Forgn.Closing_Bal_Qty
    for i in data:
        sum6+=i.Pro_Stock_Forgn.Closing_Bal_Vlu 
    context={"data":data,'display':display,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum5':sum5,'sum6':sum6}
    return render(request,'stock_item_voucher.html',context)

def Select_Groups(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        # display=tally_group.objects.all()
        display=tally_group.objects.filter(company=t_id)
        context={'display':display}
        return render(request,'select_grp.html',context)

def Creat_Group_Summary(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        # display=tally_group.objects.all()
        display=tally_group.objects.filter(company=t_id)
        context={'display':display}
        return render(request,'crt_grp_sumry.html',context)

def Group_Summary_Create(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        if request.method=='POST':
            gname=request.POST['gname']
            galias=request.POST['alias']
            under=request.POST['group']
            nature=request.POST['group_nature']
            gross=request.POST['gorss_profit']
            ledg=request.POST['ledger']
            cred=request.POST['debit/credit']
            calc=request.POST['calculation']
            invc=request.POST['invoice']
            grp=tally_group(group_name=gname,
                    group_alias=galias,
                    group_under=under,
                    nature=nature,
                    gross_profit=gross,
                    sub_ledger=ledg,
                    debit_credit=cred,
                    calculation=calc,
                    invoice=invc,
                    company_id=t_id
                    )          
            grp.save()
            return redirect('Select_Groups')

def Group_Summary(request,pk):
    display=tally_group.objects.get(id=pk)
    data=First_Group_Summary_Model.objects.filter(Group_Name=display)
    sum1=0
    sum2=0
    for i in data:
        sum1+=i.Credit
    for i in data:
        sum2+=i.Debit
    context={'data':data,'display':display,'sum1':sum1,'sum2':sum2}
    return render(request,'grp_summary.html',context)

def Sec_Group_Summary(request,pk):
    display=First_Group_Summary_Model.objects.get(id=pk)
    data=Second_Group_Summary_Model.objects.filter(Fgroup_Forng=display)

    sum1=0
    sum2=0
    for i in data:
        sum1+=i.Fgroup_Forng.Credit
    for i in data:
        sum2+=i.Fgroup_Forng.Debit
    context={'data':data,'display':display,'sum1':sum1,'sum2':sum2}

    return render(request,'secgrp_sumry.html',context)

def Thrd_Group_Summary(request,pk):
    display=Second_Group_Summary_Model.objects.get(id=pk)
    data=Third_Group_Summary_Model.objects.filter(Sgroup_Forng=display)
    sum1=0
    sum2=0
    for i in data:
        sum1+=i.Sgroup_Forng.Fgroup_Forng.Credit
    for i in data:
        sum2+=i.Sgroup_Forng.Fgroup_Forng.Debit
    context={'data':data,'display':display,'sum1':sum1,'sum2':sum2}
    return render(request,'trdgrp_sumry.html',context)

def Ledger_Monthly_Summary(request,pk):
    Display=Third_Group_Summary_Model.objects.get(id=pk)
    month=Months.objects.all()
    # month=Months.objects.get(month_name='April')
    # m1=Months.objects.get(month_name='')   
    data=Ledger_Monthly_Summary_Model.objects.filter(Tgroup_Forgn=Display)
    mon1=('April')
    mon2=('May')
    mon3=('June')
    mon4=('July')
    mon5=('August')
    mon6=('Septemper')
    mon7=('October')
    mon8=('November')
    mon9=('December')
    mon10=('January')
    mon11=('Februery')
    mon12=('March')
    for  i in data:
        if i.Particular == mon1:
            mon1 = ''
        if i.Particular == mon2:
            mon2 = ''
        if i.Particular == mon3:
            mon3 = ''
        if i.Particular == mon4:
            mon4 = ''
        if i.Particular == mon5:
            mon5 = ''
        if i.Particular == mon6:
            mon6 = ''
        if i.Particular == mon7:
            mon7 = ''
        if i.Particular == mon8:
            mon8 = ''
        if i.Particular == mon9:
            mon9 = ''
        if i.Particular == mon10:
            mon10 = ''
        if i.Particular == mon11:
            mon11 = ''
        if i.Particular == mon12:
            mon12 = ''
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    for a in data:
        sum1 += a.Credit
    for b in data:
        sum2 += b.Dedit
    
    for d in data:
        sum4 += d.Open_Balance

    for c in data:
        sum3 += c.Closing_Balance

    sum5 = sum3 + sum4
    context={"data":data,
            'Display':Display,
            'sum1':sum1,
            'sum2':sum2,
            'sum3':sum3,
            'sum4':sum4,
            'sum5':sum5,
            'month':month,
            'mon1':mon1,
            'mon2':mon2,
            'mon3':mon3,
            'mon4':mon4,
            'mon5':mon5,
            'mon6':mon6,
            'mon7':mon7,
            'mon8':mon8,
            'mon9':mon9,
            'mon10':mon10,
            'mon11':mon11,
            'mon12':mon12}
    return render(request,'ledgr_grp_summary.html',context)

def Ledger_Voucher(request,pk):
    display=Ledger_Voucher_Model.objects.all()
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    for a in display:
        sum1+=a.Debit
    for a in display:
        sum2+=a.Credit
    for a in display:
        sum3+=a.Open_Balance
    # for a in display:
    #     sum4+=a.
    sum4=(sum2-sum1)+sum3
    

    context={'display':display,'sum1':sum1,'sum2':sum2,"sum3":sum3,'sum4':sum4}
    return render(request,'ledgr_voucher.html',context)



# .........................................AMAL K V ......................................................................................
def alter_payrol_emp_add2(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        emp=Create_employeegroup.objects.filter(status=0)
        emp1=Create_employeegroup.objects.filter(company_id=t_id)
        return render(request,'alter_payrol_employegroup2.html',{'data':emp,'tally':tally,'emp1':emp1}) 
    return redirect('/') 

def alter_payrol_emp_gredit(request,pk):
    data=Create_employeegroup.objects.get(id=pk)
    data2=Create_employeegroup.objects.all()
    context={'p1':data,
    'emp':data2}
    return render(request,'alter_payrol_gredit.html',context) 

def alter_payrol_emp_gredit2(request,pk):
    if request.method=='POST':
        datas=Create_employeegroup.objects.get(id=pk)
        datas.name =request.POST.get('name')
        datas.alias = request.POST.get('alias')
        datas.under = request.POST.get('under')
        datas.define_salary = request.POST.get('sal')
        

        datas.save()
        return redirect('alter_payrol_emp_add2')

def alter_payrol_employee(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    p3=Employee.objects.filter(company_id=t_id)
    context={'data':p3}
    return render(request,'alter_payrol_employe2.html',context)

def alter_payrol_employee_edit(request,pk):
    std=Create_employeegroup.objects.all()
    p=Employee.objects.get(id=pk)
    p1=add_bank.objects.get(id=pk)
    p2=E_found_trasfer.objects.get(id=pk)
    return render(request,'alter_payrol_employee_edit.html',{'std':std,'p':p,'p1':p1,'p2':p2})

def alter_payrol_employee_edit2(request,pk):
    std=Employee.objects.get(id=pk)
    std.name=request.POST.get('name')
    std.alias=request.POST.get('alias')
    std.under=request.POST.get('under')
    std.date_join=request.POST.get('join')
    std.defn_sal=request.POST.get('sal')
    std.emp_name=request.POST.get('empname')
    std.emp_desg=request.POST.get('desig')
    std.fnctn=request.POST.get('fn')
    std.location=request.POST.get('loc')
    std.gender=request.POST.get('gen')
    std.dob=request.POST.get('dob')
    std.blood=request.POST.get('blood')
    std.parent_name=request.POST.get('prnts')
    std.spouse_name=request.POST.get('spouse')
    std.address=request.POST.get('adrs')
    std.number=request.POST.get('phone')
    std.email=request.POST.get('email')
    std.inc_tax_no=request.POST.get('taxno')
    std.aadhar_no=request.POST.get('aadhar')
    
    std.uan=request.POST.get('uan')
    std.pfn=request.POST.get('pfn')
    std.pran=request.POST.get('pran')
    std.esin=request.POST.get('esin')
    std.bankdtls=request.POST.get('bank')
    std.save()

    std1=add_bank.objects.get(id=pk)
    std1.Acount_No=request.POST.get('acount')
    std1.IFSC_code=request.POST.get('ifsc')
    std1.Bank_name=request.POST.get('bank_name')
    std1.Branch_name=request.POST.get('branch_name')
    std1.Transaction_type=request.POST.get('Transaction_type')
    std1.save()

    std2=add_bank.objects.get(id=pk)
    std2.Acount_No=request.POST.get('acnumber')
    std2.IFSC_code=request.POST.get('ifsccode')
    std2.Bank_name=request.POST.get('bank_name2')
    std2.Cheque=request.POST.get('cheque')
    std2.save()
    
    return redirect('alter_payrol_employee')


def alter_payrol_unit2(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        p=units.objects.filter(company_id=t_id)
    return render(request,'alter_payrol_unit2.html',{'data':p})

def alter_payrol_unit_edit(request,pk):
    uq=unitQuantityCode.objects.all()
    ps=units.objects.all()
    std=units.objects.get(id=pk)
    return render(request,'alter_payrol_unit_edit.html',{'ps':ps,'uq':uq,'std':std})

def alter_payrol_unit_edit2(request,pk):
    std=units.objects.get(id=pk)
    std.type=request.POST.get('type')
    std.symbol=request.POST.get('symbol')  
    std.formal_name=request.POST.get('formal')
    std.uqc1=request.POST.get('uqc1')
    std.number_of_decimal_places=request.POST.get('decimal') 
    std.first_unit=request.POST.get('ft1')
    std.conversion=request.POST.get('con')
    std.second_unit=request.POST.get('sec')  
    std.save()
    print('hai')
    return redirect('alter_payrol_unit2')

def alter_payrol_attendence(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    data=Create_attendence.objects.filter(company_id=t_id)
    return render(request,'alter_payrol_attendence2.html',{'p':data})

def alter_payrol_attendence_edit(request,pk):
    data=Create_attendence.objects.get(id=pk)
    data2=Create_attendence.objects.all()
    pk=units.objects.all()
    context={'p':data,
    'std':data2,'pk':pk}
    return render(request,'alter_payrol_attendence_edit.html',context) 

def alter_payrol_attendence_edit2(request,pk):
    if request.method == 'POST':
        data=Create_attendence.objects.get(id=pk)
        data.name=request.POST.get('name')
        data.alias=request.POST.get('alias')
        data.under=request.POST.get('under')
        data.type=request.POST.get('type')
        data.period=request.POST.get('period')
        data.units=request.POST.get('units1')
        data.save()
        return redirect('alter_payrol_attendence')

def alter_payrol_payheads(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        data=create_payhead.objects.filter(company_id=t_id)
    return render(request,'alter_payrol_payheads2.html',{'p':data})  

def alter_payrol_payhead_edit2(request,pk):
    if request.method=='POST':
        data=create_payhead.objects.get(id=pk)
        data.name=request.POST.get('name')
        data.alias=request.POST.get('alias')
        data.pay_type=request.POST.get('payhead')
        data.income_type=request.POST.get('income')
        data.under=request.POST.get('under')
        data.affect_net=request.POST.get('netsalary')
        data.payslip=request.POST.get('payslip')
        data.calculation_of_gratuity=request.POST.get('caltype')
        data.cal_type=request.POST.get('ctype')
        data.calculation_period=request.POST.get('caltype')
        data.leave_withpay=request.POST.get('attendence with pay')
        data.leave_with_out_pay=request.POST.get('Attendance with out pay')
        data.production_type=request.POST.get('ptype')
        data.opening_balance=request.POST.get('balance')
        data.save()

        idd=data

        data2=compute_information.objects.get(id=pk)
        data2.compute=request.POST.get('compute')
        data2.effective_from=request.POST.get('effective_from')
        data2.amount_upto=request.POST.get('amount_upto')
        data2.slab_type=request.POST.get('slab_type')
        data2.value=request.POST.get('value')
        data2.Pay_head_id=idd

        data2.save()


        data3=Rounding.objects.get(id=pk)
        data3.Rounding_Method=request.POST.get('roundmethod')
        data3.Round_limit=request.POST.get('limit')
        data3.pay_head_id=idd
        data3.save()

        data4=gratuity.objects.get(id=pk)
        data4.days_of_months=request.POST.get('days_of_months')
        data4.number_of_months_from=request.POST.get('from')
        data4.to=request.POST.get('to')
        data4.calculation_per_year=request.POST.get('eligiibility')
        data4.pay_head_id=idd
        data4.save()
        return redirect('alter_payrol_payheads')
    return render(request,'alter_payrol_payhead_edit.html')
    

def alter_payrol_payhead_edit(request,pk):
    data=create_payhead.objects.get(id=pk)
    data2=compute_information.objects.get(id=pk)
    data3=Rounding.objects.get(id=pk)
    data4=gratuity.objects.get(id=pk)
    context={'p':data,'p2':data2,
    'p3':data3,'p4':data4
    }
    return render(request,'alter_payrol_payhead_edit.html',context) 


def alter_payrol_add_voucher2(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        emp=create_VoucherModels.objects.filter(company_id=t_id)
    return render(request,'alter_payrol_payroll2.html',{'data':emp}) 

def alter_payrol_add_voucher_edit(request,pk):
    emp=create_VoucherModels.objects.get(id=pk)
    data2=create_VoucherModels.objects.all()
    context={'p':emp,
    'data':data2}
    return render(request,'alter_payrol_payrolledit.html',context) 

def alter_payrol_add_voucher_edit2(request,pk):
    emp=create_VoucherModels.objects.get(id=pk)
    emp.voucher_name=request.POST.get('name')
    emp.alias=request.POST.get('alias')
    emp.voucher_type=request.POST.get('type')
    emp.abbreviation=request.POST.get('abber')
    emp.active_this_voucher_type=request.POST.get('active')
    emp.method_voucher_numbering=request.POST.get('numbering')
    emp.use_adv_conf=request.POST.get('config', False)
    emp.prvnt_duplictes=request.POST.get('prevent', False)
    emp.use_effective_date=request.POST.get('effect')
    emp.allow_zero_value_trns=request.POST.get('trans')
    emp.allow_naration_in_voucher=request.POST.get('narr')
    emp.make_optional=request.POST.get('optical')
    emp.provide_naration=request.POST.get('ledg')
    emp.print_voucher=request.POST.get('print')
    emp.save()
    return redirect('alter_payrol_add_voucher2')


    # ----------------------------AMAYA---------------------------------------

def voucheradd(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        led=tally_ledger.objects.filter(status=0)
        led1=tally_ledger.objects.filter(company_id=t_id)
        context={'led':led,'led1':led1}
    return render(request,'voucheradd.html',context)    

def vouchadd(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method == 'POST':
            vdate=request.POST['vdate']
            particular=request.POST['particular']
            account=request.POST['account']
            vouchertype=request.POST['vouchertype']
            voucherno=request.POST['voucherno']
            openingbal=request.POST['openingbal']
            
            
            debit=request.POST['debit']
        
            credit=request.POST['credit']
            

            vou=vouchert(
                vdate=vdate,
                particular=particular,
                account=account,
                vouchertype=vouchertype,
                voucherno=voucherno,
                debit=debit,
                credit=credit,
                openingbal=openingbal,
                company_id=t_id
                

            )
            vou.save()
            return render(request,'voucheradd.html',{'tally':tally})
    return redirect('/')       


def groupsummery(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        
   
        vouch=vouchert.objects.filter(company_id=t_id)

        sum1=0
        sum2=0
        sum3=0
        for a in vouch:
            sum1+=a.credit

        for b in vouch:
            sum2+=b.debit

        for c in vouch:
            sum3+=c.openingbal   

        tot=sum1+sum2 
        cltot=tot-sum3     

        context={'vouch':vouch,'sum1':sum1,'sum2':sum2,'tot':tot,'cltot':cltot}    
        return render(request,'groupsummery.html',context)        
    return redirect('/')

def ledgersummary(request,pk):
    vch=vouchert.objects.get(id=pk)  
    vouch=vouchert.objects.filter(id=pk)

    sum1=0
    sum2=0
    sum3=0
    for a in vouch:
        sum1+=a.credit

    for b in vouch:
        sum2+=b.debit 

    

    for c in vouch:
        sum3+=c.openingbal   

    tot=sum1+sum2 
    cltot=tot-sum3  
      
    
    context={'vch':vch,'vouch':vouch,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum3':sum3,'tot':tot,'cltot':cltot}      
    return render(request,'ledgersummary.html',context)    

def ledgervoucher(request,pk):
    vch=vouchert.objects.get(id=pk)
    vouch=vouchert.objects.filter(id=pk)

    sum1=0
    sum2=0
    sum3=0

    for a in vouch:
        sum1+=a.credit

    for b in vouch:
        sum2+=b.debit  

    for c in vouch:
        sum3+=c.openingbal   

    tot=sum1+sum2 
    cltot=tot-sum3  

        
    context={'vch':vch,'vouch':vouch,'sum1':sum1,'sum2':sum2,'sum3':sum3,'tot':tot,'cltot':cltot}     
    return render(request,'ledgervoucher.html',context)      

def ex(request):
    return render(request,'ex.html')  






def voucher2(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        led=tally_ledger.objects.filter(status=0)
        led1=tally_ledger.objects.filter(company_id=t_id)
        context={'led':led,'led1':led1}   
    return render(request,'loanvoucher.html',context)    

def loanvouchadd(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method == 'POST':
            ivdate=request.POST['ivdate']
            iparticular=request.POST['iparticular']
            iaccount=request.POST['iaccount']
            ivouchertype=request.POST['ivouchertype']
            ivoucherno=request.POST['ivoucherno']
            
            idebit=request.POST['idebit']
        
            icredit=request.POST['icredit']
            

            voui=lvouchert(
                ivdate=ivdate,
                iparticular=iparticular,
                iaccount=iaccount,
                ivouchertype=ivouchertype,
                ivoucherno=ivoucherno,
                idebit=idebit,
                icredit=icredit,
                company_id=t_id
            )
            voui.save()
            return redirect('voucher3')
    return redirect('/')  

def loangroupsummary(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id) 
        vouch=lvouchert.objects.filter(company_id=t_id)

        sum1=0
        sum2=0
        for a in vouch:
            sum1+=a.icredit
            
        for b in vouch:
            sum2+=b.idebit

        context={'vouch':vouch,'sum1':sum1,'sum2':sum2}    
        return render(request,'loangroupsummary.html',context)

def loanledgersummary(request,pk):
    vch=lvouchert.objects.get(id=pk)
    vouch=lvouchert.objects.filter(id=pk)

    sum1=0
    sum2=0
    

    for a in vouch:
        sum1+=a.icredit

    for b in vouch:
        sum2+=b.idebit 

    clsum=sum1+sum2       
        
    context={'vch':vch,'vouch':vouch,'sum1':sum1,'sum2':sum2,'clsum':clsum}   
    return render(request,'loanledgersummary.html',context) 


def loanledgervoucher(request,pk):
    vch=lvouchert.objects.get(id=pk)
    vouch=lvouchert.objects.filter(id=pk)

    sum1=0
    sum2=0

    for a in vouch:
        sum1+=a.icredit

    for b in vouch:
        sum2+=b.idebit 

    context={'vch':vch,'vouch':vouch,'sum1':sum1,'sum2':sum2}     
    return render(request,'loanledgervoucher.html',context)    






def voucher3(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        led=tally_ledger.objects.filter(status=0)
        led1=tally_ledger.objects.filter(company_id=t_id)
        context={'led':led,'led1':led1}       
    return render(request,'cvoucher.html',context)    

def cvouchadd(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method == 'POST':
            ivdate=request.POST['ivdate']
            iparticular=request.POST['iparticular']
            iaccount=request.POST['iaccount']
            ivouchertype=request.POST['ivouchertype']
            ivoucherno=request.POST['ivoucherno']
            iopeningbal=request.POST['iopeningbal']
            idebit=request.POST['idebit']
        
            icredit=request.POST['icredit']
            

            voui=cvouchert(
                ivdate=ivdate,
                iparticular=iparticular,
                iaccount=iaccount,
                ivouchertype=ivouchertype,
                ivoucherno=ivoucherno,
                iopeningbal=iopeningbal,
                idebit=idebit,
                icredit=icredit,
                company_id=t_id

            )
            voui.save()
            return redirect('voucher3') 
    return redirect('/')  
 


def cgroup(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        grp=tally_group.objects.filter(company_id=t_id)
        vouch=cvouchert.objects.all()
        sum1=0
        sum2=0
        sum3=0

        for a in vouch:
            sum1+=a.icredit

        for b in vouch:
            sum2+=b.idebit

        for c in vouch:
            sum3+=c.iopeningbal   

        clsum=sum1+sum2
        cltot=clsum-sum3 

        context={'vouch':vouch,'grp':grp,'sum1':sum1,'sum2':sum2,'sum3':sum3,'clsum':clsum,'cltot':cltot}        

        return render(request,'cgroup.html',context)  

def cgroupsummary(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id) 
        vouch=cvouchert.objects.filter(company_id=t_id)
        sum1=0
        sum2=0
        sum3=0

        for a in vouch:
            sum1+=a.icredit

        for b in vouch:
            sum2+=b.idebit

        for c in vouch:
            sum3+=c.iopeningbal   

        clsum=sum1+sum2
        cltot=clsum-sum3 

        context={'vouch':vouch,'sum1':sum1,'sum2':sum2,'sum3':sum3,'clsum':clsum,'cltot':cltot}        

        return render(request,'cgroupsummary.html',context)  


def cledgersummary(request,pk):
    vch=cvouchert.objects.get(id=pk)
    vouch=cvouchert.objects.filter(id=pk)

    sum1=0
    sum2=0
    sum3=0

    for a in vouch:
        sum1+=a.icredit

    for b in vouch:
        sum2+=b.idebit

    for c in vouch:
        sum3+=c.iopeningbal   

    clsum=sum1+sum2
    cltot=clsum-sum3 


    context={'vch':vch,'vouch':vouch,'sum1':sum1,'sum2':sum2,'clsum':clsum,'cltot':cltot}
    return render(request,'cledgersummary.html',context)

def cledgervoucher(request,pk):
    vch=cvouchert.objects.get(id=pk)
    vouch=cvouchert.objects.filter(id=pk)

    sum1=0
    sum2=0
    sum3=0
    for a in vouch:
        sum1+=a.icredit

    for b in vouch:
        sum2+=b.idebit 
    for c in vouch:
        sum3+=c.iopeningbal   

    clsum=sum1+sum2
    cltot=clsum-sum3   

    context={'vch':vch,'sum1':sum1,'sum2':sum2,'sum3':sum3,'clsum':clsum,'cltot':cltot}
    return render(request,'cledgervoucher.html',context)





def trialbalance(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        total=vouchert.objects.filter(company_id=t_id)

        sum1=0
        sum2=0
        sum3=0

        for a in total:
            sum1+=a.credit

        for b in total:
            sum2+=b.debit  

        for c in total:
            sum3+=c.openingbal   

        tot=sum1+sum2 
        cltot=tot-sum3  

        totinc=lvouchert.objects.filter(company_id=t_id)
        

        sm3=0
        sum4=0
        

        for a in totinc:
            sm3+=a.icredit

        for b in totinc:
            sum4+=b.idebit

        totinx=cvouchert.objects.filter(company_id=t_id)

        sum6=0
        sum7=0
        sum8=0

        for a in totinx:
            sum6+=a.icredit

        for b in totinx:
            sum7+=b.idebit   

        for c in totinx:
            sum8+=c.iopeningbal   

        clsum=sum6+sum7 
        ctot=clsum-sum8

        
        crtot=sum1+sum3+sum6
        drtot=sum2+sum4+sum7
        diff=crtot-drtot

        



        context={'total':total,'totinc':totinc,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sm3':sm3,'sum4':sum4,'sum6':sum6,'sum7':sum7,'sum8':sum8,'totinx':totinx,
        'tot':tot,'cltot':cltot,'clsum':clsum,'ctot':ctot,
        'crtot':crtot,'drtot':drtot,'diff':diff}
        return render(request,'trialbalance.html',context)
    return redirect('/')
