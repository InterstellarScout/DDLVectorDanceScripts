#!/usr/bin/env python3

# Copyright (c) 2019 acidzebra
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# for use with Anki's awesome Vector robot: https://www.anki.com/en-us/vector
# Source: https://gist.github.com/acidzebra/5e23b6dd46e3bee93e12b561e431ce68
#
import nltk
import anki_vector

bigramlist = {
("th","anim_blackjack_getin_01"),
("he","anim_blackjack_deal_01"),
("in","anim_inspectheldcube_cubemissing_01"),
("er","anim_message_getin_01"),
("an","anim_hiking_react_05"),
("re","anim_lookatphone_getin_01"),
("on","anim_keepaway_getout_frustrated_01"),
("at","anim_eyecontact_squint_01"),
("en","anim_reacttoblock_ask_01_0"),
("nd","anim_movement_comehere_reaction_01"),
("ti","anim_feedback_bequiet_01"),
("es","anim_fistbump_fail_01"),
("or","anim_eyecontact_giggle_01"),
("te","anim_inspectheldcube_cubemissing_01"),
("of","anim_reacttoblock_happydetermined_02"),
("ed","anim_hiking_react_05"),
("is","anim_message_getin_01"),
("it","anim_blackjack_spread_01"),
("al","anim_lookatphone_getin_01"),
("ar","anim_petting_bliss_getout_01"),
("st","anim_photo_shutter_01"),
("to","anim_blackjack_getin_01"),
("nt","anim_petting_lvl2_01"),
("ng","anim_hiking_react_06"),
("se","anim_reacttoblock_react_short_01"),
("ha","anim_knowledgegraph_success_01"),
("as","anim_blackjack_victorbjackwin_01"),
("ou","anim_handdetection_reaction_01"),
("io","anim_feedback_bequiet_01"),
("le","anim_knowledgegraph_fail_01"),
("ve","anim_petting_bliss_getout_01"),
("co","anim_inspectheldcube_cubemissing_01"),
("me","anim_eyecontact_squint_01"),
("de","anim_message_getin_01"),
("hi","anim_blackjack_deal_01"),
("ri","anim_keepaway_getout_frustrated_01"),
("ro","anim_eyecontact_giggle_01"),
("ic","anim_blackjack_spread_01"),
("ne","anim_greeting_imhome_01"),
("ea","anim_reacttoblock_ask_01_0"),
("ra","anim_blackjack_getin_01"),
("ce","anim_movement_comehere_reaction_01"),
("li","anim_hiking_react_05"),
("ch","anim_fistbump_fail_01"),
("ll","anim_lookatphone_getin_01"),
("be","anim_reacttoblock_happydetermined_02"),
("ma","anim_petting_lvl2_01"),
("si","anim_inspectheldcube_cubemissing_01"),
("om","anim_photo_shutter_01"),
("ur","anim_feedback_bequiet_01"),
("ca","anim_reacttoblock_react_short_01"),
("el","anim_hiking_react_06"),
("ta","anim_knowledgegraph_success_01"),
("la","anim_knowledgegraph_fail_01"),
("ns","anim_hiking_react_05"),
("di","anim_blackjack_victorbjackwin_01"),
("fo","anim_message_getin_01"),
("ho","anim_petting_bliss_getout_01"),
("pe","anim_handdetection_reaction_01"),
("ec","anim_eyecontact_squint_01"),
("pr","anim_blackjack_deal_01"),
("no","anim_keepaway_getout_frustrated_01"),
("ct","anim_blackjack_spread_01"),
("us","anim_explorer_huh_far_01"),
("ac","anim_reacttoblock_ask_01_0"),
("ot","anim_lookatphone_getin_01"),
("il","anim_eyecontact_giggle_01"),
("tr","anim_reacttocliff_huh_01"),
("ly","anim_reacttoblock_happydetermined_02"),
("nc","anim_feedback_bequiet_01"),
("et","anim_movement_comehere_reaction_01"),
("ut","anim_fistbump_fail_01"),
("ss","anim_inspectheldcube_cubemissing_01"),
("so","anim_petting_lvl2_01"),
("rs","anim_photo_shutter_01"),
("un","anim_hiking_react_05"),
("lo","anim_reacttoblock_react_short_01"),
("wa","anim_knowledgegraph_success_01"),
("ge","anim_message_getin_01"),
("ie","anim_greeting_imhome_01"),
("wh","anim_hiking_react_06"),
("ee","anim_blackjack_deal_01"),
("wi","anim_blackjack_victorbjackwin_01"),
("em","anim_petting_bliss_getout_01"),
("ad","anim_keepaway_getout_frustrated_01"),
("ol","anim_handdetection_reaction_01"),
("rt","anim_blackjack_spread_01"),
("po","anim_lookatphone_getin_01"),
("we","anim_reacttoblock_ask_01_0"),
("na","anim_eyecontact_squint_01"),
("ul","anim_knowledgegraph_fail_01"),
("ni","anim_blackjack_getin_01"),
("ts","anim_keepaway_hit_reaction_01"),
("mo","anim_eyecontact_giggle_01"),
("ow","anim_reacttocliff_huh_01"),
("pa","anim_reacttoblock_happydetermined_02"),
("im","anim_hiking_react_05"),
("mi","anim_inspectheldcube_cubemissing_01"),
("ai","anim_movement_comehere_reaction_01"),
("sh","anim_feedback_bequiet_01"),
("ir","anim_fistbump_fail_01"),
("su","anim_reacttoblock_react_short_01"),
("id","anim_photo_shutter_01"),
("os","anim_keepaway_getout_frustrated_01"),
("iv","anim_petting_lvl2_01"),
("ia","anim_message_getin_01"),
("am","anim_hiking_react_06"),
("fi","anim_blackjack_deal_01"),
("ci","anim_petting_bliss_getout_01"),
("vi","anim_knowledgegraph_success_01"),
("pl","anim_explorer_huh_far_01"),
("ig","anim_blackjack_spread_01"),
("tu","anim_greeting_imhome_01"),
("ev","anim_blackjack_victorbjackwin_01"),
("ld","anim_handdetection_reaction_01"),
("ry","anim_lookatphone_getin_01"),
("mp","anim_eyecontact_squint_01"),
("fe","anim_inspectheldcube_cubemissing_01"),
("bl","anim_reacttoblock_ask_01_0"),
("ab","anim_hiking_react_05"),
("gh","anim_petting_lvl3_01"),
("ty","anim_reacttoblock_react_short_01"),
("op","anim_reacttocliff_huh_01"),
("wo","anim_feedback_bequiet_01"),
("sa","anim_eyecontact_giggle_01"),
("ay","anim_photo_shutter_01"),
("ex","anim_reacttoblock_happydetermined_02"),
("ke","anim_blackjack_getin_01"),
("fr","anim_movement_comehere_reaction_01"),
("oo","anim_message_getin_01"),
("av","anim_fistbump_fail_01"),
("ag","anim_keepaway_getout_frustrated_01"),
("if","anim_hiking_react_06"),
("ap","anim_knowledgegraph_success_01"),
("gr","anim_petting_lvl2_01"),
("od","anim_hiking_react_05"),
("bo","anim_lookatphone_getin_01"),
("sp","anim_petting_bliss_getout_01"),
("rd","anim_blackjack_victorbjackwin_01"),
("do","anim_blackjack_deal_01"),
("uc","anim_eyecontact_squint_01"),
("bu","anim_greeting_imhome_01"),
("ei","anim_reacttoblock_react_short_01"),
("ov","anim_knowledgegraph_fail_01"),
("by","anim_handdetection_reaction_01"),
("rm","anim_keepaway_hit_reaction_01"),
("ep","anim_reacttoblock_happydetermined_02"),
("tt","anim_reacttocliff_huh_01"),
("oc","anim_explorer_huh_far_01"),
("fa","anim_reacttoblock_ask_01_0"),
("ef","anim_message_getin_01"),
("cu","anim_inspectheldcube_cubemissing_01"),
("rn","anim_fistbump_fail_01"),
("sc","anim_hiking_react_05"),
("gi","anim_eyecontact_giggle_01"),
("da","anim_blackjack_spread_01"),
("yo","anim_feedback_bequiet_01"),
("cr","anim_movement_comehere_reaction_01"),
("cl","anim_lookatphone_getin_01"),
("du","anim_photo_shutter_01"),
("ga","anim_hiking_react_06"),
("qu","anim_knowledgegraph_success_01"),
("ue","anim_petting_lvl2_01"),
("ff","anim_keepaway_getout_frustrated_01"),
("ba","anim_blackjack_deal_01"),
("ey","anim_petting_bliss_getout_01"),
("ls","anim_reacttoblock_react_short_01"),
("va","anim_blackjack_victorbjackwin_01"),
("um","anim_eyecontact_squint_01"),
("pp","anim_greeting_imhome_01"),
("ua","anim_petting_lvl3_01"),
("up","anim_handdetection_reaction_01"),
("lu","anim_inspectheldcube_cubemissing_01"),
("go","anim_blackjack_getin_01"),
("ht","anim_reacttocliff_huh_01"),
("ru","anim_reacttoblock_ask_01_0"),
("ug","anim_message_getin_01"),
("ds","anim_hiking_react_05"),
("lt","anim_knowledgegraph_success_01"),
("pi","anim_knowledgegraph_fail_01"),
("rc","anim_fistbump_fail_01"),
("rr","anim_reacttoblock_happydetermined_02"),
("eg","anim_blackjack_spread_01"),
("au","anim_eyecontact_giggle_01"),
("ck","anim_reacttoblock_react_short_01"),
("ew","anim_keepaway_getout_frustrated_01"),
("mu","anim_feedback_bequiet_01"),
("br","anim_movement_comehere_reaction_01"),
("bi","anim_hiking_react_06"),
("pt","anim_petting_lvl2_01"),
("ak","anim_blackjack_victorbjackwin_01"),
("pu","anim_lookatphone_getin_01"),
("ui","anim_petting_bliss_getout_01"),
("rg","anim_photo_shutter_01"),
("ib","anim_explorer_huh_far_01"),
("tl","anim_blackjack_deal_01"),
("ny","anim_keepaway_hit_reaction_01"),
("ki","anim_greeting_imhome_01"),
("rk","anim_eyecontact_squint_01"),
("ys","anim_knowledgegraph_success_01"),
("ob","anim_petting_lvl3_01"),
("mm","anim_reacttoblock_ask_01_0"),
("fu","anim_hiking_react_05"),
("ph","anim_message_getin_01"),
("og","anim_inspectheldcube_cubemissing_01"),
("ms","anim_reacttoblock_react_short_01"),
("ye","anim_fistbump_fail_01"),
("ud","anim_blackjack_getin_01"),
("mb","anim_launch_cubediscovery"),
("ip","anim_reacttoblock_happydetermined_02"),
("ub","anim_reacttocliff_huh_01"),
("oi","anim_blackjack_spread_01"),
("rl","anim_eyecontact_giggle_01"),
("gu","anim_keepaway_getout_frustrated_01"),
("dr","anim_movement_comehere_reaction_01"),
("hr","anim_hiking_react_06"),
("cc","anim_lookatphone_getin_01"),
("tw","anim_petting_bliss_getout_01"),
("ft","anim_handdetection_reaction_01"),
("wn","anim_feedback_bequiet_01"),
("nu","anim_petting_lvl2_01"),
("af","anim_reacttoblock_react_short_01"),
("hu","anim_photo_shutter_01"),
("nn","anim_eyecontact_squint_01"),
("eo","anim_hiking_react_05"),
("vo","anim_knowledgegraph_fail_01"),
("rv","anim_explorer_huh_far_01"),
("nf","anim_feedback_bequiet_01"),
("xp","anim_blackjack_victorbjackwin_01"),
("gn","anim_knowledgegraph_success_01"),
("sm","anim_reacttocliff_huh_01"),
("fl","anim_handdetection_reaction_01"),
("iz","anim_reacttoblock_ask_01_0"),
("ok","anim_inspectheldcube_cubemissing_01"),
("nl","anim_blackjack_deal_01"),
("my","anim_reacttoblock_happydetermined_02"),
("gl","anim_fistbump_fail_01"),
("aw","anim_reacttoblock_react_short_01"),
("ju","anim_eyecontact_giggle_01"),
("oa","anim_keepaway_getout_frustrated_01"),
("eq","anim_movement_comehere_reaction_01"),
("sy","anim_message_getin_01"),
("sl","anim_blackjack_spread_01"),
("ps","anim_lookatphone_getin_01"),
("jo","anim_hiking_react_06"),
("lf","anim_greeting_imhome_01"),
("nv","anim_petting_bliss_getout_01"),
("je","anim_petting_lvl2_01"),
("nk","anim_hiking_react_05"),
("kn","anim_keepaway_hit_reaction_01"),
("gs","anim_explorer_huh_far_01"),
("dy","anim_eyecontact_squint_01"),
("hy","anim_blackjack_getin_01"),
("ze","anim_photo_shutter_01"),
("ks","anim_petting_lvl3_01"),
("xt","anim_knowledgegraph_success_01"),
("bs","anim_blackjack_victorbjackwin_01"),
("ik","anim_knowledgegraph_fail_01"),
("dd","anim_inspectheldcube_cubemissing_01"),
("cy","anim_reacttoblock_happydetermined_02"),
("rp","anim_handdetection_reaction_01"),
("sk","anim_hiking_react_05"),
("xi","anim_reacttoblock_ask_01_0"),
("oe","anim_message_getin_01"),
("oy","anim_reacttoblock_react_short_01"),
("ws","anim_hiking_react_06"),
("lv","anim_lookatphone_getin_01"),
("dl","anim_eyecontact_giggle_01"),
("rf","anim_movement_comehere_reaction_01"),
("eu","anim_feedback_bequiet_01"),
("dg","anim_blackjack_spread_01"),
("wr","anim_petting_bliss_getout_01"),
("xa","anim_keepaway_getout_frustrated_01"),
("yi","anim_blackjack_deal_01"),
("nm","anim_fistbump_fail_01"),
("eb","anim_petting_lvl2_01"),
("rb","anim_reacttocliff_huh_01"),
("tm","anim_knowledgegraph_success_01"),
("xc","anim_eyecontact_squint_01"),
("eh","anim_photo_shutter_01"),
("tc","anim_greeting_imhome_01"),
("gy","anim_explorer_huh_far_01"),
("ja","anim_handdetection_reaction_01"),
("hn","anim_hiking_react_05"),
("yp","anim_reacttoblock_ask_01_0"),
("za","anim_reacttoblock_happydetermined_02"),
("gg","anim_message_getin_01"),
("ym","anim_reacttoblock_react_short_01"),
("sw","anim_keepaway_hit_reaction_01"),
("bj","anim_inspectheldcube_cubemissing_01"),
("lm","anim_blackjack_getin_01"),
("cs","anim_blackjack_victorbjackwin_01"),
("ii","anim_blackjack_spread_01"),
("ix","anim_hiking_react_06"),
("xe","anim_knowledgegraph_fail_01"),
("oh","anim_lookatphone_getin_01"),
("lk","anim_movement_comehere_reaction_01"),
("dv","anim_eyecontact_giggle_01"),
("lp","anim_petting_bliss_getout_01"),
("ax","anim_reacttocliff_huh_01"),
("ox","anim_feedback_bequiet_01"),
("uf","anim_knowledgegraph_success_01"),
("dm","anim_fistbump_fail_01"),
("iu","anim_keepaway_getout_frustrated_01"),
("sf","anim_petting_lvl2_01"),
("bt","anim_photo_shutter_01"),
("ka","anim_hiking_react_05"),
("yt","anim_eyecontact_squint_01"),
("ek","anim_explorer_huh_far_01"),
("pm","anim_handdetection_reaction_01"),
("ya","anim_blackjack_deal_01"),
("gt","anim_reacttoblock_ask_01_0"),
("wl","anim_inspectheldcube_cubemissing_01"),
("rh","anim_reacttoblock_react_short_01"),
("yl","anim_reacttoblock_happydetermined_02"),
("hs","anim_petting_lvl3_01"),
("ah","anim_knowledgegraph_success_01"),
("yc","anim_blackjack_spread_01"),
("yn","anim_greeting_imhome_01"),
("rw","anim_message_getin_01"),
("hm","anim_movement_comehere_reaction_01"),
("lw","anim_hiking_react_06"),
("hl","anim_keepaway_hit_reaction_01"),
("ae","anim_lookatphone_getin_01"),
("zi","anim_petting_bliss_getout_01"),
("az","anim_blackjack_getin_01"),
("lc","anim_eyecontact_giggle_01"),
("py","anim_keepaway_getout_frustrated_01"),
("aj","anim_blackjack_victorbjackwin_01"),
("iq","anim_knowledgegraph_fail_01"),
("nj","anim_reacttocliff_huh_01"),
("bb","anim_hiking_react_05"),
("nh","anim_photo_shutter_01"),
("uo","anim_petting_lvl2_01"),
("kl","anim_inspectheldcube_cubemissing_01"),
("lr","anim_fistbump_fail_01"),
("tn","anim_reacttoblock_ask_01_0"),
("gm","anim_eyecontact_squint_01"),
("sn","anim_feedback_bequiet_01"),
("nr","anim_reacttoblock_react_short_01"),
("fy","anim_handdetection_reaction_01"),
("mn","anim_reacttoblock_happydetermined_02"),
("dw","anim_explorer_huh_far_01"),
("sb","anim_launch_cubediscovery"),
("yr","anim_message_getin_01"),
("dn","anim_blackjack_deal_01"),
("sq","anim_knowledgegraph_success_01"),
("zo","anim_petting_lvl3_01"),
("oj","anim_lookatphone_getin_01"),
("yd","anim_movement_comehere_reaction_01"),
("lb","anim_hiking_react_06"),
("wt","anim_blackjack_spread_01"),
("lg","anim_reacttoblock_react_short_01"),
("ko","anim_keepaway_hit_reaction_01"),
("np","anim_inspectheldcube_cubemissing_01"),
("sr","anim_hiking_react_05"),
("nq","anim_greeting_imhome_01"),
("ky","anim_eyecontact_giggle_01"),
("ln","anim_petting_bliss_getout_01"),
("nw","anim_reacttocliff_huh_01"),
("tf","anim_blackjack_victorbjackwin_01"),
("fs","anim_knowledgegraph_fail_01"),
("cq","anim_petting_lvl2_01"),
("dh","anim_fistbump_fail_01"),
("sd","anim_keepaway_getout_frustrated_01"),
("vy","anim_blackjack_deal_01"),
("dj","anim_eyecontact_squint_01"),
("hw","anim_reacttoblock_ask_01_0"),
("xu","anim_reacttoblock_happydetermined_02"),
("ao","anim_photo_shutter_01"),
("ml","anim_hiking_react_05"),
("uk","anim_message_getin_01"),
("uy","anim_handdetection_reaction_01"),
("ej","anim_hiking_react_06"),
("ez","anim_inspectheldcube_cubemissing_01"),
("hb","anim_lookatphone_getin_01"),
("nz","anim_movement_comehere_reaction_01"),
("nb","anim_blackjack_getin_01"),
("mc","anim_reacttoblock_react_short_01"),
("yb","anim_knowledgegraph_success_01"),
("tp","anim_explorer_huh_far_01"),
("xh","anim_blackjack_spread_01"),
("ux","anim_launch_cubediscovery"),
("tz","anim_keepaway_hit_reaction_01"),
("bv","anim_feedback_bequiet_01"),
("mf","anim_greeting_imhome_01"),
("wd","anim_eyecontact_giggle_01"),
("oz","anim_petting_lvl3_01"),
("yw","anim_petting_bliss_getout_01"),
("kh","anim_petting_lvl2_01"),
("gd","anim_reacttoblock_happydetermined_02"),
("bm","anim_fistbump_fail_01"),
("mr","anim_keepaway_getout_frustrated_01"),
("ku","anim_hiking_react_05"),
("uv","anim_eyecontact_squint_01"),
("dt","anim_reacttoblock_ask_01_0"),
("hd","anim_photo_shutter_01"),
("aa","anim_lookatphone_getin_01"),
("xx","anim_hiking_react_06"),
("df","anim_blackjack_victorbjackwin_01"),
("db","anim_message_getin_01"),
("ji","anim_inspectheldcube_cubemissing_01"),
("kr","anim_blackjack_getin_01"),
("xo","anim_movement_comehere_reaction_01"),
("cm","anim_reacttocliff_huh_01"),
("zz","anim_reacttoblock_react_short_01"),
("nx","anim_knowledgegraph_success_01"),
("yg","anim_blackjack_spread_01"),
("xy","anim_handdetection_reaction_01"),
("kg","anim_knowledgegraph_fail_01"),
("tb","anim_launch_cubediscovery"),
("dc","anim_hiking_react_05"),
("bd","anim_eyecontact_giggle_01"),
("sg","anim_keepaway_getout_frustrated_01"),
("wy","anim_feedback_bequiet_01"),
("zy","anim_explorer_huh_far_01"),
("aq","anim_petting_bliss_getout_01"),
("hf","anim_petting_lvl2_01"),
("cd","anim_blackjack_deal_01"),
("vu","anim_reacttoblock_happydetermined_02"),
("kw","anim_greeting_imhome_01"),
("zu","anim_petting_lvl3_01"),
("bn","anim_fistbump_fail_01"),
("ih","anim_reacttoblock_ask_01_0"),
("tg","anim_lookatphone_getin_01"),
("xv","anim_eyecontact_squint_01"),
("uz","anim_photo_shutter_01"),
("bc","anim_movement_comehere_reaction_01"),
("xf","anim_inspectheldcube_cubemissing_01"),
("yz","anim_hiking_react_06"),
("km","anim_reacttoblock_react_short_01"),
("dp","anim_message_getin_01"),
("lh","anim_hiking_react_05"),
("wf","anim_reacttocliff_huh_01"),
("kf","anim_knowledgegraph_success_01"),
("pf","anim_blackjack_spread_01"),
("cf","anim_keepaway_hit_reaction_01"),
("mt","anim_blackjack_victorbjackwin_01"),
("yu","anim_launch_cubediscovery"),
("cp","anim_eyecontact_giggle_01"),
("pb","anim_knowledgegraph_fail_01"),
("td","anim_lookatphone_getin_01"),
("zl","anim_feedback_bequiet_01"),
("sv","anim_blackjack_getin_01"),
("hc","anim_keepaway_getout_frustrated_01"),
("mg","anim_petting_bliss_getout_01"),
("pw","anim_handdetection_reaction_01"),
("gf","anim_reacttoblock_happydetermined_02"),
("pd","anim_petting_lvl2_01"),
("pn","anim_reacttoblock_react_short_01"),
("pc","anim_explorer_huh_far_01"),
("rx","anim_eyecontact_squint_01"),
("tv","anim_blackjack_victorbjackwin_01"),
("ij","anim_reacttoblock_ask_01_0"),
("wm","anim_message_getin_01"),
("uh","anim_hiking_react_05"),
("wk","anim_movement_comehere_reaction_01"),
("wb","anim_fistbump_fail_01"),
("bh","anim_photo_shutter_01"),
("oq","anim_hiking_react_06"),
("kt","anim_feedback_bequiet_01"),
("rq","anim_blackjack_getin_01"),
("kb","anim_greeting_imhome_01"),
("cg","anim_keepaway_hit_reaction_01"),
("vr","anim_knowledgegraph_success_01"),
("cn","anim_blackjack_spread_01"),
("pk","anim_knowledgegraph_fail_01"),
("uu","anim_reacttoblock_react_short_01"),
("yf","anim_lookatphone_getin_01"),
("wp","anim_petting_bliss_getout_01"),
("cz","anim_eyecontact_giggle_01"),
("kp","anim_reacttoblock_happydetermined_02"),
("dq","anim_keepaway_getout_frustrated_01"),
("wu","anim_reacttoblock_ask_01_0"),
("fm","anim_inspectheldcube_cubemissing_01"),
("wc","anim_eyecontact_squint_01"),
("md","anim_hiking_react_05"),
("kd","anim_petting_lvl2_01"),
("zh","anim_photo_shutter_01"),
("gw","anim_hiking_react_06"),
("rz","anim_blackjack_deal_01"),
("cb","anim_message_getin_01"),
("iw","anim_fistbump_fail_01"),
("xl","anim_blackjack_victorbjackwin_01"),
("hp","anim_explorer_huh_far_01"),
("mw","anim_handdetection_reaction_01"),
("vs","anim_movement_comehere_reaction_01"),
("fc","anim_lookatphone_getin_01"),
("rj","anim_feedback_bequiet_01"),
("bp","anim_reacttocliff_huh_01"),
("mh","anim_knowledgegraph_success_01"),
("hh","anim_blackjack_spread_01"),
("yh","anim_reacttoblock_react_short_01"),
("uj","anim_petting_lvl3_01"),
("fg","anim_reacttoblock_ask_01_0"),
("fd","anim_greeting_imhome_01"),
("gb","anim_keepaway_hit_reaction_01"),
("pg","anim_knowledgegraph_fail_01"),
("tk","anim_reacttoblock_happydetermined_02"),
("kk","anim_petting_bliss_getout_01"),
("hq","anim_blackjack_getin_01"),
("fn","anim_hiking_react_05"),
("lz","anim_inspectheldcube_cubemissing_01"),
("vl","anim_keepaway_getout_frustrated_01"),
("gp","anim_eyecontact_squint_01"),
("hz","anim_eyecontact_giggle_01"),
("dk","anim_photo_shutter_01"),
("yk","anim_message_getin_01"),
("qi","anim_lookatphone_getin_01"),
("lx","anim_petting_lvl2_01"),
("vd","anim_hiking_react_06"),
("zs","anim_explorer_huh_far_01"),
("bw","anim_launch_cubediscovery"),
("xq","anim_blackjack_deal_01"),
("mv","anim_fistbump_fail_01"),
("uw","anim_reacttoblock_react_short_01"),
("hg","anim_blackjack_victorbjackwin_01"),
("fb","anim_handdetection_reaction_01"),
("sj","anim_blackjack_spread_01"),
("ww","anim_reacttocliff_huh_01"),
("gk","anim_reacttoblock_ask_01_0"),
("uq","anim_movement_comehere_reaction_01"),
("bg","anim_knowledgegraph_success_01"),
("sz","anim_inspectheldcube_cubemissing_01"),
("jr","anim_keepaway_getout_frustrated_01"),
("ql","anim_feedback_bequiet_01"),
("zt","anim_reacttoblock_happydetermined_02"),
("hk","anim_hiking_react_05"),
("vc","anim_petting_lvl2_01"),
("xm","anim_petting_bliss_getout_01"),
("gc","anim_blackjack_deal_01"),
("fw","anim_eyecontact_squint_01"),
("pz","anim_hiking_react_06"),
("kc","anim_eyecontact_giggle_01"),
("hv","anim_keepaway_hit_reaction_01"),
("xw","anim_knowledgegraph_fail_01"),
("zw","anim_photo_shutter_01"),
("fp","anim_greeting_imhome_01"),
("iy","anim_message_getin_01"),
("pv","anim_blackjack_getin_01"),
("vt","anim_fistbump_fail_01"),
("jp","anim_blackjack_spread_01"),
("cv","anim_reacttoblock_react_short_01"),
("zb","anim_reacttoblock_ask_01_0"),
("vp","anim_reacttocliff_huh_01"),
("zr","anim_lookatphone_getin_01"),
("fh","anim_knowledgegraph_success_01"),
("yv","anim_inspectheldcube_cubemissing_01"),
("zg","anim_movement_comehere_reaction_01"),
("zm","anim_hiking_react_05"),
("zv","anim_blackjack_victorbjackwin_01"),
("qs","anim_feedback_bequiet_01"),
("kv","anim_handdetection_reaction_01"),
("vn","anim_reacttoblock_happydetermined_02"),
("zn","anim_explorer_huh_far_01"),
("qa","anim_keepaway_getout_frustrated_01"),
("yx","anim_blackjack_deal_01"),
("jn","anim_eyecontact_squint_01"),
("bf","anim_hiking_react_06"),
("mk","anim_petting_lvl2_01"),
("cw","anim_petting_bliss_getout_01"),
("jm","anim_photo_shutter_01"),
("lq","anim_eyecontact_giggle_01"),
("jh","anim_greeting_imhome_01"),
("kj","anim_petting_lvl3_01"),
("jc","anim_message_getin_01"),
("gz","anim_lookatphone_getin_01"),
("js","anim_reacttoblock_react_short_01"),
("tx","anim_knowledgegraph_fail_01"),
("fk","anim_fistbump_fail_01"),
("jl","anim_hiking_react_05"),
("vm","anim_blackjack_spread_01"),
("lj","anim_reacttoblock_ask_01_0"),
("tj","anim_blackjack_getin_01"),
("jj","anim_reacttoblock_happydetermined_02"),
("cj","anim_reacttocliff_huh_01"),
("vg","anim_movement_comehere_reaction_01"),
("mj","anim_inspectheldcube_cubemissing_01"),
("jt","anim_knowledgegraph_success_01"),
("pj","anim_blackjack_victorbjackwin_01"),
("wg","anim_eyecontact_squint_01"),
("vh","anim_keepaway_hit_reaction_01"),
("bk","anim_launch_cubediscovery"),
("vv","anim_hiking_react_05"),
("jd","anim_hiking_react_06"),
("tq","anim_petting_bliss_getout_01"),
("vb","anim_handdetection_reaction_01"),
("jf","anim_feedback_bequiet_01"),
("dz","anim_photo_shutter_01"),
("xb","anim_petting_lvl2_01"),
("jb","anim_greeting_imhome_01"),
("zc","anim_keepaway_getout_frustrated_01"),
("fj","anim_message_getin_01"),
("yy","anim_lookatphone_getin_01"),
("qn","anim_eyecontact_giggle_01"),
("xs","anim_reacttoblock_react_short_01"),
("qr","anim_reacttoblock_happydetermined_02"),
("jk","anim_blackjack_spread_01"),
("jv","anim_blackjack_deal_01"),
("qq","anim_knowledgegraph_fail_01"),
("xn","anim_reacttoblock_ask_01_0"),
("vf","anim_movement_comehere_reaction_01"),
("px","anim_inspectheldcube_cubemissing_01"),
("zd","anim_fistbump_fail_01"),
("qt","anim_hiking_react_06"),
("zp","anim_hiking_react_05"),
("qo","anim_explorer_huh_far_01"),
("dx","anim_petting_lvl3_01"),
("hj","anim_blackjack_getin_01"),
("gv","anim_reacttocliff_huh_01"),
("jw","anim_greeting_imhome_01"),
("qc","anim_knowledgegraph_success_01"),
("jy","anim_keepaway_hit_reaction_01"),
("gj","anim_eyecontact_squint_01"),
("qb","anim_inspectheldcube_cubemissing_01"),
("pq","anim_petting_lvl2_01"),
("jg","anim_petting_bliss_getout_01"),
("bz","anim_photo_shutter_01"),
("mx","anim_blackjack_victorbjackwin_01"),
("qm","anim_keepaway_getout_frustrated_01"),
("mz","anim_message_getin_01"),
("qf","anim_lookatphone_getin_01"),
("wj","anim_eyecontact_giggle_01"),
("zq","anim_knowledgegraph_fail_01"),
("xr","anim_blackjack_spread_01"),
("zk","anim_feedback_bequiet_01"),
("cx","anim_movement_comehere_reaction_01"),
("fx","anim_hiking_react_06"),
("fv","anim_hiking_react_05"),
("bx","anim_reacttoblock_ask_01_0"),
("vw","anim_reacttoblock_react_short_01"),
("vj","anim_reacttoblock_happydetermined_02"),
("mq","anim_launch_cubediscovery"),
("qv","anim_handdetection_reaction_01"),
("zf","anim_petting_lvl3_01"),
("qe","anim_fistbump_fail_01"),
("yj","anim_reacttocliff_huh_01"),
("gx","anim_blackjack_deal_01"),
("kx","anim_knowledgegraph_success_01"),
("xg","anim_explorer_huh_far_01"),
("qd","anim_eyecontact_squint_01"),
("xj","anim_blackjack_getin_01"),
("sx","anim_photo_shutter_01"),
("vz","anim_petting_bliss_getout_01"),
("vx","anim_greeting_imhome_01"),
("wv","anim_lookatphone_getin_01"),
("yq","anim_message_getin_01"),
("bq","anim_keepaway_getout_frustrated_01"),
("gq","anim_petting_lvl2_01"),
("vk","anim_blackjack_spread_01"),
("zj","anim_knowledgegraph_fail_01"),
("xk","anim_reacttoblock_ask_01_0"),
("qp","anim_hiking_react_05"),
("hx","anim_inspectheldcube_cubemissing_01"),
("fz","anim_movement_comehere_reaction_01"),
("qh","anim_eyecontact_giggle_01"),
("qj","anim_fistbump_fail_01"),
("jz","anim_hiking_react_06"),
("vq","anim_feedback_bequiet_01"),
("kq","anim_blackjack_victorbjackwin_01"),
("xd","anim_reacttoblock_happydetermined_02"),
("qw","anim_blackjack_deal_01"),
("jx","anim_eyecontact_squint_01"),
("qx","anim_reacttoblock_react_short_01"),
("kz","anim_knowledgegraph_success_01"),
("wx","anim_keepaway_getout_frustrated_01"),
("fq","anim_hiking_react_05"),
("xz","anim_petting_lvl2_01"),
("zx","anim_blackjack_getin_01"),
("jq","anim_petting_bliss_getout_01"),
("qg","anim_photo_shutter_01"),
("qk","anim_blackjack_spread_01"),
("qy","anim_movement_comehere_reaction_01"),
("qz","anim_reacttoblock_ask_01_0"),
("wq","anim_message_getin_01"),
("wz","anim_lookatphone_getin_01")
}

TextString = 'vector is so cool! I love him so much. Yay yay yay yay yay mmmmhmmhmmhmhmmmhmmhmhmhahahahahhhahhahhahhahhahhahhhaaaaha.'

# Insert a space inbetween each character in TextString
TextString.replace(" ", "")
spaced = ''
for ch in TextString:
    spaced = spaced + ch + ' '
# Generate bigrams out of the new spaced string
tokenized = spaced.split(" ")
myList = list(nltk.bigrams(tokenized))
# Join the items in each tuple in myList together and put them in a new list
Bigrams = []
del myList[1::2]

for i in myList:
    Bigrams.append((''.join([w for w in i])).strip())

with anki_vector.Robot() as robot:
    print ("translating ", TextString, " to Vectorian")
    for i,c in enumerate(Bigrams):
        for k,v in bigramlist:
            if k == c:
                print ("bigram ", c, " translates to ", v)
                robot.anim.play_animation(v, ignore_body_track=True, ignore_head_track=False, ignore_lift_track=True)
    print ("translation complete!")