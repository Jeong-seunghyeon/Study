import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


plt.figure(figsize=(10,6))

# font_name=fm.FontProperties(fname="Analysis/font\H2MJRE.TTF").get_name()
# plt.rc("font",family=font_name)#글꼴 설정
# plt.rcParams['axes.unicode_minus'] = False

plt.title("hist:히스토그램 그리기; plt..hist(__list__)", fontsize=14, color='#FF00FF', fontweight='bold')

weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
          80, 59, 67, 81, 69, 73, 69, 74, 70, 65]

plt.hist(weight, rwidth=0.8, bins=8)

plt.show()

