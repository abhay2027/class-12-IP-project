import pandas as pd
import matplotlib.pyplot as plt

csv1=pd.read_csv('covid19.csv')

df1=pd.DataFrame(csv1)

csv2=pd.read_csv('covid19.csv',index_col=0)

df2=pd.DataFrame(csv2)

index = 0

while True:
    
    menu = ("""
               ================================================                           
                                  Main menu
               ================================================
                            1.Data Analysis
                            2.Sort data 
                            3.Add district data into csv
                            4.Edit a record
                            5.Delete a record 
                            6.Line Graph
                            7.Bar Graph
                            8.Exit
      """)
      
    print(menu)
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        
        index += 1
        print("You chose option 1:\n",df1)
        input("Press Enter to continue...")


    elif choice == 2:
        index += 1
        
        while True:
            print("You chose option 2:")
            print("""
              1. To sort data by number of confirmed cases
              2. To sort data by number of recovered cases
              3. To sort data by number of deaths
              4. To sort data by number of active cases
              5. To go back 
              """)

            sort_choice = int(input("enter your choice: "))
            
            if sort_choice == 1:
                index += 1
                df1_sorted1 = df1.sort_values(by='Confirmed')
                print(df1_sorted1)
                input("press enter to continue...")
                pass
            
            elif sort_choice == 2:
                index += 1
                df1_sorted2 = df1.sort_values(by='Recovered')
                print(df1_sorted2)
                input("press enter to continue...")
                pass
            
            elif sort_choice == 3:
                index += 1
                df1_sorted3 = df1.sort_values(by='Deaths')
                print(df1_sorted3)
                input("press enter to continue...")
                pass
            
            elif sort_choice == 4:
                index += 1
                df1_sorted4 = df1.sort_values(by='Active')
                print(df1_sorted4)
                input("press enter to continue...")
                pass 
            
            elif sort_choice == 5:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice.")
                
          
    if choice == 3:
        index += 1
        print("You chose option 3:\n")
        
        Districts1= input("enter district name: ")
        Confirmed1= int(input("Enter number of confirmed cases: "))
        Recovered1= int(input("Enter number of Recovered Cases: "))
        Deaths1= int(input("Enter number of deaths: "))
        Active1=int( input("Eter number of active cases: "))
        
        data={'Districts':Districts1,'Confirmed':Confirmed1,
              'Recovered':Recovered1,'Deaths':Deaths1,'Active':Active1}
        df1=df1.append(data,ignore_index=True)
        df1.to_csv('covid19.csv',index=False)
        print(df1)
        input("Press Enter to continue...")


    elif choice == 4:
        index += 1
        print("You chose option 4: ")    
        dist=input("Enter district to edit: ")
        col=input("enter column name to update: ")
        val=input("enter new value: ")
        csv1.loc[csv1[csv1['Districts']==dist].index.values,col]=val
        csv1.to_csv("covid19.csv",index=False)
        print("Data updated")
        
        input("Press Enter to continue...")


    elif choice == 5:
        index += 1
        print("You chose option 5: ")  
        dist1=input("Enter district to delete: ")
        csv1=csv1[csv1.Districts!=dist1]
        csv1.to_csv('covid19.csv',index=False)
        print("deleted")
        input("Press Enter to continue")


    elif choice == 6:
        index += 1
        csv2=pd.read_csv('covid19.csv')
        Districts=csv2["Districts"]
        Confirmed=csv2["Confirmed"]
        Recovered=csv2["Recovered"]
        Deaths=csv2["Deaths"]
        Active=csv2["Active"]
        print("You chose option 6: ")
        while True:
            print("""
                  1 district wise confirmed cases
                  2 district wise recovered cases
                  3 district wise deaths 
                  4 district wise active cases
                  5 All Data
                  6 to go back 
                  enter your choice
                  """)
            line_graph_choice = int(input("Enter your choice "))
            if line_graph_choice == 1:
                plt.xlabel("Districts")
                plt.ylabel("Confirmed Cases")
                plt.title("Districts Wise Confirmed Cases")
                plt.plot(Districts,Confirmed, color='r')
                plt.show()
                
            elif line_graph_choice == 2:
                plt.xlabel("Districts")
                plt.ylabel("Recovered Cases")
                plt.title("Districts Wise Recovered Cases")
                plt.plot(Districts,Recovered, color='y')
                plt.show()
                pass 
            
            elif line_graph_choice == 3:
                plt.xlabel("Districts")
                plt.ylabel("Death Cases")
                plt.title("Districts Wise Death Cases")
                plt.plot(Districts,Deaths,color='b')
                plt.show()
                pass  
            
            elif line_graph_choice == 4:
                plt.xlabel("Districts")
                plt.ylabel("Active cases")
                plt.title("Districts Wise Active Cases")
                plt.plot(Districts,Active,color='r')
                plt.show()
                pass 
            
            elif line_graph_choice ==5:
                plt.xlabel("Districts")
                plt.ylabel("Number of cases")
                plt.plot(Districts,Confirmed,color='g',label="District Wise Confirmed Cases")
                plt.plot(Districts,Recovered,color='b',label="District Wise Recovered Cases")
                plt.plot(Districts,Deaths,color='r',label="District Wise Deaths")
                plt.plot(Districts,Active,color='y',label="District Wise Active Cases")
                plt.legend()
                plt.show()
            elif line_graph_choice == 6:
            
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")


    elif choice == 7:
        index += 1
        csv2=pd.read_csv('covid19.csv')
        Districts=csv2["Districts"]
        Confirmed=csv2["Confirmed"]
        Recovered=csv2["Recovered"]
        Deaths=csv2["Deaths"]
        Active=csv2["Active"]
        print("You chose option 7: ")
        while True:
            print(""" 
              1. District wise confirmed cases
              2. District wise recovered cases
              3. District wise deaths 
              4. District wise active cases
              5. All Data
              6. to go back 
              """)
            bar_graph_choice = int(input("Enter your choice: "))
            if bar_graph_choice == 1:
                plt.xlabel("Districts")
                plt.ylabel("Confirmed Cases")
                plt.title("District Wise Confirmed Cases")
                plt.bar(Districts, Confirmed, color='g', width=0.5)
                plt.show()  
            
            elif bar_graph_choice == 2:
                plt.xlabel("Districts")
                plt.ylabel("Recovered Cases")
                plt.title("District Wise Recovered Cases")
                plt.bar(Districts,Recovered,color='b',width=0.5)
                plt.show()            
                pass
        
            elif bar_graph_choice == 3:
                plt.xlabel("Districts")
                plt.ylabel("Deaths Cases")
                plt.title("District Wise Deaths")
                plt.bar(Districts,Deaths,color='b',width=0.5)
                plt.show()            
                pass
        
            elif bar_graph_choice == 4:
                plt.xlabel("Districts")
                plt.ylabel("Active Cases")
                plt.title("District Wise Active Cases")
                plt.bar(Districts,Active,color='b',width=0.5)
                plt.show()            
                pass
        
            elif bar_graph_choice == 5:
                plt.xlabel("Districts")
                plt.ylabel("Number of cases")
                plt.bar(Districts,Confirmed,color='g',label="District Wise Confirmed Cases")
                plt.bar(Districts,Recovered,color='b',label="District Wise Recovered Cases")
                plt.bar(Districts,Deaths,color='r',label="District Wise Deaths")
                plt.bar(Districts,Active,color='y',label="District Wise Active Cases")
                plt.legend()
                plt.show()             
                pass
        
            elif bar_graph_choice == 6:
              break  
            else:
                print("Invalid choice. Please try again.")

        input("Press Enter to continue...")

    elif choice == 8:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 8.")
        input("Press Enter to continue...")