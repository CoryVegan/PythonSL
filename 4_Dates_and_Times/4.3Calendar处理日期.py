# -*- coding: utf-8 -*-	
#calendar 模块定义了Calendar类，其中封装了一些值的计算，如给定的一个月或一年中的周几。另外，TextCalendar和HTMLCalendar类可以生成经过预格式化的输出。

#4.3.1格式化示例
#prmonth()方法是一个简单的函数，可以生成一个月的格式化文本输出
import calendar
c = calendar.TextCalendar(calendar.SUNDAY)#一周从周日开始，默认会使用欧洲惯例，一周从星期一开始
c.prmonth(2011, 7)

import pprint
cal = calendar.Calendar(calendar.SUNDAY)

cal_data = cal.yeardays2calendar(2011, 3)
print 'len(cal_data)   :', len(cal_data)

top_months = cal_data[0]
print 'len(top_months) :', len(top_months)

first_month = top_months[0]
print 'len(first_month):', len(first_month)

print 'first_month:'
pprint.pprint(first_month)
#调用yeardays2calendar(2011, 3)会返回2011年的数据，按每栏3个月组织，这等价于formatyear()使用的数据
cal = calendar.TextCalendar(calendar.SUNDAY)
print cal.formatyear(2011, 2, 1, 1, 3)

#4.3.2计算日期
pprint.pprint(calendar.monthcalendar(2011, 7))
print
#要计算2011年的会议日期，假设是每个月的第二个星期四，0值指示第一周的星期四是否包含在这个月内
for month in xrange(1, 13):
    # Compute the dates for each week that overlaps the month
    c = calendar.monthcalendar(2013, month)
    first_week = c[0]
    second_week=c[1]
    third_week = c[2]
    if first_week[calendar.THURSDAY]:
        meeting_date = second_week[calendar.THURSDAY]
    else:
        meeting_date = third_week[calendar.THURSDAY]
    
    print '%3s: %2s' % (calendar.month_abbr[month], meeting_date)
