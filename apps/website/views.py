from django.shortcuts import render, redirect

def pat_home_redirect(request):
    return redirect('/patients-and-caregivers/pages/home')

def pat_home(request):
    template = "website/base/pat-home.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/base/pat-home.html"
    return render(request, template)

def pat_needs_home(request):
    template = "website/needs/pat-needs-home.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/needs/pat-needs-home.html"
    return render(request, template)

def pat_needs_explained(request):
    template = "website/needs/pat-needs-explained.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/needs/pat-needs-explained.html"
    return render(request, template)

def pat_needs_need(request):
    template = "website/needs/pat-needs-need.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/needs/pat-needs-need.html"
    return render(request, template)

def pat_needs_paid(request):
    template = "website/needs/pat-needs-paid.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/needs/pat-needs-paid.html"
    return render(request, template)

def pat_needs_choice(request):
    template = "website/needs/pat-needs-choice.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/needs/pat-needs-choice.html"
    return render(request, template)

def pat_services_home(request):
    template = "website/services/pat-services-home.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/services/pat-services-home.html"
    return render(request, template)

def pat_services_care(request):
    template = "website/services/pat-services-care.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/services/pat-services-care.html"
    return render(request, template)

def pat_services_quality(request):
    template = "website/services/pat-services-quality.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/services/pat-services-quality.html"
    return render(request, template)

def pat_services_guide(request):
    template = "website/services/pat-services-guide.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/services/pat-services-guide.html"
    return render(request, template)

def pat_grief_home(request):
    template = "website/grief/pat-grief-home.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/grief/pat-grief-home.html"
    return render(request, template)

def pat_grief_resources(request):
    template = "website/grief/pat-grief-resources.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/grief/pat-grief-resources.html"
    return render(request, template)

def pat_grief_reading(request):
    template = "website/grief/pat-grief-reading.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/grief/pat-grief-reading.html"
    return render(request, template)

def pat_grief_FAQ(request):
    template = "website/grief/pat-grief-faq.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/grief/pat-grief-faq.html"
    return render(request, template)

def pat_volunteer_home(request):
    template = "website/volunteer/pat-volunteer-home.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/volunteer/pat-volunteer-home.html"
    return render(request, template)

def pat_volunteer_prospective(request):
    template = "website/volunteer/pat-volunteer-prospective.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/volunteer/pat-volunteer-prospective.html"  
    return render(request, template)

def pat_news_home(request):
    template = "website/news/pat-news-home.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/pat-news-home.html"
    return render(request, template)

def pat_news_j(request):
    template = "website/news/pat-news-journey.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/pat-news-journey.html"
    return render(request, template)

def pat_news_j_myth(request):
    template = "website/news/journey/pat-news-myth.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/journey/pat-news-myth.html"
    return render(request, template)

def pat_news_ab(request):
    template = "website/news/pat-news-grief.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/pat-news-grief.html"
    return render(request, template)

def pat_news_ab_men(request):
    template = "website/news/grief/pat-news-men.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-men.html"
    return render(request, template)

def pat_news_ab_overdose(request):
    template = "website/news/grief/pat-news-overdose.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-overdose.html"
    return render(request, template)

def pat_news_ab_suicide(request):
    template = "website/news/grief/pat-news-suicide.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-suicide.html"
    return render(request, template)

def pat_news_ab_substance(request):
    template = "website/news/grief/pat-news-substance.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-substance.html"
    return render(request, template)

def pat_news_ab_pregnancy(request):
    template = "website/news/grief/pat-news-pregnancy.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-pregnancy.html"
    return render(request, template)

def pat_news_ab_lonely(request):
    template = "website/news/grief/pat-news-lonely.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-lonely.html"
    return render(request, template)

def pat_news_ab_death(request):
    template = "website/news/grief/pat-news-death.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-death.html"
    return render(request, template)

def pat_news_ab_mindful(request):
    template = "website/news/grief/pat-news-mindful.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-mindful.html"
    return render(request, template)

def pat_news_ab_school(request):
    template = "website/news/grief/pat-news-school.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-school.html"
    return render(request, template)

def pat_news_ab_teen(request):
    template = "website/news/grief/pat-news-teen.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-teen.html"
    return render(request, template)

def pat_news_ab_college(request):
    template = "website/news/grief/pat-news-college.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-college.html"
    return render(request, template)

def pat_news_ab_olderadult(request):
    template = "website/news/grief/pat-news-olderadult.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-olderadult.html"
    return render(request, template)

def pat_news_ab_homocide(request):
    template = "website/news/grief/pat-news-homocide.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-homocide.html"
    return render(request, template)

def pat_news_ab_petloss(request):
    template = "website/news/grief/pat-news-petloss.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-petloss.html"
    return render(request, template)

def pat_news_ab_online(request):
    template = "website/news/grief/pat-news-online.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/grief/pat-news-online.html"
    return render(request, template)

def pat_news_cc(request):
    template = "website/news/pat-news-connection.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/news/pat-news-connection.html"
    return render(request, template)

def pat_giving_home(request):
    template = "website/giving/pat-giving-home.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/giving/pat-giving-home.html"
    return render(request, template)

def pat_giving_gift(request):
    template = "website/giving/pat-giving-gift.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/giving/pat-giving-gift.html"
    return render(request, template)

def pat_giving_supporters(request):
    template = "website/giving/pat-giving-supporters.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/giving/pat-giving-supporters.html"
    return render(request, template)

def pat_giving_charity(request):
    template = "website/giving/pat-giving-charity.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/giving/pat-giving-charity.html"
    return render(request, template)

def pat_giving_wish(request):
    template = "website/giving/pat-giving-wish.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/giving/pat-giving-wish.html"
    return render(request, template)

def pat_contact_home(request):
    template = "website/contact/pat-contact-home.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/contact/pat-contact-home.html"
    return render(request, template)

def prof_home(request):
    template = "website/base/prof-home.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/base/prof-home.html"
    return render(request, template)

def prof_reimbursement(request):
    template = "website/base/prof-reimbursement.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/base/prof-reimbursement.html"
    return render(request, template)

def prof_refer_home(request):
    template = "website/refer/prof-refer-home.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/refer/prof-refer-home.html"
    return render(request, template)

def prof_refer_admission(request):
    template = "website/refer/prof-refer-admission.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/refer/prof-refer-admission.html"
    return render(request, template)

def prof_refer_care(request):
    template = "website/refer/prof-refer-care.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet:
        template = "mobile/refer/prof-refer-care.html"
    return render(request, template)

def prof_refer_quality(request):
    template = "website/refer/prof-refer-quality.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet:
        template = "mobile/refer/prof-refer-quality.html"
    return render(request, template)

def prof_careers_home(request):
    template = "website/careers/prof-careers-home.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/careers/prof-careers-home.html"
    return render(request, template)

def prof_careers_jobs(request):
    template = "website/careers/prof-careers-jobs.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/careers/prof-careers-jobs.html"
    return render(request, template)

def footer_about(request):
    template = "website/about/pat-about-home.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/about/pat-about-home.html"
    return render(request, template)

def footer_history(request):
    template = "website/about/pat-about-history.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/about/pat-about-history.html"
    return render(request, template)

def footer_nds(request):
    template = "website/about/pat-about-nds.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/about/pat-about-nds.html"
    return render(request, template)

def footer_npp(request):
    template = "website/about/pat-about-npp.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/about/pat-about-npp.html"
    return render(request, template)

def footer_ac(request):
    template = "website/about/pat-about-ac.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/about/pat-about-ac.html"
    return render(request, template)

def footer_la(request):
    template = "website/about/pat-about-la.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/about/pat-about-la.html"
    return render(request, template)

def footer_cp(request):
    template = "website/about/pat-about-cp.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/about/pat-about-cp.html"
    return render(request, template)

def footer_sitemap(request):
    template = "website/about/pat-about-sitemap.html"
    if request.user_agent.is_mobile or request.user_agent.is_tablet: 
        template = "mobile/about/pat-about-sitemap.html"
    return render(request, template)
