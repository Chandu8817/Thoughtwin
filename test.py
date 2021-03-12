# import csv

# with open('demodata.csv', mode='r') as csv_file:

#     csv_read= csv.reader(csv_file)

#     for row in csv_read:
#         print(row)




def updateprofilepic(request):
    context={}
    profiledetial = UserPorfilePic.objects.get(user=request.user)

    user_form = ExtendedUser(request.POST)
    upd_profile=UserPorfilePic.objects.get(user=request.user)
    update_form=ProfilePicForm(request.POST,request.FILES , instance=upd_profile)
    
    if update_form.is_valid():
        user=user_form.save()
        updprofile = update_form.save(commit=False)
        updprofile.user = user
        updprofile.save()



        # update_form.save() 
        return HttpResponseRedirect(reverse('home'))
    
    context['update_form']=updprofile
    
    return render(request,'account/result.html',context)
































# with open('demodata.txt', mode='r') as csv_file:

#     csv_read = csv.DictReader(csv_file,delimiter=',')
#     line_count=0
#     for row in csv_read:
#         if line_count ==0:
#             print(','.join(row))
#             line_count += 1
       
#         print(row['name'],row['department'],row['birthday month'])
#         line_count += 1
#     print(line_count)

# with open('demodata.txt') as csv_file:

#     csv_reader= csv.reader(csv_file, delimiter=',')

#     line_count=0

#     for row in csv_reader:

#         if line_count==0:
#             print(f'colunm names are {",".join(row)}')

#             line_count += 1

#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')





