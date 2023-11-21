#include <iostream>
#include <string>
#include <unordered_map>
#include <set>
#include <limits>

#include "homework5.cpp"

/*
Test Case solutions:

Gradescope working properly - should be always correct, please ignore
YES_NO_NO
NO_NO_NO_NO_YES

YES_YES_NO_YES
YES_NO_NO_NO_NO_NO_YES_YES_NO
NO_NO_NO_NO_NO_NO_NO_NO_NO

NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO
YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES
YES_YES_YES
YES_NO
YES_YES_YES_YES
YES_NO
YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_NO
YES
NO_NO_YES_YES_YES_YES_YES_YES_YES_YES
YES
NO
NO
YES
NO_NO_NO
YES_YES_NO_NO_NO_YES_YES_NO_NO_NO_YES_YES_NO_NO_NO_YES_YES_NO_NO_NO
NO_NO_YES_YES_YES_NO
NO_YES_NO_NO
NO_YES_NO_YES_NO_YES_YES_YES_YES_YES
79_1_1
6_1_2_2_1
7_1_3_2_1_3_2_4_4
8_1_3_2_6_3_5_4_7_5_4_6_1_7_2
501_1_1
9_1_3_2_2_3_1_4_4_5_5
1_1_1
2_1_1_2_2
1_1_2_2_1
0_1_1_2_2
2_1_1_2_2
3_1_1_2_3_3_2
10_1_8_2_5_3_10_4_1_5_3_6_7_7_6_8_9_9_4_10_2
0_1_1
2_1_1
2_1_1
9_1_5_2_6_3_1_4_2_5_3_6_4_7_7_8_9_9_8_10_10
6_1_2_2_6_3_3_4_5_5_10_6_1_7_4_8_7_9_8_10_9
0_1_10_2_9_3_3_4_8_5_1_6_7_7_2_8_4_9_5_10_6
51_1_30_2_10_3_17_4_20_5_26_6_9_7_15_8_22_9_8_10_21_11_7_12_13_13_6_14_24_15_18_16_12_17_29_18_11_19_3_20_2_21_1_22_16_23_27_24_14_25_25_26_19_27_5_28_23_29_4_30_28
51_1_3_2_1_3_2_4_8_5_11_6_4_7_5_8_6_9_10_10_12_11_13_12_14_13_15_14_16_15_19_16_20_17_7_18_9_19_27_20_29_21_32_22_21_23_35_24_22_25_17_26_23_27_24_28_38_29_18_30_36_31_25_32_37_33_26_34_28_35_39_36_30_37_31_38_44_39_33_40_34_41_42_42_45_43_46_44_40_45_41_46_43_47_51_48_48_49_49_50_50_51_47
6_1_8_2_6_3_1_4_3_5_2_6_7_7_5_8_4_9_9_10_10
13_1_1_2_2_3_5_4_4_5_3
9_1_1_2_5_3_7_4_6_5_8_6_2_7_3_8_4
12_1_6_2_1_3_3_4_5_5_2_6_4
61_1_1_2_2
3_1_8_2_2_3_9_4_12_5_1_6_5_7_7_8_4_9_6_10_10_11_3_12_13_13_11
0
0_1_1
5_1_1
0_1_1
0_1_1
1_1_1
4_1_2_2_1_3_3
11_1_1_2_2_3_3_4_4
17_1_8_2_10_3_5_4_7_5_6_6_4_7_2_8_9_9_3_10_1
11_1_3_2_5_3_4_4_1_5_2
*/

using namespace std; 

int main( int argc, char *argv[]){
    
    // Test Cases for count_scores() -> 30 * 1 = 30
    if( atoi( argv[1]) == 0){
        cout << "Gradescope working properly - should be always correct, please ignore" << endl;
    }
    else if( atoi( argv[1]) == 1){ // YES_NO_NO
        cout << count_scores(2, 3, "aaaaa_acacaca", "aabaa_ccacacc_caaac") << endl;
    }
    else if( atoi( argv[1]) == 2){
        cout << count_scores(1, 5, "acbacbacb", "cbacbacb_acbacbac_aacbacbacb_acbacbacbb_acbaabacb") << endl;
    }  
    else if( atoi( argv[1]) == 3){
        cout << count_scores(0, 0, "", "") << endl;
    }  
    else if( atoi( argv[1]) == 4){
        cout << count_scores(5, 4, "ab_cacab_cbabc_acc_cacab", "abc_aa_acbca_cb") << endl;
    } 
    else if( atoi( argv[1]) == 5){

        cout << count_scores(9, 9, "caccbcacabccba_aacbcbcaabacbcbcba_babccaaacccacbb_caaabcaacbababbabbb_abbaccacabacaaaa_bccbccababcaacb_caacbcaacbababbabbb_bcacababbbcaaca_ccbbcbababbccaab", "bbcbccababcaacb_aacccbabbacbabacaca_bbcbcccbabcaacb_acbacacbcacc_caaabcaaabacabbabbb_abbbabaaaba_aacccbcaabacbcbcba_abbaccacabbcaaaa_aaccbbcabbacbcbcba") << endl;
    }
    else if( atoi( argv[1]) == 6){
        cout << count_scores(0, 9, "", "caccbcacabccba_aacbcbcaabacbcbcba_babccaaacccacbb_caaabcaacbababbabbb_abbaccacabacaaaa_bccbccababcaacb_caacbcaacbababbabbb_bcacababbbcaaca_ccbbcbababbccaab") << endl;
    }
    else if( atoi( argv[1]) == 7){
        cout << count_scores(9, 0, "caccbcacabccba_aacbcbcaabacbcbcba_babccaaacccacbb_caaabcaacbababbabbb_abbaccacabacaaaa_bccbccababcaacb_caacbcaacbababbabbb_bcacababbbcaaca_ccbbcbababbccaab", "") << endl;
    }  
    else if( atoi( argv[1]) == 8){
        cout << count_scores(200, 200, "bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac", "bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac") << endl;
    }  
    else if( atoi( argv[1]) == 9){
        cout << count_scores(200, 200, "bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac", "bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc") << endl;
    }  
    else if( atoi( argv[1]) == 10){
        cout << count_scores(2, 3, "a_c", "b_c_a") << endl;
    }  
    else if( atoi( argv[1]) == 11){
        cout << count_scores(3, 2, "a_b_c", "a_bb") << endl;
    }  
    else if( atoi( argv[1]) == 12){
        cout << count_scores(3, 4, "aa_bb", "ac_cb_ab_ba") << endl;
    }  
    else if( atoi( argv[1]) == 13){
        cout << count_scores(2, 3, "aabc_ca", "aacc_bb") << endl;
    }  
    else if( atoi( argv[1]) == 14){
        cout << count_scores(14, 14, "abc_bca_cab_aab_aba_baa_aca_caa_bcc_aaa_bbb_ccc_abb_abbcb", "abc_bca_cab_aab_aba_baa_aca_caa_bcc_aaa_bbb_ccc_abb_abbcb") << endl;
    }  
    else if( atoi( argv[1]) == 15){
        cout << count_scores(1, 1, "ccaaaabacbbaaacbcaccbaabaabcaacbbbaabcabbbcabcbbacccabaabcbbcbbbbbbcbacaaabcccacaacbbbbaaccabcbcaaacbabbbbcaabaaabaabaabaccbbcaacccabcacaaabacccccaacbbccbcbcbccaacbabbccbccabbcabacbacccbaababacabababbaabaabccccbcbaabababbccbcaacaacaaabbaccababcabacaaccbbbacbccacacbbbacccccbabcbaacbabaabcabaacbcaacacacbabcacbabaabbcccaccacbccbacccacbbaacaaacaacabcacccccaaaccbcbbcaaabbcbcbacabcaccabbabccccaccccabbababbccacccaacccacbbacbccbbacccbcbbcbacaaacaacbbaabacacacaabcaacbbbbacbccccccbbacaabaccacbaccccaacacbcacbbab", "ccaaaabacbbaaacbcaccbaabaabcaacbbbaabcabbbcabcbbacccabaabcbbcbbbbbbcbacaaabcccacaacbbbbaaccabcbcaaacbabbbbcaabaaabaabaabaccbbcaacccabcacaaabacccccaacbbccbcbcbccaacbabbccbccabbcabacbacccbaababacabababbaabaabccccbcbaabababbccbcaacaacaaabbaccababcabacaaccbbbacbccacacbbbacccccbabcbaacbabaabcabaacbcaacacacbabcacbabaabbcccaccacbccbacccacbbaacaaacaacabcacccccaaaccbcbbcaaabbcbcbacabcaccabbabccccaccccabbababbccacccaacccacbbacbccbbacccbcbbcbacaaacaacbbaabacacacaabcaacbbbbacbccccccbbacaabaccacbaccccaacacbcacbbac") << endl;
    }  
    else if( atoi( argv[1]) == 16){
        cout << count_scores(1, 10, "ab", "cc_abc_aa_aa_aa_aa_aa_aa_aa_aa") << endl;
    }  
    else if( atoi( argv[1]) == 17){
        cout << count_scores(10, 1, "cc_abc_aa_aa_aa_aa_aa_aa_aa_aa", "ab") << endl;
    }  
    else if( atoi( argv[1]) == 18){
        cout << count_scores(1, 1, "c", "ccccccccccc") << endl;
    }  
    else if( atoi( argv[1]) == 19){
        cout << count_scores(1, 1, "bbbbbbbaaaabbbbbaabbbba", "aaabbbabbbbbbbaabbabbbb") << endl;
    }  
    else if( atoi( argv[1]) == 20){
        cout << count_scores(1, 1, "bbbbbbbaaaabbbbbaabbbba", "bbbbbbbaaaabbbbbaabbbbb") << endl;
    }
    else if( atoi( argv[1]) == 21){
        cout << count_scores(3, 3, "abc_abb_a", "ab_ab_ab") << endl;
    }  
    else if( atoi( argv[1]) == 22){
        cout << count_scores(10, 20, "a_b_c_bb_aa_cc_abc_bac_ccc_acc", "ca_bbc_aaa_bbb_caa_baa_acb_aaa_bbb_caa_ca_bbc_aaa_bbb_caa_baa_acb_aaa_bbb_caa") << endl;
    }  
    else if( atoi( argv[1]) == 23){
        cout << count_scores(1, 6, "aaaaaaaaaaaaa", "aaaaaaaaaaaaa_bbbbbbbbbbbbb_caaaaaaaaaaaa_aaaaaaaaaaaac_aaaaaaabaaaaa_baaaaaaaaaaca") << endl;
    }  
    else if( atoi( argv[1]) == 24){
        cout << count_scores(2, 4, "abc_acb", "acb_aba_aaa_ac") << endl;
    }
    else if( atoi( argv[1]) == 25){
        cout << count_scores(2, 2, "ab_bc", "ab_aa_ab_ac_bc_ba_bb_aa_cc_ac") << endl;
    }
    // rename_people() -> 30 * 2 + 2 * 5 = 10
    else if( atoi( argv[1]) == 26){
        cout << rename_people(1, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") << endl;
    }  
    else if( atoi( argv[1]) == 27){
        cout << rename_people(2, "aaaa_aaa", "aa_aaaa") << endl;
    }
    else if( atoi( argv[1]) == 28){
        cout << rename_people(4, "aaa_bba_ccb_dcss", "bba_ccb_acc_caa") << endl;
    }  
    else if( atoi( argv[1]) == 29){
        cout << rename_people(7, "a_cc_aaa_bb_bca_acb_aa", "aba_aac_hhd_bcd_aad_ooa_bab") << endl;
    }  
    else if( atoi( argv[1]) == 30){
        cout << rename_people(1, "baababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaababbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbabaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaababbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbabaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaababbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabba", "baababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaababbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbabaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaababbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbabaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaababbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabcabba") << endl;
    }
    else if( atoi( argv[1]) == 31){
        cout << rename_people(5, "geeennady_galya_bdris_bal_toshik", "bbbilbo_torin_geneealf_smaug_toshikaaadnjn") << endl;
    }
    else if( atoi( argv[1]) == 32){
        cout << rename_people(1, "a", "a") << endl;
    }
    else if( atoi( argv[1]) == 33){
        cout << rename_people(2, "a_a", "a_a") << endl;
    }  
    else if( atoi( argv[1]) == 34){
        cout << rename_people(2, "a_b", "a_a") << endl;
    }
    else if( atoi( argv[1]) == 35){
        cout << rename_people(2, "b_b", "a_a") << endl;
    }
    else if( atoi( argv[1]) == 36){
        cout << rename_people(2, "a_b", "a_b") << endl;
    }  
    else if( atoi( argv[1]) == 37){
        cout << rename_people(3, "a_b_c", "a_c_b") << endl;
    }
    else if( atoi( argv[1]) == 38){
        cout << rename_people(10, "abaabbaaa_acccccaacabc_acbaabaaabbca_aaccca_cbbba_aaba_acab_ac_cbac_ca", "bbbbc_bacbcbcaac_c_cba_a_abba_bcabc_abcccaa_ab_a") << endl;
    }  
    else if( atoi( argv[1]) == 39){
        cout << rename_people(1, "zzzz", "yyx") << endl;
    } 
    else if( atoi( argv[1]) == 40){
        cout << rename_people(1, "aa", "aaa") << endl;
    } 
    else if( atoi( argv[1]) == 41){
        cout << rename_people(1, "aaa", "aa") << endl;
    } 
    else if( atoi( argv[1]) == 42){
        cout << rename_people(10, "b_b_a_a_a_a_b_b_a_b", "b_a_a_a_b_b_b_a_b_b") << endl;
    } 
    else if( atoi( argv[1]) == 43){
        cout << rename_people(10, "a_b_a_a_c_a_a_a_a_a", "b_c_c_a_c_b_a_a_a_c") << endl;
    } 
    else if( atoi( argv[1]) == 44){
        cout << rename_people(10, "w_r_a_c_x_e_b_x_w_x", "z_g_d_y_s_y_j_h_l_u") << endl;
    } 
    else if( atoi( argv[1]) == 45){
        cout << rename_people(30, "cb_ac_ac_bb_a_ccbbb_cb_bccaba_bca_a_ccbbbbcac_a_cba_b_aa_cca_bc_ac_acc_babc_caaa_bca_bacaaaaabcacb_c_caa_cb_bac_cc_baa_cc", "caacc_babbcbcbbc_acaa_bb_bbabaacb_cbaaac_cc_bcbccaac_ccc_ab_acaba_ccab_ab_a_c_bcabcab_ac_aaac_cb_bbcbbccb_ab_bccc_cabb_a_cac_abcbc_bb_cab_bc_cacccccc") << endl;
    } 
    else if( atoi( argv[1]) == 46){
        cout << rename_people(51, "a_c_c_c_b_a_a_a_c_c_c_c_c_b_c_c_a_a_a_a_a_c_a_c_b_c_c_c_b_a_b_a_b_b_a_b_b_c_b_b_b_c_c_a_a_a_c_a_a_a_b", "c_c_a_a_a_a_a_c_a_c_b_c_c_c_c_b_b_b_c_c_c_c_c_c_b_b_a_b_a_b_b_a_b_b_a_a_a_c_a_a_a_b_a_c_c_c_b_a_a_a_c") << endl;
    } 
    else if( atoi( argv[1]) == 47){
        cout << rename_people(10, "we_i_o_d_jt_wh_l_k_v_b", "w_v_c_km_wa_mh_wee_wei_vo_bb") << endl;
    } 
    else if( atoi( argv[1]) == 48){
        cout << rename_people(5, "aa_aca_avvs_abb_abca", "aaaa_acxa_abcaa_avas_avvs") << endl;
    } 
    else if( atoi( argv[1]) == 49){
        cout << rename_people(8, "aa_acc_abb_aba_bac_bcc_ca_ac", "aaa_bbb_ccc_a_b_c_ab_ba") << endl;
    }  
    else if( atoi( argv[1]) == 50){
        cout << rename_people(6, "aaaaaa_aa_a_ab_abab_abaab", "aaa_aaaaa_a_aaa_aaaaaaaa_aaaaaaaaaa") << endl;
    } 
    else if( atoi( argv[1]) == 51){
        cout << rename_people(2, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_xxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_xxxxxx") << endl;
    } 
    else if( atoi( argv[1]) == 52){
        cout << rename_people(13, "q_r_c_r_j_g_j_k_z_u_w_u_e", "g_n_y_h_g_z_f_l_a_p_b_r_p") << endl;
    } 
    else if( atoi( argv[1]) == 53){
        cout << rename_people(0, "", "") << endl;
    } 
    else if( atoi( argv[1]) == 54){
        cout << rename_people(1, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "abcde") << endl;
    } 
    else if( atoi( argv[1]) == 55){
        cout << rename_people(1, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxx") << endl;
    } 
    else if( atoi( argv[1]) == 56){
        cout << rename_people(1, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "") << endl;
    } 
    else if( atoi( argv[1]) == 57){
        cout << rename_people(1, "x", "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") << endl;
    } 
    else if( atoi( argv[1]) == 58){
        cout << rename_people(1, "x", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") << endl;
    } 
    else if( atoi( argv[1]) == 59){
        cout << rename_people(3, "yyyyy_acccs_asdnj", "skd_yyyyaccc_dsdjksnj") << endl;
    } 
     else if( atoi( argv[1]) == 60){
        cout << rename_people(4, "hda_sdn_sndm_sfmn", "hdands_sdnmsdn_snsfdm_sfmdmsn") << endl;
    } 
    else if( atoi( argv[1]) == 61){
        cout << rename_people(10, "baa_a_ba_aabab_aa_baab_bb_abbbb_a_a", "a_ba_ba_baabbb_ba_a_aabb_baa_ab_b") << endl;
    } 
    else if( atoi( argv[1]) == 62){
        cout << rename_people(5, "gennady_galya_boris_bill_toshik", "bilbo_torin_gendalf_smaug_galadriel") << endl;
    }

    return 0; 
}
