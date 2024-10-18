
import pandas as pd

data = pd.read_csv('titanic.csv')



over18 = data.loc[data["Age"]>18,"Name"]
print(over18)

maleNames=data.loc[data['Sex']=="male","Name"]
print(maleNames)



section=data.iloc[12:25,0:2]
print(section)

section1=data.iloc[18:19,1:2]
print(section1)


data.iloc[18:19,1:2]=1

section2=data.iloc[18:19,1:2]
print(section2)

data.to_csv('change.csv')



data["40y"]=data["Age"]+40
data.to_csv('change2.csv')



data["FareAge"]=data["Fare"]/data["Age"]
data.to_csv('change3.csv')



data_rename=data.rename(
    columns={"Pclass":"Passenger Class","Parents/Children Aboard":"Family Aboard"}
)
print(data_rename)



print(data["FareAge"].mean()) #mean -> medium

print(data["Age"].min()) #min -> minumn

print(data["Fare"].max()) #max

#multiple
print(data[["Age","Fare"]].max())


print(data.agg({
    "Age":['min','max','mean','std','median'],
    "Fare":['sum','mean','median','std']
}))



print(data[["Sex","Age"]].groupby("Sex").mean())

print(data[["Pclass","Age"]].groupby("Pclass").mean())



x=data.sort_values(by="Pclass",ascending=True)
print(x.head()) 



#homework
#meanFare_sex_pclass = data.groupby(["Sex", "Pclass"])["Fare"].mean()
#print(meanFare_sex_pclass)



data["NameLowerCase"]=data["Name"].str.lower()
print(data["NameLowerCase"])

data["NameUpperCase"]=data["Name"].str.upper()
print(data["NameUpperCase"])

data["NameCapsCase"]=data["Name"].str.capitalize()
print(data["NameCapsCase"])


data["NameStripCase"]=data["Name"].str.strip() #remove extra spaces between words(leading/trailing)
print(data["NameStripCase"])

# strip can be

#  lstrip() ->  leading

#  rstrip() ->  trailing


x="Mr. Owen Banks"

name=x.split(" ")

print(x.split(" "))

print(name[2])



data["TitleName"] = data["Name"].str.split(" ").str.get(0)
print(data["TitleName"])



data["Sex"]=data["Sex"].replace({"male":"M","female":"F"})
print(data["Sex"])



data["Survived"]=data["Survived"].replace({0:"Survived",1:"Not Survived"})
print(data["Survived"])



data["SurName"] = data["Name"].str.split(" ").str.get(2)

data["ShortName"]=data["TitleName"]+data["SurName"]
print(data["ShortName"])



data["NumTitle"]=data["TitleName"].replace({"Mr.":0,"Mrs.":1,"Miss.":2,"Master.":4})
print(data["NumTitle"])







