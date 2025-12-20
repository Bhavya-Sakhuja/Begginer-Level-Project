import qrcode
from PIL import ImageShow

upi = input('Enter UPI Id: ')

# upi://pay?pa=upi_id&pn=name&am=Amount&cu=Currency&tn=message

phonepay_url = f"upi://pay?pa={upi}&pn=Recepient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi}&pn=Recepient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi}&pn=Recepient%20Name&mc=1234"

# Create QR Codes 

phonepay_qr = qrcode.make(phonepay_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# save the qr code to image file 
# phonepay_qr.save('phonepay_qr.png')
# paytm_qr.save('paytm_qr.png')
# google_pay_qr.save('google_pay_qr.png')

phonepay_qr.show()
paytm_qr.show()
google_pay_qr.show()