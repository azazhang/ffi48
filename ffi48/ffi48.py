def ffi48(sic_code):
    if sic_code is None:
        return {"FFI48": None, "FFI48_desc": None}
    
    if 100 <= sic_code <= 199 or 200 <= sic_code <= 299 or 700 <= sic_code <= 799 or 910 <= sic_code <= 919 or sic_code == 2048:
        return {"FFI48": 1, "FFI48_desc": "Agric"}
    elif 2000 <= sic_code <= 2009 or 2010 <= sic_code <= 2019 or 2020 <= sic_code <= 2029 or 2030 <= sic_code <= 2039 or 2040 <= sic_code <= 2046 or 2050 <= sic_code <= 2059 or 2060 <= sic_code <= 2063 or 2070 <= sic_code <= 2079 or 2090 <= sic_code <= 2092 or sic_code == 2095 or 2098 <= sic_code <= 2099:
        return {"FFI48": 2, "FFI48_desc": "Food"}
    elif 2064 <= sic_code <= 2068 or sic_code == 2086 or sic_code == 2087 or sic_code == 2096 or sic_code == 2097:
        return {"FFI48": 3, "FFI48_desc": "Soda"}
    elif sic_code == 2080 or sic_code == 2082 or sic_code == 2083 or sic_code == 2084 or sic_code == 2085:
        return {"FFI48": 4, "FFI48_desc": "Beer"}
    elif 2100 <= sic_code <= 2199:
        return {"FFI48": 5, "FFI48_desc": "Smoke"}
    elif 920 <= sic_code <= 999 or 3650 <= sic_code <= 3651 or sic_code == 3652 or sic_code == 3732 or 3930 <= sic_code <= 3931 or 3940 <= sic_code <= 3949:
        return {"FFI48": 6, "FFI48_desc": "Toys"}
    elif 7800 <= sic_code <= 7829 or 7830 <= sic_code <= 7833 or 7840 <= sic_code <= 7841 or sic_code == 7900 or 7910 <= sic_code <= 7911 or 7920 <= sic_code <= 7929 or 7930 <= sic_code <= 7933 or 7940 <= sic_code <= 7949 or sic_code == 7980 or 7990 <= sic_code <= 7999:
        return {"FFI48": 7, "FFI48_desc": "Fun"}
    elif 2700 <= sic_code <= 2709 or 2710 <= sic_code <= 2719 or 2720 <= sic_code <= 2729 or 2730 <= sic_code <= 2739 or 2740 <= sic_code <= 2749 or 2770 <= sic_code <= 2771 or 2780 <= sic_code <= 2789 or 2790 <= sic_code <= 2799:
        return {"FFI48": 8, "FFI48_desc": "Books"}
    elif sic_code == 2047 or 2391 <= sic_code <= 2392 or 2510 <= sic_code <= 2519 or 2590 <= sic_code <= 2599 or 2840 <= sic_code <= 2843 or sic_code == 2844 or 3160 <= sic_code <= 3161 or 3170 <= sic_code <= 3171 or sic_code == 3172 or 3190 <= sic_code <= 3199 or sic_code == 3229 or sic_code == 3260 or 3262 <= sic_code <= 3263 or sic_code == 3269 or 3230 <= sic_code <= 3231 or 3630 <= sic_code <= 3639 or 3750 <= sic_code <= 3751 or sic_code == 3800 or 3860 <= sic_code <= 3861 or 3870 <= sic_code <= 3873 or 3910 <= sic_code <= 3911 or sic_code == 3914 or sic_code == 3915 or 3960 <= sic_code <= 3962 or sic_code == 3991 or sic_code == 3995:
        return {"FFI48": 9, "FFI48_desc": "Hshld"}
    elif 2300 <= sic_code <= 2390 or 3020 <= sic_code <= 3021 or 3100 <= sic_code <= 3111 or sic_code == 3130 or 3140 <= sic_code <= 3149 or sic_code == 3150 or 3963 <= sic_code <= 3965:
        return {"FFI48": 10, "FFI48_desc": "Clths"}
    elif 8000 <= sic_code <= 8099:
        return {"FFI48": 11, "FFI48_desc": "Hlth"}
    elif sic_code == 3693 or 3840 <= sic_code <= 3849 or sic_code == 3850:
        return {"FFI48": 12, "FFI48_desc": "MedEq"}
    elif 2830 <= sic_code <= 2831 or sic_code == 2833 or sic_code == 2834 or sic_code == 2835 or sic_code == 2836:
        return {"FFI48": 13, "FFI48_desc": "Drugs"}
    elif 2800 <= sic_code <= 2809 or 2810 <= sic_code <= 2819 or 2820 <= sic_code <= 2829 or 2850 <= sic_code <= 2859 or 2860 <= sic_code <= 2869 or 2870 <= sic_code <= 2879 or 2890 <= sic_code <= 2899:
        return {"FFI48": 14, "FFI48_desc": "Chems"}
    elif sic_code == 3031 or sic_code == 3041 or 3050 <= sic_code <= 3053 or 3060 <= sic_code <= 3069 or 3070 <= sic_code <= 3079 or 3080 <= sic_code <= 3089 or 3090 <= sic_code <= 3099:
        return {"FFI48": 15, "FFI48_desc": "Rubbr"}
    elif 2200 <= sic_code <= 2269 or 2270 <= sic_code <= 2279 or 2280 <= sic_code <= 2284 or 2290 <= sic_code <= 2295 or sic_code == 2297 or sic_code == 2298 or sic_code == 2299 or 2393 <= sic_code <= 2395 or 2397 <= sic_code <= 2399:
        return {"FFI48": 16, "FFI48_desc": "Txtls"}
    elif 800 <= sic_code <= 899 or 2400 <= sic_code <= 2439 or 2450 <= sic_code <= 2459 or 2490 <= sic_code <= 2499 or sic_code == 2660 or sic_code == 2950 or sic_code == 3200 or 3210 <= sic_code <= 3211 or 3240 <= sic_code <= 3241 or 3250 <= sic_code <= 3259 or sic_code == 3261 or sic_code == 3264 or 3270 <= sic_code <= 3275 or 3280 <= sic_code <= 3281 or 3290 <= sic_code <= 3293 or 3295 <= sic_code <= 3299 or 3420 <= sic_code <= 3429 or 3430 <= sic_code <= 3433 or sic_code == 3440 or sic_code == 3442 or sic_code == 3446 or sic_code == 3448 or sic_code == 3449 or sic_code == 3450 or sic_code == 3452 or 3490 <= sic_code <= 3499 or sic_code == 3996:
        return {"FFI48": 17, "FFI48_desc": "BldMt"}
    elif 1500 <= sic_code <= 1511 or 1520 <= sic_code <= 1529 or 1530 <= sic_code <= 1539 or 1540 <= sic_code <= 1549 or 1600 <= sic_code <= 1699 or 1700 <= sic_code <= 1799:
        return {"FFI48": 18, "FFI48_desc": "Cnstr"}
    elif sic_code == 3300 or 3310 <= sic_code <= 3317 or 3320 <= sic_code <= 3325 or 3330 <= sic_code <= 3339 or sic_code == 3340 or 3350 <= sic_code <= 3357 or 3360 <= sic_code <= 3369 or 3370 <= sic_code <= 3379 or 3390 <= sic_code <= 3399:
        return {"FFI48": 19, "FFI48_desc": "Steel"}
    elif sic_code == 3400 or sic_code == 3443 or sic_code == 3444 or 3460 <= sic_code <= 3469 or 3470 <= sic_code <= 3479:
        return {"FFI48": 20, "FFI48_desc": "FabPr"}
    elif 3510 <= sic_code <= 3519 or 3520 <= sic_code <= 3529 or sic_code == 3530 or sic_code == 3531 or sic_code == 3532 or sic_code == 3533 or sic_code == 3534 or sic_code == 3535 or sic_code == 3536 or sic_code == 3538 or 3540 <= sic_code <= 3549 or 3550 <= sic_code <= 3559 or 3560 <= sic_code <= 3569 or sic_code == 3580 or sic_code == 3581 or sic_code == 3582 or sic_code == 3585 or sic_code == 3586 or sic_code == 3589 or 3590 <= sic_code <= 3599:
        return {"FFI48": 21, "FFI48_desc": "Mach"}
    elif sic_code == 3600 or 3610 <= sic_code <= 3613 or sic_code == 3620 or sic_code == 3621 or 3623 <= sic_code <= 3629 or 3640 <= sic_code <= 3644 or sic_code == 3645 or sic_code == 3646 or 3648 <= sic_code <= 3649 or sic_code == 3660 or sic_code == 3690 or sic_code == 3691 or sic_code == 3692 or sic_code == 3699:
        return {"FFI48": 22, "FFI48_desc": "ElcEq"}
    elif sic_code == 2296 or sic_code == 2396 or 3010 <= sic_code <= 3011 or sic_code == 3537 or sic_code == 3647 or sic_code == 3694 or sic_code == 3700 or sic_code == 3710 or sic_code == 3711 or sic_code == 3713 or sic_code == 3714 or sic_code == 3715 or sic_code == 3716 or sic_code == 3792 or 3790 <= sic_code <= 3791 or sic_code == 3799:
        return {"FFI48": 23, "FFI48_desc": "Autos"}
    elif sic_code == 3720 or sic_code == 3721 or 3723 <= sic_code <= 3724 or sic_code == 3725 or 3728 <= sic_code <= 3729:
        return {"FFI48": 24, "FFI48_desc": "Aero"}
    elif sic_code == 3730 or 3740 <= sic_code <= 3743:
        return {"FFI48": 25, "FFI48_desc": "Ships"}
    elif 3760 <= sic_code <= 3769 or sic_code == 3795 or 3480 <= sic_code <= 3489:
        return {"FFI48": 26, "FFI48_desc": "Guns"}
    elif 1040 <= sic_code <= 1049:
        return {"FFI48": 27, "FFI48_desc": "Gold"}
    elif 1000 <= sic_code <= 1009 or 1010 <= sic_code <= 1019 or 1020 <= sic_code <= 1029 or 1030 <= sic_code <= 1039 or 1050 <= sic_code <= 1059 or 1060 <= sic_code <= 1069 or 1070 <= sic_code <= 1079 or 1080 <= sic_code <= 1089 or 1090 <= sic_code <= 1099 or 1100 <= sic_code <= 1119 or 1400 <= sic_code <= 1499:
        return {"FFI48": 28, "FFI48_desc": "Mines"}
    elif 1200 <= sic_code <= 1299:
        return {"FFI48": 29, "FFI48_desc": "Coal"}
    elif sic_code == 1300 or 1310 <= sic_code <= 1319 or 1320 <= sic_code <= 1329 or 1330 <= sic_code <= 1339 or 1370 <= sic_code <= 1379 or sic_code == 1380 or sic_code == 1381 or sic_code == 1382 or sic_code == 1389 or 2900 <= sic_code <= 2912 or 2990 <= sic_code <= 2999:
        return {"FFI48": 30, "FFI48_desc": "Oil"}
    elif sic_code == 4900 or 4910 <= sic_code <= 4911 or 4920 <= sic_code <= 4922 or sic_code == 4923 or 4924 <= sic_code <= 4925 or 4930 <= sic_code <= 4931 or sic_code == 4932 or sic_code == 4939 or 4940 <= sic_code <= 4942:
        return {"FFI48": 31, "FFI48_desc": "Util"}
    elif sic_code == 4800 or 4810 <= sic_code <= 4813 or 4820 <= sic_code <= 4822 or 4830 <= sic_code <= 4839 or 4840 <= sic_code <= 4841 or 4880 <= sic_code <= 4889 or sic_code == 4890 or sic_code == 4891 or sic_code == 4892 or 4899 <= sic_code <= 4899:
        return {"FFI48": 32, "FFI48_desc": "Telcm"}
    elif sic_code == 7020 or 7030 <= sic_code <= 7033 or sic_code == 7200 or 7210 <= sic_code <= 7212 or sic_code == 7214 or 7215 <= sic_code <= 7216 or sic_code == 7217 or sic_code == 7219 or 7220 <= sic_code <= 7221 or sic_code == 7230 or sic_code == 7240 or sic_code == 7250 or 7260 <= sic_code <= 7269 or 7270 <= sic_code <= 7290 or sic_code == 7291 or 7292 <= sic_code <= 7299 or sic_code == 7395 or sic_code == 7500 or 7520 <= sic_code <= 7529 or 7530 <= sic_code <= 7539 or 7540 <= sic_code <= 7549 or sic_code == 7600 or sic_code == 7620 or sic_code == 7622 or sic_code == 7623 or sic_code == 7629 or sic_code == 7630 or sic_code == 7631 or sic_code == 7640 or sic_code == 7641 or 7690 <= sic_code <= 7699 or 8100 <= sic_code <= 8199 or 8200 <= sic_code <= 8299 or 8300 <= sic_code <= 8399 or 8400 <= sic_code <= 8499 or 8600 <= sic_code <= 8699 or 8800 <= sic_code <= 8899 or sic_code == 7510:
        return {"FFI48": 33, "FFI48_desc": "PerSv"}
    elif 2750 <= sic_code <= 2759 or sic_code == 3993 or sic_code == 7218 or sic_code == 7300 or 7310 <= sic_code <= 7319 or 7320 <= sic_code <= 7329 or 7330 <= sic_code <= 7339 or 7340 <= sic_code <= 7342 or sic_code == 7349 or sic_code == 7350 or sic_code == 7351 or sic_code == 7352 or sic_code == 7353 or sic_code == 7359 or 7360 <= sic_code <= 7369 or 7370 <= sic_code <= 7372 or sic_code == 7374 or sic_code == 7375 or sic_code == 7376 or sic_code == 7377 or sic_code == 7378 or sic_code == 7379 or sic_code == 7380 or 7381 <= sic_code <= 7382 or sic_code == 7383 or sic_code == 7384 or sic_code == 7385 or 7389 <= sic_code <= 7390 or sic_code == 7391 or sic_code == 7392 or sic_code == 7393 or sic_code == 7394 or sic_code == 7396 or sic_code == 7397 or sic_code == 7399 or sic_code == 7519 or sic_code == 8700 or 8710 <= sic_code <= 8713 or sic_code == 8720 or 8730 <= sic_code <= 8734 or 8740 <= sic_code <= 8748 or 8900 <= sic_code <= 8910 or sic_code == 8911 or 8920 <= sic_code <= 8999 or sic_code == 4220:
        return {"FFI48": 34, "FFI48_desc": "BusSv"}
    elif 3570 <= sic_code <= 3579 or sic_code == 3680 or sic_code == 3681 or sic_code == 3682 or sic_code == 3683 or sic_code == 3684 or sic_code == 3685 or sic_code == 3686 or sic_code == 3687 or sic_code == 3688 or sic_code == 3689 or sic_code == 3695 or sic_code == 7373:
        return {"FFI48": 35, "FFI48_desc": "Comps"}
    elif sic_code == 3622 or sic_code == 3661 or sic_code == 3662 or sic_code == 3663 or sic_code == 3664 or sic_code == 3665 or sic_code == 3666 or sic_code == 3669 or 3670 <= sic_code <= 3679 or sic_code == 3810 or sic_code == 3812:
        return {"FFI48": 36, "FFI48_desc": "Chips"}
    elif sic_code == 3811 or sic_code == 3820 or sic_code == 3821 or sic_code == 3822 or sic_code == 3823 or sic_code == 3824 or sic_code == 3825 or sic_code == 3826 or sic_code == 3827 or sic_code == 3829 or 3830 <= sic_code <= 3839:
        return {"FFI48": 37, "FFI48_desc": "LabEq"}
    elif 2520 <= sic_code <= 2549 or 2600 <= sic_code <= 2639 or 2670 <= sic_code <= 2699 or sic_code == 2760 or sic_code == 2761 or 3950 <= sic_code <= 3955:
        return {"FFI48": 38, "FFI48_desc": "Paper"}
    elif 2440 <= sic_code <= 2449 or 2640 <= sic_code <= 2659 or sic_code == 3220 or sic_code == 3221 or 3410 <= sic_code <= 3412:
        return {"FFI48": 39, "FFI48_desc": "Boxes"}
    elif 4000 <= sic_code <= 4013 or 4040 <= sic_code <= 4049 or sic_code == 4100 or 4110 <= sic_code <= 4119 or sic_code == 4120 or sic_code == 4121 or sic_code == 4130 or sic_code == 4131 or 4140 <= sic_code <= 4142 or sic_code == 4150 or sic_code == 4151 or 4170 <= sic_code <= 4173 or 4190 <= sic_code <= 4199 or sic_code == 4200 or 4210 <= sic_code <= 4219 or sic_code == 4230 or sic_code == 4231 or 4240 <= sic_code <= 4249 or 4400 <= sic_code <= 4499 or 4500 <= sic_code <= 4599 or 4600 <= sic_code <= 4699 or sic_code == 4700 or 4710 <= sic_code <= 4712 or 4720 <= sic_code <= 4729 or 4730 <= sic_code <= 4739 or 4740 <= sic_code <= 4749 or sic_code == 4780 or sic_code == 4782 or sic_code == 4783 or sic_code == 4784 or sic_code == 4785 or sic_code == 4789:
        return {"FFI48": 40, "FFI48_desc": "Trans"}
    elif sic_code == 5000 or 5010 <= sic_code <= 5015 or 5020 <= sic_code <= 5023 or 5030 <= sic_code <= 5039 or 5040 <= sic_code <= 5042 or sic_code == 5043 or sic_code == 5044 or sic_code == 5045 or sic_code == 5046 or sic_code == 5047 or sic_code == 5048 or sic_code == 5049 or 5050 <= sic_code <= 5059 or sic_code == 5060 or sic_code == 5063 or sic_code == 5064 or sic_code == 5065 or 5070 <= sic_code <= 5078 or sic_code == 5080 or sic_code == 5081 or sic_code == 5082 or sic_code == 5083 or sic_code == 5084 or sic_code == 5085 or sic_code == 5086 or sic_code == 5087 or sic_code == 5088 or sic_code == 5090 or sic_code == 5091 or sic_code == 5092 or sic_code == 5093 or sic_code == 5094 or sic_code == 5099 or sic_code == 5100 or 5110 <= sic_code <= 5113 or 5120 <= sic_code <= 5122 or 5130 <= sic_code <= 5139 or 5140 <= sic_code <= 5149 or 5150 <= sic_code <= 5159 or 5160 <= sic_code <= 5169 or 5170 <= sic_code <= 5172 or 5180 <= sic_code <= 5182 or 5190 <= sic_code <= 5199:
        return {"FFI48": 41, "FFI48_desc": "Whlsl"}
    elif sic_code == 5200 or 5210 <= sic_code <= 5219 or 5220 <= sic_code <= 5229 or sic_code == 5230 or sic_code == 5231 or sic_code == 5250 or sic_code == 5251 or sic_code == 5260 or sic_code == 5261 or sic_code == 5270 or sic_code == 5271 or sic_code == 5300 or sic_code == 5310 or sic_code == 5311 or sic_code == 5320 or sic_code == 5330 or sic_code == 5331 or sic_code == 5334 or 5340 <= sic_code <= 5349 or 5390 <= sic_code <= 5399 or sic_code == 5400 or sic_code == 5410 or sic_code == 5411 or sic_code == 5412 or 5420 <= sic_code <= 5429 or 5430 <= sic_code <= 5439 or 5440 <= sic_code <= 5449 or 5450 <= sic_code <= 5459 or 5460 <= sic_code <= 5469 or 5490 <= sic_code <= 5499 or sic_code == 5500 or 5510 <= sic_code <= 5529 or 5530 <= sic_code <= 5539 or 5540 <= sic_code <= 5549 or 5550 <= sic_code <= 5559 or 5560 <= sic_code <= 5569 or 5570 <= sic_code <= 5579 or 5590 <= sic_code <= 5599 or 5600 <= sic_code <= 5699 or sic_code == 5700 or 5710 <= sic_code <= 5719 or 5720 <= sic_code <= 5722 or 5730 <= sic_code <= 5733 or sic_code == 5734 or sic_code == 5735 or sic_code == 5736 or 5750 <= sic_code <= 5799 or sic_code == 5900 or 5910 <= sic_code <= 5912 or 5920 <= sic_code <= 5929 or 5930 <= sic_code <= 5932 or sic_code == 5940 or sic_code == 5941 or sic_code == 5942 or sic_code == 5943 or sic_code == 5944 or sic_code == 5945 or sic_code == 5946 or sic_code == 5947 or sic_code == 5948 or sic_code == 5949 or 5950 <= sic_code <= 5959 or 5960 <= sic_code <= 5969 or 5970 <= sic_code <= 5979 or 5980 <= sic_code <= 5989 or sic_code == 5990 or sic_code == 5992 or sic_code == 5993 or sic_code == 5994 or sic_code == 5995 or sic_code == 5999:
        return {"FFI48": 42, "FFI48_desc": "Rtail"}
    elif 5800 <= sic_code <= 5819 or 5820 <= sic_code <= 5829 or 5890 <= sic_code <= 5899 or sic_code == 7000 or 7010 <= sic_code <= 7019 or 7040 <= sic_code <= 7049 or sic_code == 7213:
        return {"FFI48": 43, "FFI48_desc": "Meals"}
    elif sic_code == 6000 or 6010 <= sic_code <= 6019 or sic_code == 6020 or sic_code == 6021 or sic_code == 6022 or 6023 <= sic_code <= 6024 or sic_code == 6025 or sic_code == 6026 or sic_code == 6027 or 6028 <= sic_code <= 6029 or 6030 <= sic_code <= 6036 or 6040 <= sic_code <= 6059 or 6060 <= sic_code <= 6062 or 6080 <= sic_code <= 6082 or 6090 <= sic_code <= 6099 or sic_code == 6100 or sic_code == 6110 or sic_code == 6111 or sic_code == 6112 or sic_code == 6113 or 6120 <= sic_code <= 6129 or 6130 <= sic_code <= 6139 or 6140 <= sic_code <= 6149 or 6150 <= sic_code <= 6159 or 6160 <= sic_code <= 6169 or 6170 <= sic_code <= 6179 or 6190 <= sic_code <= 6199:
        return {"FFI48": 44, "FFI48_desc": "Banks"}
    elif sic_code == 6300 or 6310 <= sic_code <= 6319 or 6320 <= sic_code <= 6329 or sic_code == 6330 or sic_code == 6331 or sic_code == 6350 or sic_code == 6351 or sic_code == 6360 or sic_code == 6361 or 6370 <= sic_code <= 6379 or 6390 <= sic_code <= 6399 or 6400 <= sic_code <= 6411:
        return {"FFI48": 45, "FFI48_desc": "Insur"}
    elif sic_code == 6500 or sic_code == 6510 or sic_code == 6512 or sic_code == 6513 or sic_code == 6514 or sic_code == 6515 or 6517 <= sic_code <= 6519 or 6520 <= sic_code <= 6529 or sic_code == 6530 or sic_code == 6531 or sic_code == 6532 or sic_code == 6540 or sic_code == 6541 or 6550 <= sic_code <= 6553 or 6590 <= sic_code <= 6599 or sic_code == 6610 or sic_code == 6611:
        return {"FFI48": 46, "FFI48_desc": "RlEst"}
    elif 6200 <= sic_code <= 6299 or sic_code == 6700 or 6710 <= sic_code <= 6719 or 6720 <= sic_code <= 6722 or sic_code == 6723 or sic_code == 6724 or sic_code == 6725 or sic_code == 6726 or 6730 <= sic_code <= 6733 or 6740 <= sic_code <= 6779 or sic_code == 6790 or sic_code == 6791 or sic_code == 6792 or sic_code == 6793 or sic_code == 6794 or sic_code == 6795 or sic_code == 6798 or sic_code == 6799:
        return {"FFI48": 47, "FFI48_desc": "Fin"}
    elif 4950 <= sic_code <= 4959 or sic_code == 4960 or sic_code == 4961 or sic_code == 4970 or sic_code == 4971 or sic_code == 4990 or sic_code == 4991:
        return {"FFI48": 48, "FFI48_desc": "Other"}
    else:
        return {"FFI48": None, "FFI48_desc": None}
