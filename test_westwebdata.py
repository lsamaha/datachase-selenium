__author__ = 'lsamaha'

import unittest
from westwebdata import *


class TestWestWebDat(unittest.TestCase):

    def test_parse_westlaw_html(self):
        data = parse_westlaw_html(sample_html)
        self.assertIn('filedate', data)
        self.assertEquals('07/22/2015', data['filedate'])
        self.assertIsNotNone(data['court'])
        self.assertIsNotNone(data['panel'])
        self.assertEquals(len(data['panel']), 3)
        self.assertEquals(data['panel'][0], 'THOMAS')
        self.assertIsNotNone(data['decision'])
        self.assertEquals(48, len(data['decision']))
        with self.assertRaises(ValueError):
            parse_westlaw_html('')
        with self.assertRaises(ValueError):
            parse_westlaw_html(None)
        with self.assertRaises(ValueError):
            parse_westlaw_html('<a></b>')
        self.assertIsNotNone(parse_westlaw_html('<html><title>a</title></html>'))
        self.assertEquals('A Title', parse_westlaw_html('<html><title>A Title</title></html>')['title'])
        self.assertIsNotNone(get_by_id(get_dom(sample_html), 'span', 'filedate'))


sample_html2 = '''
<html><title>a</title></html>
'''

sample_html = '''
<html xmlns="http://www.w3.org/1999/xhtml">

<head id="ctl00_ctl00_coid_website_head" profile="http://www.w3.org/2005/10/profile"><meta http-equiv="content-type" content="text/html; charset=UTF-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=IE6" /><title>

Crazy Ely Western Village, LLC v. City of Las Vegas - Westlaw

</title><link href='https://ca.next.westlaw.com/StaticContent_32.0.2006/css/v2/utilities.css' type='text/css' rel='stylesheet' /><link href='https://ca.next.westlaw.com/StaticContent_32.0.2006/css/v2/core.css' type='text/css' rel='stylesheet' /><link href='https://ca.next.westlaw.com/StaticContent_32.0.2006/css/v2/components.css' type='text/css' rel='stylesheet' /><link href='https://ca.next.westlaw.com/StaticContent_32.0.2006/css/v2/features.css' type='text/css' rel='stylesheet' />



<link href='https://ca.next.westlaw.com/StaticContent_32.0.2006/css/v2/document.css' type='text/css' rel='stylesheet' />





<!--[if gte IE 6]>

<link href='https://ca.next.westlaw.com/StaticContent_32.0.2006/css/v2/ie.css' type='text/css' rel='stylesheet' />

<![endif]-->

<link href='https://ca.next.westlaw.com/StaticContent_32.0.2006/css/v2/hover.css' type='text/css' rel='stylesheet' /><link href='https://ca.next.westlaw.com/StaticContent_32.0.2006/css/v2/print.css' type='text/css' rel='stylesheet' media='print' />

<link rel="shortcut icon" type="image/vnd.microsoft.icon" href="https://ia.next.westlaw.com/favicon.ico" />

<link rel="apple-touch-icon" href="https://ia.next.westlaw.com/StaticContent_32.0.2006/images/v2/iphone-webclip-icon.png" />

</head>



<body class="co_t2Left co_docDisplay refresh">



<div id="co_pageContainer" class="co_bodyToolbar">

<div id="co_mainContainer">











<div id="co_headerWrapper" class="wlnv2">



<div id="co_newHeader" >

<div id="co_headerContainer">

<div id="co_newHeader_top" class="headerContent" role="banner">





<div class="skipButtonContainer"></div>





<ul id="co_mainNav" class="co_inlineList" role="navigation">



<li id="co_kmFirmNameContainer"></li>





<li id="co_clientIdContainer" class="co_menuListFirst">



</li>



<li id="co_recentFoldersContainer"></li>



<li id="co_recentHistoryContainer"></li>



<li id="co_frequentFavoritesContainer"></li>

<li id="co_alertsCenterContainer"></li>



<li id="co_signOffContainer" class="co_hideState">



<div class="co_dropdownTabCollapsed">

<div class="co_dropdownTab">

<a href="javascript:void(0)" id="coid_website_signOffRegion" class="co_dropdownBoxanchorLabel co_hasTooltip" title="Toggle Profile Settings">

<span class="th_simple_icon icon_user reversed"></span>

<span class="th_simple_icon icon_down_arrow reversed"></span>

<span class="co_accessibilityLabel">Toggle Profile Settings</span>

</a>

</div>

</div>

<div class="co_dropdownBoxCollapsed co_globalNavDropdownBox">

<div class="co_globalNavDropdownBox_header">

<h3>Profile Settings</h3>

</div>

<div class="co_globalNavDropdownBox_content">

<div class="co_signOff_profile">

<h4>Adam Samaha</h4>

<ul>

<li>adam.samaha@nyu.edu</li>

</ul>

</div>



<div class="co_signOff_links">

</div>



<div class="co_signOff_buttons">

<div>

<button type="button" class="co_primaryBtn js_website_signoff">Sign Off</button>

</div>

</div>

</div>

</div>



</li>





</ul>



</div>

<div id="co_newHeader_bottom" class="headerContent">



<div id="headerLogo" class="">



<a id="coid_website_logo" href="/Search/Home.html/?transitionType=Default&contextData=(sc.Default)" tabindex="1" title="Westlaw Home" onclick="Cobalt.Widget.CompartmentDropdown.Instance().AddClearStickyTabToSession()">

<img src="https://ia.next.westlaw.com/StaticContent_32.0.2006/images/v2/logo.png" alt="Westlaw" />

</a>

</div>



<div id="co_compartment" class="co_dropDownMenu th_simple js_dropDownMenu right hasIcon">

<button name="dropdown" class="co_dropDownButton" aria-haspopup="true" aria-expanded="false">

<span tabindex="5" class="th_simple_icon icon_down_arrow reversed"></span>

<span class="co_accessibilityLabel">Select Product</span>

</button>

<div id="co_compartmentContainer" class="co_dropDownMenuContent" aria-hidden="true" aria-label="submenu">

<ul class="co_dropDownMenuList">



<li>



<span tabindex="6">

<span class="th_simple_icon icon_checkmark">Selected</span>

Westlaw

</span>



</li>



<li>



<a tabindex="7" id="co_PracticalLawLink" href="/Browse/Home/PracticalLaw/?transitionType=Default&contextData=(sc.Default)" onclick="Cobalt.Widget.CompartmentDropdown.Instance().AddClearStickyTabToSession()">Practical Law</a>



</li>



</ul>

</div>

</div>





<div id="coid_website_searchWidget" style="display:none;"></div>

<div id="co_headerSearch" class="co_hideState">

<div id="co_searchWidgetInnerId" class="">

<form action="" onsubmit="return false;">

<div id="co_searchFormLeft">

<a href="javascript:void(0);" id="co_categorySearchButton">

<span id="co_currentSelectedCategoryText">All Content</span>

<span id="co_currentSelectedCategoryToggle" class="th_simple_icon icon_down_arrow co_hideState">Icon</span>

</a>

<div class="co_dropdownBoxCollapsed" id="co_searchCategoryDropdown">



</div>

</div>

<div class="co_searchFormOuter">

<div class="co_searchInputContainer" id="co_searchInputContainer">

<div class="co_inputTop">

<div class="co_inputTopRight"></div>

</div>

<div class="co_inputMidLeft">

<div class="co_inputMidRight">

<!-- Search text box -->

<div class="co_textarea">

<label id="searchInputIdLabel" for="searchInputId">Search:</label>

<textarea style="" title="Search" name="searchInputId"

aria-label="Westlaw Search. Search suggestions available after typing 3 characters. Use arrow keys to navigate suggestions."

id="searchInputId" rows="1" spellcheck="false" autocorrect="off" autocapitalize="off"></textarea>

</div>



<!-- Medical litigator check box container -->

<div id="co_medLitExpandedTerms" class="co_floatRight co_formInline"></div>







<!-- Recent search query toggle -->

<a id="co_searchLast10Link" class="th_simple_icon icon_down_arrow co_hasTooltip" href="#"

onclick="return false;" title="View last twenty searches">

<span class="co_accessibilityLabel">View last twenty searches</span>

</a>

</div>

</div>

<div class="co_inputBottom">

<div class="co_inputBottomRight"></div>

</div>





<!-- Hold recent query drop down -->

<div id="co_recentQueryListBox" class="co_hideState">

<ul class="co_searchSuggestionContainer" id="co_searchLast10List"></ul>

</div>

</div>

</div>

<div id="co_searchFormRight">

<div id="co_searchFormRightWrapper">

<!-- Jurisdiction selected -->

<div id="co_jurisdictionWidgetContainer" class=""></div>

<!-- Search button -->

<input type="button" value="Search " id="searchButton" />

<!-- Advanced search -->

<a href="#" onclick="return false;" class="co_hideState" id="co_search_advancedSearchLink" title="Advanced Search">Advanced</a>

<!-- Holder jurisdiction pop up -->

<div id="co_searchJurisdictionHoverContainer"></div>

</div>

</div>

<!-- Search error container -->

<div id="co_searchInputErrorMessageContainer" class="co_hideState"></div>

</form>

</div>

</div>



<div id="coid_website_searchWidget" style="display:none;"></div>



<div id="co_researchAcceleratorWrapper">







<div id="co_researchAcceleratorContainer">



<a class="co_hasTooltip" href="javascript:void(0)" onclick="search_PublishResearchAcceleratorClickedEvent();"

title="Open Research Recommendations"

data-enableresearchaccel="true" >Research Accelerator</a>

</div>



</div>

<div id="co_dockContainer"> </div>



<div class="co_skipToLink">

<a id="coid_website_startContent" name="coid_website_startContent"></a>

</div>



</div><!--newHeader_bottom-->

</div><!--headerContainer-->

</div><!--newHeader-->



</div><!--co_headerWrapper-->









<!-- moved delivery toolbar to separate ascx control -->





<div id="co_body">







<!-- Reporting Name is "CTA" for document with guid "I401e23b1310611e5b86bd602cb8781fa". -->



<!-- CENTER COLUMN -->

<div id="co_contentWrapper">

<div id="co_contentColumn">

<div class="co_innertube">









<div id="co_docHeaderContainer">

<a class="co_skipToLink" href="#coid_website_errorsSummaryPlaceHolder">

Skip Page Header

</a>

<div id="co_docHeader">

<div id="co_docFixedHeader"><div id="co_docHeaderTitle"><h2 id="co_docHeaderTitleLine" title="Crazy Ely Western Village, LLC v. City of Las Vegas"><span id="title"><a class="co_drag" href="https://1.next.westlaw.com/Document/I401e23b1310611e5b86bd602cb8781fa/View/FullText.html?listSource=Search&amp;navigationPath=Search%2fv3%2fsearch%2fresults%2fnavigation%2fi0ad705250000015516bedc5391b305f7%3fNav%3dCASE%26fragmentIdentifier%3dI29ff453b835211e5b86bd602cb8781fa%26startIndex%3d1%26contextData%3d%2528sc.Search%2529%26transitionType%3dSearchItem&amp;list=CASE&amp;rank=7&amp;listPageSource=6f25ba1e16c760ebf11095b26d70afce&amp;originationContext=docHeader&amp;contextData=(sc.Search)&amp;transitionType=Document&amp;needToInjectTerms=False">Crazy Ely Western Village, LLC v. City of Las Vegas</a></span></h2><ul id="co_documentStatusIcons" class="co_document_indicators"><li><img src="https://ia.next.westlaw.com/StaticContent_32.0.2006/images/co_document_icon_previouslyviewed.png" width="18" alt="Eyeglasses &#8211; Previously viewed in last 30 days for current Client ID" title="Previously viewed in last 30 days for current Client ID" /></li></ul><h3 id="co_docHeaderCitation" title="United States Court of Appeals, Ninth Circuit. | July 22, 2015 | 618 Fed.Appx. 904 (Approx. 5 pages)"><span id="courtline">United States Court of Appeals, Ninth Circuit.</span><span id="filedate">July 22, 2015</span><span id="cite0">618 Fed.Appx. 904</span><em> (Approx. 5 pages)</em></h3><h4 id="co_docHeaderNegativeTreatment"><span id="co_document_compositeHeader_citatorFlag" class="co_citatorFlag"></span></h4></div></div>

<div class="co_clear"></div>

<div id="co_docPrimaryTabNavigationContainer" class="co_docTabs">



<a id="co_iPadKeyCiteMenuToggle" onclick="jQuery('#co_docPrimaryTabNavigation').toggleClass('co_showState')">

Toggle Menu

</a>



<ul id="co_docPrimaryTabNavigation" class="co_tabs">



<li id="DocumentTab" class="co_tabLeft co_tabActive co_dropdownTab">



<h2 class="co_tabRight">

<a id="coid_DocumentTab_link" class="co_tabLink" href="javascript:void(0);">

<span>Document</span>

</a>





<div class="co_clear"></div>

</h2>





</li>

<li id="riFilingsTab" class="co_tabLeft co_tabInactive" countStatus="" categoryEnum="riFilings">

<h2 class="co_tabRight">

<a id="coid_relatedInfo_riFilings_link" class="co_tabLink" href="javascript:void(0);" hiddenHref="/RelatedInformation/I401e23b1310611e5b86bd602cb8781fa/riFilings.html?originationContext=documentTab&transitionType=Filings&contextData=(sc.Search)&docSource=c7230a017b4046c694b6baebda7c1d8e&rank=7&rulebookMode=false">



<span>

Filings </span>

</a>



<div class="co_clear"></div>

</h2>



</li>

<li id="kcNegativeTreatmentTab" class="co_tabLeft co_tabInactive" countStatus="" categoryEnum="kcNegativeTreatment">

<h2 class="co_tabRight">

<a id="coid_relatedInfo_kcNegativeTreatment_link" class="co_tabLink" href="javascript:void(0);" hiddenHref="/RelatedInformation/I401e23b1310611e5b86bd602cb8781fa/kcNegativeTreatment.html?originationContext=documentTab&transitionType=NegativeTreatment&contextData=(sc.Search)&docSource=c7230a017b4046c694b6baebda7c1d8e&rank=7&rulebookMode=false">



<span>

Negative Treatment </span>

</a>



<div class="co_clear"></div>

</h2>



</li>

<li id="kcJudicialHistoryTab" class="co_tabLeft co_tabInactive" countStatus="" categoryEnum="kcJudicialHistory">

<h2 class="co_tabRight">

<a id="coid_relatedInfo_kcJudicialHistory_link" class="co_tabLink" href="javascript:void(0);" hiddenHref="/RelatedInformation/I401e23b1310611e5b86bd602cb8781fa/kcJudicialHistory.html?originationContext=documentTab&transitionType=History&contextData=(sc.Search)&docSource=c7230a017b4046c694b6baebda7c1d8e&rank=7&rulebookMode=false">



<span>

History </span>

</a>



<div class="co_clear"></div>

</h2>



</li>

<li id="kcCitingReferencesTab" class="co_tabLeft co_tabInactive co_dropdownTab" countStatus="" categoryEnum="kcCitingReferences">

<h2 class="co_tabRight">

<a id="coid_relatedInfo_kcCitingReferences_link" class="co_tabLink" href="javascript:void(0);" hiddenHref="/RelatedInformation/I401e23b1310611e5b86bd602cb8781fa/kcCitingReferences.html?originationContext=documentTab&transitionType=CitingReferences&contextData=(sc.Search)&docSource=c7230a017b4046c694b6baebda7c1d8e&rank=7&rulebookMode=false">



<span>

Citing References </span>

</a>



<span id="co_kcCitingReferencesNavAnchor" class="co_dropdownArrowCollapsed">Navigate Citing References</span>



<div class="co_clear"></div>

</h2>



<div id="co_kcCitingReferencesNavContent" class="co_dropdownBoxCollapsed" style="display:none;"></div>



</li>

<li id="kcTableOfAuthoritiesTab" class="co_tabLeft co_tabInactive" countStatus="" categoryEnum="kcTableOfAuthorities">

<h2 class="co_tabRight">

<a id="coid_relatedInfo_kcTableOfAuthorities_link" class="co_tabLink" href="javascript:void(0);" hiddenHref="/RelatedInformation/I401e23b1310611e5b86bd602cb8781fa/kcTableOfAuthorities.html?originationContext=documentTab&transitionType=TableOfAuthorities&contextData=(sc.Search)&docSource=c7230a017b4046c694b6baebda7c1d8e&rank=7&rulebookMode=false">



<span>

Table of Authorities </span>

</a>



<div class="co_clear"></div>

</h2>



</li>



<li id="co_powByKCContainer">

<a id="co_powByKC" href="javascript:void(0)">

Powered by KeyCite

</a>

</li>



</ul>

</div>

<div class="co_clear"></div>

<div id="co_docToolbarContainer" class="">

<div id="co_docToolbar"></div>

<div class="co_clear"></div>

</div>

</div>

</div>



<div id="coid_website_errorsSummaryPlaceHolder"></div>

<div id="coid_website_messagePlaceholder"></div>



<div id="test_hplink"></div>

<div class="co_scrollWrapper">





<div id="coid_website_documentWidgetDiv" class="co_dipOpt_fontTimesNewRoman co_disOpt_textSizeExtraLarge co_khSpeedReadExpandAll">

<div id="co_document"><div id="co_document_0" class="co_document co_caselawNRS"><input type="hidden" id="co_keyCiteFlagPlaceHolder" /><input type="hidden" id="co_document_starPageMetadata" value="{ &quot;citations&quot;: { &quot;S0a851820936611e5b86bd602cb8781fa&quot;:&quot;618 Fed.Appx. 904&quot; }, &quot;pubs&quot;: { &quot;S0a851820936611e5b86bd602cb8781fa&quot;:&quot;6538&quot; } }" alt="metadata" /><div class="co_cites">618 Fed.Appx. 904</div><input type="hidden" id="co_document_paraNumbersSourceCiteMetadata" value="{ &quot;paraNumbersSourceCite&quot;: &quot;618 Fed.Appx. 904&quot;, &quot;publicationNumber&quot;: &quot;6538&quot; }" alt="metadata" /><div class="co_contentBlock co_briefItState co_editorialNoteBlock"><div>This case was not selected for publication in West's Federal Reporter.</div><div>See Fed. Rule of Appellate Procedure 32.1 generally governing citation of judicial decisions issued on or after Jan. 1, 2007. See also U.S.Ct. of App. 9th Cir. Rule 36-3.</div></div><div class="co_contentBlock co_briefItState co_courtBlock"><div><div class="co_hAlign2">United States Court of Appeals,</div>Ninth Circuit.</div></div><div class="co_title"><div class="co_suit"><div class="co_partyLine">CRAZY ELY WESTERN VILLAGE, LLC, a Nevada limited liability company and <a id="co_link_I4809d7c51d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Search/Results.html?query=advanced%3a+OAID(5018213927)&amp;saveJuris=False&amp;contentType=BUSINESS-INVESTIGATOR&amp;startIndex=1&amp;contextData=(sc.Default)&amp;categoryPageUrl=Home%2fCompanyInvestigator&amp;originationContext=document&amp;transitionType=DocumentItem">G &amp; G Fremont, LLC</a>, a Nevada limited liability company, Plaintiffs–Appellants,</div><div>v.</div><div class="co_partyLine">CITY OF LAS VEGAS, Defendant–Appellee.</div></div></div><div class="co_docketDate"><div class="co_contentBlock co_briefItState co_docketBlock"><span>No. 14–17208.</span></div><div class="co_date"><span>Argued and Submitted May 11, 2015.</span><span>Filed July 22, 2015.</span></div></div><div class="co_contentBlock co_briefItState co_synopsis"><h2 id="co_synopsis" class="co_printHeading">Synopsis</h2><div><div class="co_paragraph"><div class="co_paragraphText"><strong>Background:</strong> Owner of three souvenir and package liquor stores along pedestrian mall brought action against city, challenging constitutionality of advertising and notice restrictions imposed by ordinance on stores selling alcohol pursuant to off-sale or package alcohol license along the mall, and subsequently filed motion for preliminary injunction. The United States District Court for the District of Nevada, <a id="co_link_I4809d7c81d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=h&amp;pubNum=176284&amp;cite=0169483301&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RQ&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">James C. Mahan</a>, J., <a id="co_link_I4809d7c91d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=2034568243&amp;pubNum=0000999&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">2014 WL 5062548</a>, denied the motion, and owner appealed.</div></div></div><div class="co_contentBlock co_briefItState co_synopsisHolding"><div class="co_paragraph"><div class="co_paragraphText"><strong>Holdings:</strong> The Court of Appeals held that:</div></div><div class="co_paragraph"><div class="co_paragraphText"><a href="#co_anchor_F12036737440" class="co_internalLink co_excludeAnnotations co_disableHighlightFeatures">1</a> the notice restrictions satisfied the <em><span class="co_searchTerm" id="co_term_324">Central</span> <span class="co_searchTerm" id="co_term_325">Hudson</span></em> test, but</div></div><div class="co_paragraph"><div class="co_paragraphText"><a href="#co_anchor_F22036737440" class="co_internalLink co_excludeAnnotations co_disableHighlightFeatures">2</a> city failed to demonstrate that the advertising restrictions satisfied the third and fourth prongs of the <em><span class="co_searchTerm" id="co_term_346">Central</span> <span class="co_searchTerm" id="co_term_347">Hudson</span></em> test.</div></div></div><div class="co_paragraph"><div class="co_paragraphText">Affirmed in part, reversed in part, and remanded.</div></div></div><div id="co_headnotes" class="co_headnotes co_fancyHeadnotes co_containsSearchTerms"><h2 id="co_headnoteHeader" class="co_headnoteHeader co_printHeading"><span class="co_headnoteHeaderSpan">West Headnotes (2)</span></h2><div class="co_headnotesContentContainer"><div id="co_expandedHeadnotes"><div class="co_headnoteRow" id="co_anchor_2036737440001"><div class="co_headnoteCell"><div class="co_headnoteCellInner"><div class="co_primaryHeadnoteNodes"><span class="co_headnoteNumber co_excludeAnnotations co_disableHighlightFeatures" id="co_anchor_F12036737440"><span class="co_headnoteNumber" id="co_anchor_headNote_1"><a href="#co_anchor_B12036737440" class="co_internalLink">1</a></span></span><span class="co_headnoteNode"><strong><a id="co_link_ID0EQEAC" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/92/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">Constitutional Law</a></strong></span><div class="co_keyIcon co_excludeAnnotations co_disableHighlightFeatures"><div class="co_headnoteTopics co_excludeAnnotations co_disableHighlightFeatures"><img src="https://ia.next.westlaw.com/StaticContent_32.0.2006/images/headnoteKey.png" class="co_headnoteKeyIcon" alt="Display Key Number Topics" title="Display Key Number Topics" /><div class="co_fancyKeyciteContainerBottom"><div class="co_fancyKeyciteContainer"><div class="co_popupHeadnote"></div></div></div></div></div><span class="co_lastKeyText"><a id="co_link_ID0EYFAC" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/92k1613/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">Intoxicating liquors</a></span></div><div class="co_secondaryHeadnoteNodes"> <span class="co_headnoteNode"><strong><a id="co_link_ID0EHGAC" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/223/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">Intoxicating Liquors</a></strong></span><div class="co_keyIcon co_excludeAnnotations co_disableHighlightFeatures"><div class="co_headnoteTopics co_excludeAnnotations co_disableHighlightFeatures"><img src="https://ia.next.westlaw.com/StaticContent_32.0.2006/images/headnoteKey.png" class="co_headnoteKeyIcon" alt="Display Key Number Topics" title="Display Key Number Topics" /><div class="co_fancyKeyciteContainerBottom"><div class="co_fancyKeyciteContainer"><div class="co_popupHeadnote"></div></div></div></div></div><span class="co_lastKeyText"><a id="co_link_ID0EFHAC" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/223k15/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">Licensing and regulation</a></span></div> <div class="co_headnote"><div class="co_headnoteParagraph"><div class="co_paragraphText">Notice restrictions imposed by ordinance on stores selling alcohol pursuant to off-sale or package alcohol license along city's pedestrian mall, which required that stores post signs informing customers that opening or consuming alcohol purchased at store on mall was prohibited, satisfied the <em><span class="co_searchTerm" id="co_term_443">Central</span> <span class="co_searchTerm" id="co_term_444">Hudson</span></em> test; the notice restrictions compelled <span class="co_searchTerm" id="co_term_450">commercial</span> <span class="co_searchTerm" id="co_term_451">speech</span> that was purely factual. <a id="co_link_I4809d7d41d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=L&amp;pubNum=1000583&amp;cite=USCOAMENDI&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=LQ&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">U.S.C.A. Const.Amend. 1</a>.</div></div><div id="co_headnoteId_203673744000120160518151852" class="co_headnoteCitedCaseRef"><a id="co_link_ID0EUHAC" class="co_link co_excludeAnnotations co_disableHighlightFeatures" href="https://1.next.westlaw.com/Link/RelatedInformation/DocHeadnoteLink?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;headnoteId=203673744000120160518151852&amp;originationContext=document&amp;docSource=de1aea694c734ddb8a7b2e0078e373af&amp;rank=7&amp;transitionType=CitingReferences&amp;contextData=(sc.Search)" title="Cases that cite headnote 1">Cases that cite this headnote</a></div></div></div></div> <div class="co_headnoteTopicsCell"><div class="co_headnoteTopics co_excludeAnnotations co_disableHighlightFeatures"><img src="https://ia.next.westlaw.com/StaticContent_32.0.2006/images/headnoteKey.png" class="co_headnoteKeyIcon" alt="Key Number Symbol" title="Key Number Symbol" /><div class="co_fancyKeyciteContainerBottom"><div class="co_fancyKeyciteContainer"><div class="co_topicKeyContentTable"><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7cc1d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/92/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">92</a></span><span class="co_headnoteTopicKey">Constitutional Law</span></div><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7cd1d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/92XVIII/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">92XVIII</a></span><span class="co_headnoteTopicKey">Freedom of Speech, Expression, and Press</span></div><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7ce1d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/92XVIII(C)/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">92XVIII(C)</a></span><span class="co_headnoteTopicKey">Trade or Business</span></div><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7cf1d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/92k1613/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">92k1613</a></span><span class="co_headnoteTopicKey">Intoxicating liquors</span></div></div></div></div></div><div class="co_headnoteTopics co_excludeAnnotations co_disableHighlightFeatures"><img src="https://ia.next.westlaw.com/StaticContent_32.0.2006/images/headnoteKey.png" class="co_headnoteKeyIcon" alt="Key Number Symbol" title="Key Number Symbol" /><div class="co_fancyKeyciteContainerBottom"><div class="co_fancyKeyciteContainer"><div class="co_topicKeyContentTable"><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7d01d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/223/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">223</a></span><span class="co_headnoteTopicKey">Intoxicating Liquors</span></div><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7d11d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/223II/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">223II</a></span><span class="co_headnoteTopicKey">Constitutionality of Acts and Ordinances</span></div><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7d21d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/223k15/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">223k15</a></span><span class="co_headnoteTopicKey">Licensing and regulation</span></div></div></div></div></div></div><div class="co_clear"></div></div><div class="co_headnoteRow" id="co_anchor_2036737440002"><div class="co_headnoteCell"><div class="co_headnoteCellInner"><div class="co_primaryHeadnoteNodes"><span class="co_headnoteNumber co_excludeAnnotations co_disableHighlightFeatures" id="co_anchor_F22036737440"><span class="co_headnoteNumber" id="co_anchor_headNote_2"><a href="#co_anchor_B22036737440" class="co_internalLink">2</a></span></span><span class="co_headnoteNode"><strong><a id="co_link_ID0EDJAC" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/92/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">Constitutional Law</a></strong></span><div class="co_keyIcon co_excludeAnnotations co_disableHighlightFeatures"><div class="co_headnoteTopics co_excludeAnnotations co_disableHighlightFeatures"><img src="https://ia.next.westlaw.com/StaticContent_32.0.2006/images/headnoteKey.png" class="co_headnoteKeyIcon" alt="Display Key Number Topics" title="Display Key Number Topics" /><div class="co_fancyKeyciteContainerBottom"><div class="co_fancyKeyciteContainer"><div class="co_popupHeadnote"></div></div></div></div></div><span class="co_lastKeyText"><a id="co_link_ID0EVKAC" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/92k1649/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">Intoxicating liquors</a></span></div><div class="co_secondaryHeadnoteNodes"> <span class="co_headnoteNode"><strong><a id="co_link_ID0EELAC" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/223/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">Intoxicating Liquors</a></strong></span><div class="co_keyIcon co_excludeAnnotations co_disableHighlightFeatures"><div class="co_headnoteTopics co_excludeAnnotations co_disableHighlightFeatures"><img src="https://ia.next.westlaw.com/StaticContent_32.0.2006/images/headnoteKey.png" class="co_headnoteKeyIcon" alt="Display Key Number Topics" title="Display Key Number Topics" /><div class="co_fancyKeyciteContainerBottom"><div class="co_fancyKeyciteContainer"><div class="co_popupHeadnote"></div></div></div></div></div><span class="co_lastKeyText"><a id="co_link_ID0ECMAC" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/223k15/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">Licensing and regulation</a></span></div> <div class="co_headnote"><div class="co_headnoteParagraph"><div class="co_paragraphText">City failed to demonstrate that advertising restrictions imposed by ordinance on stores selling alcohol pursuant to off-sale or package alcohol license along city's pedestrian mall, which required that stores limit their alcohol advertising to only ten percent of store windows and prohibited stores from posting alcohol price advertisements that were visible to individuals standing outside the establishment, directly and materially advanced the governmental interests asserted and that there were no less-restrictive alternatives, as required to satisfy <em><span class="co_searchTerm" id="co_term_579">Central</span> <span class="co_searchTerm" id="co_term_580">Hudson</span></em> test; advertising regulations restricted the speech of only certain liquor sellers, thus requiring city to explain why they were not impermissibly underinclusive, and city did not show that it opted to restrict speech only after determining that conduct-based restrictions, such as citing and arresting intoxicated or underage drinkers, or banning alcohol consumption along mall, would not work. <a id="co_link_I4809d7de1d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=L&amp;pubNum=1000583&amp;cite=USCOAMENDI&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=LQ&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">U.S.C.A. Const.Amend. 1</a>.</div></div><div id="co_headnoteId_203673744000220160518151852" class="co_headnoteCitedCaseRef"><a id="co_link_ID0ERMAC" class="co_link co_excludeAnnotations co_disableHighlightFeatures" href="https://1.next.westlaw.com/Link/RelatedInformation/DocHeadnoteLink?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;headnoteId=203673744000220160518151852&amp;originationContext=document&amp;docSource=de1aea694c734ddb8a7b2e0078e373af&amp;rank=7&amp;transitionType=CitingReferences&amp;contextData=(sc.Search)" title="Cases that cite headnote 2">Cases that cite this headnote</a></div></div></div></div> <div class="co_headnoteTopicsCell"><div class="co_headnoteTopics co_excludeAnnotations co_disableHighlightFeatures"><img src="https://ia.next.westlaw.com/StaticContent_32.0.2006/images/headnoteKey.png" class="co_headnoteKeyIcon" alt="Key Number Symbol" title="Key Number Symbol" /><div class="co_fancyKeyciteContainerBottom"><div class="co_fancyKeyciteContainer"><div class="co_topicKeyContentTable"><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7d51d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/92/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">92</a></span><span class="co_headnoteTopicKey">Constitutional Law</span></div><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7d61d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/92XVIII/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">92XVIII</a></span><span class="co_headnoteTopicKey">Freedom of Speech, Expression, and Press</span></div><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7d71d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/92XVIII(E)/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">92XVIII(E)</a></span><span class="co_headnoteTopicKey">Advertising and Signs</span></div><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7d81d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/92XVIII(E)2/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">92XVIII(E)2</a></span><span class="co_headnoteTopicKey">Advertising</span></div><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7d91d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/92k1649/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">92k1649</a></span><span class="co_headnoteTopicKey">Intoxicating liquors</span></div></div></div></div></div><div class="co_headnoteTopics co_excludeAnnotations co_disableHighlightFeatures"><img src="https://ia.next.westlaw.com/StaticContent_32.0.2006/images/headnoteKey.png" class="co_headnoteKeyIcon" alt="Key Number Symbol" title="Key Number Symbol" /><div class="co_fancyKeyciteContainerBottom"><div class="co_fancyKeyciteContainer"><div class="co_topicKeyContentTable"><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7da1d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/223/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">223</a></span><span class="co_headnoteTopicKey">Intoxicating Liquors</span></div><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7db1d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/223II/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">223II</a></span><span class="co_headnoteTopicKey">Constitutionality of Acts and Ordinances</span></div><div class="co_headnoteKeyPair"><span class="co_headnoteRefNumber"><a id="co_link_I4809d7dc1d8111e698dc8b09b4f043e0" class="co_link" href="https://1.next.westlaw.com/Browse/Home/KeyNumber/223k15/View.html?docGuid=I401e23b1310611e5b86bd602cb8781fa&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">223k15</a></span><span class="co_headnoteTopicKey">Licensing and regulation</span></div></div></div></div></div></div><div class="co_clear"></div></div></div></div><div> </div></div><a id="co_headnotesEnd"></a><h2 class="co_attorneyBlockLabel co_printHeading co_briefItState" id="co_attorneysAndLawFirms">Attorneys and Law Firms</h2><div class="co_contentBlock co_briefItState co_attorneyBlock"><div> <span class="co_starPage" id="co_pp_sp_6538_905"><input type="hidden" class="co_starPageMetadataItem" value="{ &quot;pageset&quot;: &quot;S0a851820936611e5b86bd602cb8781fa&quot;, &quot;pageNumber&quot;: &quot;905&quot; }" alt="metadata" />*905</span> <a id="co_link_I4809d7df1d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=h&amp;pubNum=176284&amp;cite=0329026501&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RQ&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">Tillman J. Breckenridge</a>, Reed Smith LLP, Washington, DC, <input type="hidden" id="co_docMarker_0" /><a id="co_link_I4809d7e01d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=h&amp;pubNum=176284&amp;cite=0330434001&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RQ&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">Jeffrey F. Barr</a>, Esquire, Ashcraft &amp; Barr LLP, Las Vegas, NV, for Plaintiffs–Appellants.</div><div><a id="co_link_I4809d7e11d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=h&amp;pubNum=176284&amp;cite=0159661001&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RQ&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">Philip Byrnes</a>, Esquire, Jeffry M. Dorocak, Las Vegas City Attorney's Office, Las Vegas, NV, for Defendant–Appellee.</div></div><div class="co_contentBlock co_briefItState co_actionBlock"><div>Appeal from the United States District Court for the District of Nevada, <a id="co_link_I4809d7e31d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=h&amp;pubNum=176284&amp;cite=0169483301&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RQ&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">James C. Mahan</a>, District Judge, Presiding. D.C. No. 2:14–cv–01006–JCM–PAL.</div></div><div class="co_contentBlock co_briefItState co_panelBlock"><div>Before: <a id="co_link_I4809d7e51d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=h&amp;pubNum=176284&amp;cite=0221879201&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RQ&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">THOMAS</a>, Chief Judge, and BENAVIDES<sup id="co_footnoteReference_B0012036737440_ID0EKAAE"><a href="#co_footnote_B0012036737440" class="co_footnoteReference">*</a></sup> and <a id="co_link_I4809d7e61d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=h&amp;pubNum=176284&amp;cite=0483904801&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RQ&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">OWENS</a>, Circuit Judges.</div></div><div class="co_contentBlock co_briefItState co_opinionBlock"><h2 id="co_opinion"></h2><div class="co_docDelivery_dottedLine"><img src="https://ia.next.westlaw.com/StaticContent_32.0.2006/images/co_docDelivery_dottedLine.png" alt="" /></div><div class="co_contentBlock x_opinionBlockBody"><div class="co_contentBlock x_opinionLead">
<div class="co_contentBlock x_opinionBody"><div class="co_contentBlock co_briefItState co_section" id="co_anchor_I1d0853751d8111e698dc8b09b4f043e0"><div class="co_headtext co_hAlign2"><span class="co_smallCaps">MEMORANDUM<sup id="co_footnoteReference_B0022036737440_ID0EBCAE"><a href="#co_footnote_B0022036737440" class="co_footnoteReference">**</a></sup></span></div><div class="co_paragraph"><div class="co_paragraphText">Plaintiffs Crazy Ely Western Village, LLC and G &amp; G Fremont, LLC own and operate stores that sell souvenirs and package alcohol on or adjacent to the Fremont Street pedestrian mall in Las Vegas, Nevada. In May of 2014, the City of Las Vegas enacted Ordinance 6320. The ordinance applies only to stores selling alcohol pursuant to an off-sale or package alcohol license along the pedestrian mall. <em>See</em> LVMC § 6.50.475. It requires that the stores limit their alcohol advertising to only ten percent of their store windows, <em>id.</em> § 6.50.475(G)-(H), and it prohibits the stores from posting alcohol price advertisements that are visible to individuals standing outside of the establishment (“advertising restrictions”). <em>Id.</em> § 6.50.475(F). The ordinance also requires that the stores post signs informing customers that it is prohibited to open or consume alcohol purchased at the store on the pedestrian mall (“notice restrictions”). <em>Id.</em> § 6.50.475(I).</div></div><div class="co_paragraph"><div class="co_paragraphText">Plaintiffs filed suit, alleging that Ordinance 6320 and Ordinance 6266, which also regulates alcohol sales along the pedestrian mall, violate the First, Fifth, and Fourteenth Amendments, as well as § 1 of the Sherman Antitrust Act, <a id="co_link_I4809d7e81d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=L&amp;pubNum=1000546&amp;cite=15USCAS1&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=LQ&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">15 U.S.C. § 1</a>, and Plaintiffs' civil rights under <a id="co_link_I4809d7e91d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=L&amp;pubNum=1000546&amp;cite=42USCAS1983&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=LQ&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">42 U.S.C. § 1983</a>. Plaintiffs also alleged that the City's regulatory regime is a bill of attainder and constitutes a taking. They requested declaratory relief as well as a preliminary and permanent injunction. The district court determined that Plaintiffs were not likely to succeed on the merits of their claim, and it denied Plaintiffs' request for a preliminary injunction. <em>See </em> <span class="co_starPage" id="co_pp_sp_6538_906"><input type="hidden" class="co_starPageMetadataItem" value="{ &quot;pageset&quot;: &quot;S0a851820936611e5b86bd602cb8781fa&quot;, &quot;pageNumber&quot;: &quot;906&quot; }" alt="metadata" />*906</span> <a id="co_link_I4809d7ea1d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=2017439125&amp;pubNum=0000708&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)"><em>Winter v. Natural Res. Def. Council, Inc.,</em> 555 U.S. 7, 20, 129 S.Ct. 365, 172 L.Ed.2d 249 (2008)</a> (outlining four-part test for evaluating a request for a preliminary injunction).</div></div><div class="co_paragraph"><div class="co_paragraphText">On appeal, Plaintiffs raise only their First Amendment challenge to the commercial speech restrictions contained in Ordinance 6320. We have jurisdiction pursuant to <a id="co_link_I4809d7eb1d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=L&amp;pubNum=1000546&amp;cite=28USCAS1292&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RB&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)#co_pp_8b3b0000958a4">28 U.S.C. § 1292(a)</a>. In the First Amendment context, the party seeking a preliminary injunction “bears the initial burden of making a colorable claim that its First Amendment rights have been infringed, or are threatened with infringement, at which point the burden shifts to the government to justify the restriction.” <a id="co_link_I4809d7ec1d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=2025501811&amp;pubNum=0000506&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;fi=co_pp_sp_506_1116&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)#co_pp_sp_506_1116"><em>Thalheimer v. City of San Diego,</em> 645 F.3d 1109, 1116 (9th Cir.2011)</a>. We review a district court's denial of a motion for preliminary injunction for abuse of discretion. <a id="co_link_I4809d7ed1d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=2025501811&amp;pubNum=0000506&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;fi=co_pp_sp_506_1115&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)#co_pp_sp_506_1115"><em>Id.</em> at 1115</a>. Review of a district court's denial of a request for a preliminary injunction should be “limited and deferential.” <a id="co_link_I4809d7ee1d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=2003639982&amp;pubNum=0000506&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;fi=co_pp_sp_506_918&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)#co_pp_sp_506_918"><em>Sw. Voter Registration Educ. Project v. Shelley,</em> 344 F.3d 914, 918 (9th Cir.2003)</a>. We affirm in part, reverse in part, and remand.</div></div><div class="co_paragraph"><div class="co_paragraphText">When evaluating a request for a preliminary injunction, courts consider (1) the likelihood of success on the merits, (2) the likelihood that the party will suffer irreparable harm if preliminary relief is not granted, (3) the balance of equities, and (4) the public interest. <a id="co_link_I4809d7ef1d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=2017439125&amp;pubNum=0000708&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)"><em>Winter,</em> 555 U.S. at 20, 129 S.Ct. 365</a>. Regulations of commercial speech are evaluated under the four-part test outlined in <input type="hidden" id="co_docMarker_1" /><a id="co_link_I4809d7f01d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=1980116785&amp;pubNum=0000708&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)"><em><span class="co_searchTerm" id="co_term_1303">Central</span> <span class="co_searchTerm" id="co_term_1304">Hudson</span> Gas &amp; Electric Corporation v. Public Service Commission of New York.</em> 447 U.S. 557, 100 S.Ct. 2343, 65 L.Ed.2d 341 (1980)</a>. First, commercial speech receives First Amendment protection if it “concern[s] lawful activity” and is not “misleading.” <a id="co_link_I4809d7f11d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=1980116785&amp;pubNum=0000708&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)"><em>Id.</em> at 566, 100 S.Ct. 2343</a>. Second, the court “ask[s] whether the asserted governmental interest is substantial.” <em>Id.</em> Third, the court “determine[s] whether the regulation directly advances the governmental interest asserted.” <em>Id.</em> And fourth, the court asks “whether [the regulation] is not more extensive than is necessary to serve that interest.” <em>Id.</em></div></div><div class="co_paragraph"><div class="co_paragraphText"><a href="#co_anchor_F12036737440" class="co_internalLink co_headnoteLink co_excludeAnnotations co_disableHighlightFeatures" id="co_pp_HNF1">1</a><a id="co_anchor_B12036737440"></a> The notice restrictions satisfy the <em><span class="co_searchTerm" id="co_term_1409">Central</span> <span class="co_searchTerm" id="co_term_1410">Hudson</span></em> test. The government may compel “purely factual and uncontroversial” commercial speech. <a id="co_link_I4809d7f41d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=1985126962&amp;pubNum=0000708&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)"><em><span class="co_searchTerm" id="co_term_1424">Zauderer</span> v. Office of Disciplinary Counsel of Supreme Court of Ohio,</em> 471 U.S. 626, 651, 105 S.Ct. 2265, 85 L.Ed.2d 652 (1985)</a>. “Compelled disclosures, justified by the need to ‘dissipate the possibility of consumer confusion or deception,’ are permissible if the ‘disclosure requirements are reasonably related to the State's interest in preventing deception of customers.’ ” <a id="co_link_I4809d7f51d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=2018183992&amp;pubNum=0000506&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;fi=co_pp_sp_506_966&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)#co_pp_sp_506_966"><em>Video Software Dealers Ass'n v. Schwarzenegger,</em> 556 F.3d 950, 966 (9th Cir.2009)</a>, <em>aff'd sub nom. </em><a id="co_link_I4809d7f61d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=2025554470&amp;pubNum=0000708&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)"><em>Brown v. Entm't Merchants Ass'n,</em> ––– U.S. ––––, 131 S.Ct. 2729, 180 L.Ed.2d 708 (2011)</a>. Plaintiffs have presented no evidence that the notice restrictions compel speech that is not purely factual. Plaintiffs are not likely to succeed on the merits of their claim. The final three <em>Winter</em> factors also weigh in the City's favor.</div></div><div class="co_paragraph"><div class="co_paragraphText"><a href="#co_anchor_F22036737440" class="co_internalLink co_headnoteLink co_excludeAnnotations co_disableHighlightFeatures" id="co_pp_HNF2">2</a><a id="co_anchor_B22036737440"></a> The advertising restrictions satisfy the first two parts of the <em><span class="co_searchTerm" id="co_term_1568">Central</span> <span class="co_searchTerm" id="co_term_1569">Hudson</span></em> test. However, on the limited record before us, the City has not demonstrated that the advertising restrictions directly and materially advance the governmental interests asserted and that there are no less-restrictive alternatives to the restrictions. <em>See </em><a id="co_link_I4809d7f91d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=1980116785&amp;pubNum=0000708&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)"><em><span class="co_searchTerm" id="co_term_1609">Central</span> <span class="co_searchTerm" id="co_term_1610">Hudson</span>,</em> 447 U.S. at 566, 100 S.Ct. 2343</a>. These third and fourth “steps of the <em><span class="co_searchTerm" id="co_term_1626">Central</span> <span class="co_searchTerm" id="co_term_1627">Hudson</span></em> analysis basically involve a consideration of the ‘fit’ between the legislature's ends and the means chosen to accomplish those ends.” <a id="co_link_I4809d7fb1d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=1995091639&amp;pubNum=0000708&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)"><em>Rubin v. Coors Brewing Co.,</em> 514 U.S. 476, 486, 115 S.Ct. 1585, 131 L.Ed.2d 532 (1995)</a>.</div></div><div class="co_paragraph"><div class="co_paragraphText"> <span class="co_starPage" id="co_pp_sp_6538_907"><input type="hidden" class="co_starPageMetadataItem" value="{ &quot;pageset&quot;: &quot;S0a851820936611e5b86bd602cb8781fa&quot;, &quot;pageNumber&quot;: &quot;907&quot; }" alt="metadata" />*907</span> Under the third prong of <em><span class="co_searchTerm" id="co_term_1672">Central</span> <span class="co_searchTerm" id="co_term_1673">Hudson</span>,</em> there is “little chance” a speech restriction directly and materially advances a governmental interest if “other provisions of the same Act directly undermine and counteract its effects.” <a id="co_link_I4809d7fd1d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=1995091639&amp;pubNum=0000708&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)"><em>Id.</em> at 489, 115 S.Ct. 1585</a>; <em>see also </em><a id="co_link_I4809d7fe1d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=2001123226&amp;pubNum=0000506&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;fi=co_pp_sp_506_1095&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)#co_pp_sp_506_1095"><em>W. States Med. Ctr. v. Shalala,</em> 238 F.3d 1090, 1095 (9th Cir.2001)</a> (“When exemptions and inconsistencies counteract the alleged purpose of a speech restriction, the restriction fails the direct advancement test.”). Because other City ordinances encourage the consumption of alcohol on Fremont Street, the City bears a greater burden to justify restricting speech in order to combat problems connected with alcohol consumption on Fremont Street. Furthermore, a speech restriction's underinclusivity is also a “consideration in the direct advancement inquiry” because “underinclusivity ... ‘may diminish the credibility of the government's rationale for restricting speech in the first place.’ ” <a id="co_link_I4809d7ff1d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=2029974777&amp;pubNum=0000506&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;fi=co_pp_sp_506_824&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)#co_pp_sp_506_824"><em>Valle Del Sol Inc. v. Whiting,</em> 709 F.3d 808, 824 (9th Cir.2013)</a>. Because the advertising regulations restrict the speech of only certain liquor sellers, the City must explain why the regulations are not impermissibly underinclusive.</div></div><div class="co_paragraph"><div class="co_paragraphText">Under the fourth prong of <em><span class="co_searchTerm" id="co_term_1855">Central</span> <span class="co_searchTerm" id="co_term_1856">Hudson</span>,</em> “A regulation need not be ‘absolutely the least severe that will achieve the desired end,’<input type="hidden" id="co_docMarker_2" /> but if there are numerous and obvious less-burdensome alternatives to the restriction on commercial speech, that is certainly a relevant consideration in determining whether the ‘fit’ between ends and means is reasonable.” <a id="co_link_I4809d8011d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=1993072387&amp;pubNum=0000708&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)"><em>City of Cincinnati v. Discovery Network, Inc.,</em> 507 U.S. 410, 417 n. 13, 113 S.Ct. 1505, 123 L.Ed.2d 99 (1993)</a> (internal citation omitted); <em>see also </em><a id="co_link_I4809d8021d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=2001552278&amp;pubNum=0000708&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)"><em>Lorillard Tobacco Co. v. Reilly,</em> 533 U.S. 525, 556, 121 S.Ct. 2404, 150 L.Ed.2d 532 (2001)</a> (explaining that regulations satisfy prong four only if they are “narrowly tailored to achieve the desired objective”). Speech restrictions do not satisfy prong four “[i]f clear alternatives exist that can advance the government's asserted interest in a manner far less intrusive to ... free speech rights.” <a id="co_link_I4809d8031d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=2001123226&amp;pubNum=0000506&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;fi=co_pp_sp_506_1095&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)#co_pp_sp_506_1095"><em>W. States,</em> 238 F.3d at 1095</a>. As a result, a city “must consider pursuing its interests through conduct-based regulations before enacting speech-based regulations.” <a id="co_link_I4809d8041d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=Y&amp;serNum=2029974777&amp;pubNum=0000506&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RP&amp;fi=co_pp_sp_506_827&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)#co_pp_sp_506_827"><em>Valle Del Sol,</em> 709 F.3d at 827</a>. Here, the City must demonstrate that it opted to restrict speech only after determining that its interests could not be adequately advanced by means of conduct-based restrictions such as citing and arresting those who are intoxicated or drinking underage or banning alcohol consumption on Fremont Street.</div></div><div class="co_paragraph"><div class="co_paragraphText">We remand for further findings as to whether the advertising restrictions directly and materially advance the City's interests, and whether any less-restrictive alternatives to the advertising restrictions are available.</div></div><div class="co_paragraph"><div class="co_paragraphText"><strong>AFFIRMED IN PART; REVERSED IN PART; and REMANDED.</strong></div></div><div class="co_paragraph"><div class="co_paragraphText">Each side shall bear its own costs on appeal.</div></div></div></div></div></div></div><div class="co_parallelCites"><h2 id="co_allCitations" class="co_parallelCitesBlockLabel co_printHeading">All Citations</h2>618 Fed.Appx. 904</div><div id="co_footnoteSection" class="co_footnoteSection co_briefItState"><h2 class="co_footnoteSectionTitle co_printHeading">Footnotes</h2><div><div class="co_footnoteNumber"><input type="hidden" class="co_starPageMetadataItem" value="{ &quot;pageset&quot;: &quot;S0a851820936611e5b86bd602cb8781fa&quot;, &quot;pageNumber&quot;: &quot;905&quot; }" alt="metadata" /><span id="co_footnote_B0012036737440"><a href="#co_footnoteReference_B0012036737440_ID0EKAAE">*</a></span></div><div class="co_footnoteBody"><div class="co_paragraph"><div class="co_paragraphText">The Honorable <a id="co_link_I4809d7e71d8111e698dc8b09b4f043e0" class="co_link co_drag ui-draggable" href="https://1.next.westlaw.com/Link/Document/FullText?findType=h&amp;pubNum=176284&amp;cite=0201916501&amp;originatingDoc=I401e23b1310611e5b86bd602cb8781fa&amp;refType=RQ&amp;originationContext=document&amp;transitionType=DocumentItem&amp;contextData=(sc.Search)">Fortunato P. Benavides</a>, Senior Circuit Judge for the U.S. Court of Appeals for the Fifth Circuit, sitting by designation.</div></div></div></div><div><div class="co_footnoteNumber"><input type="hidden" class="co_starPageMetadataItem" value="{ &quot;pageset&quot;: &quot;S0a851820936611e5b86bd602cb8781fa&quot;, &quot;pageNumber&quot;: &quot;905&quot; }" alt="metadata" /><span id="co_footnote_B0022036737440"><a href="#co_footnoteReference_B0022036737440_ID0EBCAE">**</a></span></div><div class="co_footnoteBody"><div class="co_paragraph"><div class="co_paragraphText">This disposition is not appropriate for publication and is not precedent except as provided by 9th Cir. R. 36–3.</div></div></div></div></div><table id="co_endOfDocument"><tr><td>End of Document</td><td class="co_endOfDocCopyright">© 2016 Thomson Reuters. No claim to original U.S. Government Works.</td></tr></table></div><input class="co_chunkNumber" type="hidden" value="0" /><input id="co_finalChunkMarker" type="hidden" /></div><input id="co_document_metaInfo_I401e23b1310611e5b86bd602cb8781fa" type="hidden" value="{&quot;PU&quot;:null,&quot;accessControl&quot;:null,&quot;accessionNumber&quot;:&quot;&quot;,&quot;acquirerCompany&quot;:null,&quot;activeDate&quot;:null,&quot;additionalLinks&quot;:null,&quot;agreementDisplayDate&quot;:null,&quot;announcementDate&quot;:null,&quot;articleAttorneyAuthorName&quot;:null,&quot;articleFirmAuthorName&quot;:null,&quot;articleTitle&quot;:null,&quot;borrower&quot;:null,&quot;caseRequired&quot;:null,&quot;ciCompany&quot;:null,&quot;cicOfficer&quot;:null,&quot;cipOfficer&quot;:null,&quot;cite&quot;:&quot;618 Fed.Appx. 904&quot;,&quot;citeAbbreviation&quot;:null,&quot;citePrimary&quot;:null,&quot;city&quot;:null,&quot;collection&quot;:&quot;w_cs_fed1&quot;,&quot;compoundTitle&quot;:null,&quot;containerId&quot;:null,&quot;containerType&quot;:null,&quot;contentType&quot;:&quot;Cases&quot;,&quot;contentTypeId&quot;:&quot;1&quot;,&quot;correlationIds&quot;:null,&quot;country&quot;:null,&quot;court&quot;:&quot;C.A.9 (Nev.)&quot;,&quot;courtDocumentType&quot;:null,&quot;courtNumber&quot;:&quot;4197&quot;,&quot;courtYear&quot;:&quot;C.A.9 (Nev.),2015.&quot;,&quot;date&quot;:&quot;July 22, 2015&quot;,&quot;dateFile&quot;:&quot;July 22, 2015&quot;,&quot;dealDate&quot;:null,&quot;dealType&quot;:null,&quot;dealValue&quot;:null,&quot;description&quot;:null,&quot;docFamilyGuid&quot;:&quot;I401e23b2310611e5b86bd602cb8781fa&quot;,&quot;docGuid&quot;:&quot;I401e23b1310611e5b86bd602cb8781fa&quot;,&quot;docLink&quot;:&quot;https://1.next.westlaw.com/Document/I401e23b1310611e5b86bd602cb8781fa/View/FullText.html?originationContext=document&amp;contextData=(sc.Search)&amp;needToInjectTerms=False&quot;,&quot;documentTitle&quot;:null,&quot;edgarFileNumber&quot;:null,&quot;entityId&quot;:null,&quot;expertType&quot;:null,&quot;fileName&quot;:null,&quot;fileNumber&quot;:&quot;&quot;,&quot;fileSize&quot;:0,&quot;fileType&quot;:null,&quot;filerCik&quot;:null,&quot;filerName&quot;:null,&quot;filingDate&quot;:null,&quot;filingYear&quot;:null,&quot;firmName&quot;:null,&quot;formNumber&quot;:null,&quot;formSubType&quot;:null,&quot;formType&quot;:null,&quot;formTypeDisplay&quot;:null,&quot;formVolume&quot;:null,&quot;functionalCite&quot;:&quot;618 Fed.Appx. 904&quot;,&quot;fundFirmCompoundTitle&quot;:null,&quot;fundLocation&quot;:null,&quot;fundName&quot;:null,&quot;fundTargetSize&quot;:null,&quot;fundType&quot;:null,&quot;fundYear&quot;:null,&quot;fundraisingStatus&quot;:null,&quot;getTocData&quot;:false,&quot;hasDraftingNotes&quot;:null,&quot;impersonationKey&quot;:null,&quot;inlineKeyCiteFlagsIncluded&quot;:false,&quot;inlineKeyCiteFlagsResolutionStatus&quot;:null,&quot;insiderName&quot;:null,&quot;ip_assignmentsAction&quot;:null,&quot;ip_citeParallel&quot;:null,&quot;ip_derwentPublishedDate&quot;:null,&quot;ip_docket&quot;:null,&quot;ip_documentDate&quot;:&quot;July 22, 2015&quot;,&quot;ip_issuedDate&quot;:null,&quot;ip_litAlertAttorney&quot;:null,&quot;ip_patStatCode&quot;:null,&quot;ip_patentOwner&quot;:null,&quot;ip_publishedDate&quot;:null,&quot;ip_shortTitle&quot;:null,&quot;isDisplayMiniReport&quot;:false,&quot;isGatewayDocument&quot;:false,&quot;isLargeDocument&quot;:false,&quot;isPersistedContent&quot;:false,&quot;isPublicRecordsBlockedByPermissibleUse&quot;:false,&quot;isPublicRecordsBlockedBySocialSecurityAdmin&quot;:false,&quot;isPublicRecordsDocument&quot;:false,&quot;isRegChangeDocument&quot;:false,&quot;isSecureContent&quot;:false,&quot;issueDate&quot;:null,&quot;issuerName&quot;:null,&quot;jobDescription&quot;:null,&quot;jurisAbbrev&quot;:null,&quot;jurisdiction&quot;:&quot;NV&quot;,&quot;jurisdictionFacet&quot;:&quot;Federal|**|Cts. of Appeals|**|9th Cir.&quot;,&quot;jurisdictionText&quot;:&quot;Nevada&quot;,&quot;knos&quot;:null,&quot;lastRoundExitComb&quot;:null,&quot;legacyId&quot;:&quot;2036737440&quot;,&quot;letterType&quot;:null,&quot;locationOfIncorporation&quot;:null,&quot;maxOfferingPrice&quot;:null,&quot;natureOfTransaction&quot;:null,&quot;newsImageHrefLarge&quot;:null,&quot;newsImageHrefSmall&quot;:null,&quot;normalizedDocType&quot;:null,&quot;normalizedFormType&quot;:null,&quot;offeringType&quot;:null,&quot;organizationName&quot;:null,&quot;pageCount&quot;:null,&quot;persistedDocGuid&quot;:null,&quot;portfolioCompanyLocation&quot;:null,&quot;portfolioCompanyName&quot;:null,&quot;prMetaInfo1&quot;:null,&quot;prMetaInfo2&quot;:null,&quot;prMetaInfo3&quot;:null,&quot;prMetaInfo4&quot;:null,&quot;prMetaInfo5&quot;:null,&quot;primaryEditorialService&quot;:null,&quot;profileType&quot;:null,&quot;pubSeries&quot;:null,&quot;questionText&quot;:null,&quot;redlined&quot;:false,&quot;registrationDate&quot;:null,&quot;renditionId&quot;:null,&quot;royaltyId&quot;:&quot;0&quot;,&quot;rulebookNViews&quot;:null,&quot;serialNumber&quot;:&quot;2036737440&quot;,&quot;status&quot;:null,&quot;subContentType&quot;:&quot;Caselaw - NRS&quot;,&quot;subContentTypeId&quot;:&quot;27&quot;,&quot;subTitle&quot;:null,&quot;targetCompany&quot;:null,&quot;testimonyType&quot;:null,&quot;titleHtml&quot;:&quot;Crazy Ely Western Village, LLC v. City of Las Vegas&quot;,&quot;titleText&quot;:&quot;Crazy Ely Western Village, LLC v. City of Las Vegas&quot;,&quot;totalAmountIssuedWithCurrency&quot;:null,&quot;totalPages&quot;:&quot;&quot;,&quot;trademarkStatus&quot;:null,&quot;transactionAmountWithCurrency&quot;:null,&quot;transactionValue&quot;:null,&quot;valuationComb&quot;:null,&quot;westlawDatabaseIdentifier&quot;:&quot;AWFED2&quot;,&quot;westlawDocumentNumber&quot;:&quot;1180978&quot;}" /><input id="co_document_documentNavigation_Search_Search-v3-search-results-navigation-i0ad705250000015516bedc5391b305f7-Nav-CASE-fragmentIdentifier-I29ff453b835211e5b86bd602cb8781fa-startIndex-1-contextData--28sc.Search-29-transitionType-SearchItem_CASE_7" type="hidden" value="{&quot;CurrentPosition&quot;:7,&quot;EnableConceptCounts&quot;:false,&quot;HighlightPoints&quot;:null,&quot;HighlightTerms&quot;:[&quot;commercial&quot;,&quot;speech&quot;,&quot;zauderer&quot;,&quot;centr&quot;,&quot;hudson&quot;],&quot;InPlanUrl&quot;:null,&quot;IsSnapSnippet&quot;:false,&quot;ListCount&quot;:262,&quot;Message&quot;:null,&quot;NextDocument&quot;:{&quot;SkipLinkOutDoc&quot;:false,&quot;Title&quot;:&quot;POM Wonderful, LLC v. F.T.C.&quot;,&quot;Url&quot;:&quot;/Document/I359fa5aca8b111e4b4bafa136b480ad2/View/FullText.html?navigationPath=Search%2Fv3%2Fsearch%2Fresults%2Fnavigation%2Fi0ad705250000015516bedc5391b305f7%3FNav%3DCASE%26fragmentIdentifier%3DI29ff453b835211e5b86bd602cb8781fa%26startIndex%3D1%26contextData%3D%2528sc.Search%2529%26transitionType%3DSearchItem&amp;listSource=Search&amp;list=CASE&amp;rank=8&amp;grading=na&amp;sessionScopeId=bd8d225c659811e42c46d5f18138c2f937ca05d9fe97c7aaf12ccbc0ca15e48e&amp;originationContext=previousnextdocument&amp;transitionType=SearchItem&amp;contextData=%28sc.Search%29&amp;listPageSource=6f25ba1e16c760ebf11095b26d70afce&quot;},&quot;NovusQueryType&quot;:&quot;SEARCH&quot;,&quot;NovusSearchResult&quot;:&quot;i0ad823510000015516be911dda84d797&quot;,&quot;NumberOfSnips&quot;:4,&quot;PreviousDocument&quot;:{&quot;SkipLinkOutDoc&quot;:false,&quot;Title&quot;:&quot;National Ass&#39;n of Manufacturers v. S.E.C.&quot;,&quot;Url&quot;:&quot;/Document/Ic6bcdf6d4ffb11e5b4bafa136b480ad2/View/FullText.html?navigationPath=Search%2Fv3%2Fsearch%2Fresults%2Fnavigation%2Fi0ad705250000015516bedc5391b305f7%3FNav%3DCASE%26fragmentIdentifier%3DI29ff453b835211e5b86bd602cb8781fa%26startIndex%3D1%26contextData%3D%2528sc.Search%2529%26transitionType%3DSearchItem&amp;listSource=Search&amp;list=CASE&amp;rank=6&amp;grading=na&amp;sessionScopeId=bd8d225c659811e42c46d5f18138c2f937ca05d9fe97c7aaf12ccbc0ca15e48e&amp;originationContext=previousnextdocument&amp;transitionType=SearchItem&amp;contextData=%28sc.Search%29&amp;listPageSource=6f25ba1e16c760ebf11095b26d70afce&quot;},&quot;ReturnTo&quot;:{&quot;SkipLinkOutDoc&quot;:false,&quot;Title&quot;:&quot;list&quot;,&quot;Url&quot;:&quot;/Search/Results.html?query=adv%3A%20HE%28%22commercial%20speech%22%29%20%26%20%28zauderer%20%22centr%21%20hudson%22%29&amp;jurisdiction=CTA&amp;contentType=CASE&amp;querySubmissionGuid=i0ad705250000015516bedc5391b305f7&amp;searchId=i0ad705250000015516be90c149d3b25c&amp;transitionType=ReturnToList&amp;contextData=%28sc.Search%29#I29ff453b835211e5b86bd602cb8781fa&quot;},&quot;SearchQuery&quot;:&quot;adv: HE(\&quot;commercial speech\&quot;) &amp; (zauderer \&quot;centr! hudson\&quot;)&quot;,&quot;SearchQueryType&quot;:&quot;TERMS_AND_CONNECTORS&quot;,&quot;SearchWithinQuery&quot;:null,&quot;SecondaryHighlightTerms&quot;:[],&quot;ShowSkipOutOfPlanOption&quot;:false}" /><div id="co_nrsOutline" class="co_hideState"><div><div><a href="#co_synopsis">Synopsis</a></div><div><a href="#co_headnoteHeader">West Headnotes</a></div><div><a href="#co_attorneysAndLawFirms">Attorneys and Law Firms</a></div><div><a href="#co_opinion">Opinion</a></div><div><a href="#co_allCitations">All Citations</a></div></div></div><input id="co_documentContentCacheKey" type="hidden" value="WestlawNext|none|I401e23b1310611e5b86bd602cb8781fa||||||Search|Search/v3/search/results/navigation/i0ad705250000015516bedc5391b305f7?Nav=CASE&amp;fragmentIdentifier=I29ff453b835211e5b86bd602cb8781fa&amp;startIndex=1&amp;contextData=%28sc.Search%29&amp;transitionType=SearchItem|CASE|7|False|{&#34;HighlightPoints&#34;:null,&#34;HighlightTerms&#34;:null,&#34;SecondaryHighlightTerms&#34;:null}|False|||False|False|||True|S|False|Core|||010|False|False|False|False|False|"/>

</div>



</div>

</div>

</div>

</div>

<!-- LEFT COLUMN -->

<div id="co_leftColumn">

<div class="co_innertube">

<div id="coid_website_folderingWidgetDiv"></div>



</div>

</div>







<!-- RIGHT COLUMN -->

<div id="co_rightColumn">

<div class="co_innertube">

<div id="coid_website_relatedInfoIPWidgetDiv" >

</div>





<div id="coid_website_documentToolWidgetDiv"></div>



<div id="coid_website_relatedInfoWidgetDiv">



<div id="" class="co_progressIndicator">

<img src='https://ca.next.westlaw.com/StaticContent_32.0.2006/css/v2/images/co_loading_small.gif' />

<span></span>

</div>



</div>

<div id="coid_website_recommendedDocuments" class="co_reccomendedDocumentContainer">

</div>





<div id="downloadUserDocument"></div>

<div id="downloadUserDocument"></div>

</div>

</div>





<input class="hideTopTopics" type="hidden" id="hideTopTopics" name="hideTopTopics" value="False" />







<div class="co_clear"></div>

</div>





<!-- BEGIN FOOTER -->

<div id="co_footerContainer">



<div class="co_innertube" id="co_footer" style="display:none;" >









<div id="co_trLogo" class="co_floatRight">



<a id="co_trLogo_link" href="#" onclick="website_LinkoutAndShowTimeoutLightboxExternal('http://www.thomsonreuters.com', 'aboutwestlaw')">

<img alt="Thomson Reuters" height="30" width="134" src="https://ia.next.westlaw.com/StaticContent_32.0.2006/images/v2/co_logo_thomsonReuters.png" />

</a>

</div>

<div id="co_footerLinks">



<ul class="co_inlineList">



<li><a id="coid_websiteFooter_userSettings" href="javascript:void(0);" onclick="website_PublishUserSettingsFooterLinkClickedEvent()"><span class="icon25 icon_gear_document"></span>Preferences</a></li>



<li><a id="coid_websiteFooter_contacts" href="javascript:void(0);" onclick="website_PublishMyContactsFooterLinkClickedEvent()"><span class="icon25 icon_contacts_folder"></span>My Contacts<span class="co_accessibilityLabel"> Global</span></a></li>



<li><a id="coid_websiteFooter_helplink" href="javascript:void(0);" onclick="website_LinkoutAndShowTimeoutLightboxExternal('http://legalsolutions.thomsonreuters.com/law-products/westlaw-legal-research/training-support', 'Help')"><span class="icon25 icon_question_mark"></span>Help</a></li>

<li id="co_footerLiveChat"></li>



<li><a id="coid_websiteFooter_signofflink" href="javascript:void(0);" onclick="javascript:Cobalt.Master.Instance().SignOffManually();return false;"><span class="icon25 icon_exit_door"></span>Sign Off</a></li>



</ul>

</div>

<div id="co_footerCopyright">

<ul class="co_inlineList">



<li>Westlaw. <a href="/Copyright?transitionType=Default&contextData=(sc.Default)"> © 2016</a> Thomson Reuters</li>

<li><a href="/Privacy?transitionType=Default&contextData=(sc.Default)">Privacy Statement</a></li>



<li><a href="/Accessibility?transitionType=Default&contextData=(sc.Default)">Accessibility</a></li>



<li id="co_footer_supplier"><a href="javascript:void(0);" onclick="website_LinkoutAndShowTimeoutLightboxExternal('http://legalsolutions.com/westlaw-additional-terms')">Supplier Terms</a></li>

<li id="co_footerContactUs"><a href="/ContactUs?transitionType=Default&contextData=(sc.Default)">Contact Us</a></li>

<li id="co_footerCs">1-800-REF-ATTY (1-800-733-2889)</li>

<li id="co_footer_improve"><strong><a id="coid_websiteFooter_pageSurvey" href="javascript:void(0);" onclick="website_PageSurveyFooterLinkClickedEvent()">Improve Westlaw</a></strong></li>



</ul>

</div>



</div>

</div>







<div id="coid_Trmr" style="display:none; visibility:hidden"></div>

</div>

</div>

</body>

</html>
'''
