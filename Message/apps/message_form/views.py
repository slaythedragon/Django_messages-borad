from django.shortcuts import render

from apps.message_form.models import Message
# 默认接受一个参数request，是Django传递进来的，每一个请求都会包装成一个request对象
def message_form(request):
    # # 1.使用all()
    # # all()取出所有数据,返回QuerySet对象，允许进行多种操作
    # # 从索引0开始取，直到索引1为止，但不包括索引1
    # all_messages = Message.objects.all()
    # sliced_query = Message.objects.all()[:1]
    # print(all_messages)
    # # 输出：<QuerySet [<Message: Message object (bobby)>]>
    #
    # # 用.query方法来打印sql语句
    # print(all_messages.query)
    # # 输出：SELECT message.name, message.email, message.address, message.message FROM message
    # print(sliced_query.query)
    # # 输出：SELECT message.name, message.email, message.address, message.message FROM message  LIMIT 1


    # # 2.使用filter
    # all_messages = Message.objects.filter(name="bobby")
    # print(all_messages.query)
    # # QuerySet类型可以进行for操作，遍历取出来的所有数据
    # for message in all_messages:
    #     print(message.name)
    # 3.使用get
    # message = Message.objects.get(name="bobby")
    # print(message.name)
    # # 输出：bobby

    # # name="bobby1"不存在或者有多个时候会抛出异常
    # try:
    #     message = Message.objects.get(name="bobby1")
    #
    # # 不存在的异常
    # except Message.DoesNotExist as e:
    #     print(e)
    #     # 输出异常Message matching query does not exist.
    #
    # # 存在多个的异常
    # except Message.MultipleObjectsReturned as e:
    #     print(e)
    # all_messages = Message.objects.filter(name="bobby")
    # all_messages.delete()

    # 进行数据的插入操作
    # # 实例化一个Message对象
    # message = Message()
    # message.name = "bobby"
    # message.email = "bobby@imooc.com"
    # message.address = "北京市"
    # message.message = "留言"
    # # 使用save方法将数据保存到数据库中
    # message.save()

    # 从html中提取数据保存到数据库中
    # 如果是POST，进行取数据
    if request.method == "POST":
        # 进行值的提取
        # POS属性调用get方法，可理解为dict字典所有用get方法,""代表值不存在的话设置默认值
        name = request.POST.get("name","")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        message_text = request.POST.get("message", "")

        message = Message()
        # 和上面对应
        message.name = name
        message.email = email
        message.address = address
        message.message = message_text
        message.save()
        return render(request,"message_form.html", {
                "message":message
            })

    # 从服务器中提取出数据展示到html页面
    if request.method == "GET":
        var_dict = {}
        # 这里取数据使用filter方法，如果没有数据会返回一个空的list
        all_message = Message.objects.filter()
        if all_message:# 判断是否有数据，若没有数据取第0个会报错
            message = all_message[0]# 取第0个时会直接转为message对象而不是原来的QuerySet
            # 将views中的数据传到html页面中，传入一个字典{}，键值对的名称可以任意写，值需要为message
            var_dict = {
                "message":message
            }
            return render(request,"message_form.html", var_dict)
            # 或者可以直接写为：locals(),可以将所有的局部变量全部变成key-value的形式，但此习惯不好
            # return render(request, "message_form.html", locals())
        else:# 若没有数据直接返回页面，不然会抛异常
            return render(request, "message_form.html")
