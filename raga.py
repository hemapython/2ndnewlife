photo=open("pancard.jpg","rb")
click=open("myphoto.jpg","wb")
for no in photo:
    click.write(no)