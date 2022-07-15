# Author:- Deepak Kumar Jha
# Rules based inference for arguments type in python.
# Arguments :- Python source file path.
# Result:- list containing the inference of the arguments of the functions based 
# AST parsing and logic inferencing. 

import os
import sys
import ast
from pprint import pprint
import json

#Create Abstract Syntax Tree.
class Visitor(ast.NodeVisitor):

    def visit(self,node: ast):
        print(node)
        self.generic_visit(node)

    def function_visitor(self,nodes: ast):
        # Traversing the AST tree of the source code.
        all_func_def_list=[]

        for node in ast.walk(nodes):
            #Looking only for Function Definition  
            if isinstance(node, ast.FunctionDef):
                # AST Tree dump.
                # print("AST")
                # print(ast.dump(node))
                func_list=[]
                print("Function Name--------------------")
                print(node.name)
                func_list.append(node.name)
                print("---------------------------------")
                print(ast.dump(node))
                #print(node.args)
                #print(node)
                #print(node.returns)
                #print(node._fields)
                print("Arguments list-----------")
                #arg_dict=json.dumps(ast.dump(node.args))
                #print(ast.dump(node.args))
                #print(arg_dict)
                #print(ast.dump(node.args))
                # Getting the Arguements of the function calls.
                arg_lis=[]
                for arglis in node.args.args:    
                    print(arglis.arg)
                    arg_lis.append(arglis.arg)
                # Body contains the Assign and Return object.
                for bod in node.body:
                    # Assign object.
                    arg_def=[]
                    # Assign object in body.
                    if isinstance(bod, ast.Assign):
                        bod_dump = ast.dump(bod.value)
                        print("Assign object-----")
                        # print(bod_dump)
                        Type_val=""
                        # Variable assigment object target.
                        # Target variable assignments.
                        '''
                        for val in bod.targets:
                            print(val.id)
                        '''    
                        # Dictionary instance.
                        if isinstance(bod.value, ast.Call): 
                           print(arg_lis)
                           print("Call Attribute")
                           
                           if isinstance(bod.value.func, ast.Attribute):
                                print(ast.dump(bod.value.func))
                                # Attribute contains Name object.
                                # Nested Call and Attribute 
                                if isinstance(bod.value.func.value, ast.Call):
                                    print(ast.dump(bod.value.func.value))
                                    print(bod.value.func.value.func.value)
                                    if isinstance(bod.value.func.value.func.value, ast.Name):
                                        print(bod.value.func.value.func.value.id)
                                        print(bod.value.func.value.func.attr)
                                        print(bod.value.func.attr)
                                        # Arguments list.
                                        print(bod.value.func)
                                        
                                        for argx in arg_lis:
                                            if argx==bod.value.func.value.func.value.id:
                                                arg_def.append(argx)
                                                arg_def.append("pandas.Dataframe")
                                                Type_val = "pandas.Dataframe"
                                                     
                                if isinstance(bod.value.func.value, ast.Name):
                                    print("value")
                                    print(bod.value.func.value.id)
                                    print("attr")
                                    print(bod.value.func.attr)
                                    # Apply function of DataFrames.
                                    if(bod.value.func.attr=="apply"):
                                        print("Dataframe apply.")
                                        print(ast.dump(bod.value.func))
                                        print("Argument list for more function calls.")
                                        for arelem in bod.value.args:
                                            print(arelem.value.id)
                                            print(arelem.attr)
                                    # isnull() function of the Dataframes.        
                                    if(bod.value.func.attr=="isnull"):
                                        print("Dataframe isnull() function.")
                                        print(ast.dump(bod.value.func))
                                        print("Argument list for more function calls.")
                                        for arelem in bod.value.args:
                                            print(arelem.value.id)
                                            print(arelem.attr)
                                    # merge function of the dataframes.
                                    if(bod.value.func.attr=="merge"):
                                        print("Dataframe merge() function.")
                                        print(ast.dump(bod.value.func))
                                        print("Argument list for more function calls.")
                                        for arelem in bod.value.args:
                                            print(ast.dump(arelem))
                                            print(arelem.id)
                                            if(arelem.id) in arg_lis:
                                                arg_def.append(arelem.id)
                                                arg_def.append("pandas.Dataframe")
                                                Type_val = "pandas.Dataframe"

                                    # For DataFrame creation method.        
                                    if(bod.value.func.attr=="DataFrame"):
                                        print("Assign target variable")
                                        print(bod.targets)
                                        # List objects of target variables.
                                        for elem in bod.targets:
                                            print(elem.id)
                                            if elem.id in arg_lis:
                                                print("Dataframe Manipulation")
                                                arg_def.append(elem.id)
                                                arg_def.append("pandas.Dataframe")
                                                Type_val = "pandas.Dataframe"
                                    # When the dataframe funtions are used.    
                                    if(bod.value.func.value.id) in arg_lis:
                                        arg_def.append(bod.value.func.value.id)
                                        arg_def.append("pandas.Dataframe")
                                        Type_val = "pandas.Dataframe"

                                # Part of the Subscript object.
                                elif isinstance(bod.value.func.value.func.value, ast.Subscript):
                                    print(bod.value.func.value.func.value.value.id)
                                    if (bod.value.func.value.func.value.value.id) in arg_lis:
                                        arg_def.append(bod.value.func.value.func.value.value.id)
                                        arg_def.append("pandas.Dataframe")
                                        Type_val = "pandas.Dataframe"
                                    print(bod.value.func.value.func.value._attributes)
                                    print(bod.value.func.value.func.value.slice.id)
                                    if bod.value.func.value.func.value.slice.id in arg_lis:
                                        arg_def.append(bod.value.func.value.func.value.slice.id)
                                        arg_def.append("Int")
                                    print(bod.value.func.value.func.value.slice._attributes)
                                    print(bod.value.func.value.func.value.slice) 

                        # Dictionary object       
                        if isinstance(bod.value, ast.Dict):
                           print("Dictionary object")
                           for val in bod.targets:
                                var_id = val.id
                                #print(val)
                                print(var_id) 
                           # Arguments list match.     
                           if var_id in arg_lis:
                               arg_def.append(var_id)    
                               dic_val = bod.value
                               print(dic_val)
                               print("Dictionary Keys")
                               for ele_keys in bod.value.keys:
                                  print(ele_keys.value)
                               print("Dictionary Values:-")    
                               for ele_val in bod.value.values:
                                  if isinstance(ele_val, ast.List):
                                     print(ele_val)
                                  else:
                                     print(ele_val.value)
                               arg_def.append("Dict") 
                               Type_val = "Dict" 

                        # Lists Instance       
                        if isinstance(bod.value, ast.List):
                           print("List object")
                           for val in bod.targets:
                                var_id = val.id
                                #print(val)
                                print(var_id)
                           #list_val = bod.value
                           #print(list_val)
                           for eleml in bod.value.elts:
                               print(eleml.value)
                           if var_id in arg_lis:
                               arg_def.append(var_id)            
                           arg_def.append("List") 
                           Type_val="List"
                        # Subscript Assumption.    
                        if isinstance(bod.value, ast.Subscript):
                           print("Subscript Object")
                           vars_nod = bod.value.value.id 
                           print(vars_nod)
                           # print(bod.value.value)
                           # slicing from the upper val.

                           if (bod.value.slice):
                            print("Slice object")
                            print(ast.dump(bod.value.slice))
                            if isinstance(bod.value.slice, ast.Slice):
                                print("upper slice id")
                                print(bod.value.slice.upper.id)
                                
                                if vars_nod in arg_lis:
                                    arg_def.append(vars_nod)
                                    arg_def.append("List")
                                    Type_val = 'List'

                                if bod.value.slice.upper.id in arg_lis:
                                    arg_def.append(bod.value.slice.upper.id)
                                    arg_def.append("Int")

                        # Subscript Assumption.    
                        if isinstance(bod.value, ast.Subscript):
                           print("Subscript Object")
                           vars_nod = bod.value.value.id 
                           print(vars_nod)
                           # print(bod.value.value)
                           # slicing from the upper val.
                           if (bod.value.slice):
                            print("Slice object")
                            print(ast.dump(bod.value.slice))
                            if isinstance(bod.value.slice, ast.Name):
                                print("Slice is Name object")
                                print(bod.value.slice.id)
                                if vars_nod in arg_lis:
                                    arg_def.append(vars_nod)
                                    arg_def.append("List")
                                    Type_val = 'List'
                                if bod.value.slice.id in arg_lis:
                                    arg_def.append(bod.value.slice.id)
                                    arg_def.append("Int")

                        # Constant variable values.        
                        if isinstance(bod.value, ast.Constant):
                            
                            for val in bod.targets:
                                var_id = val.id
                                print(val)
                                print(var_id)

                            vars_cons = bod.value.value
                            type_c = type(vars_cons)
                            if var_id in arg_lis:
                                arg_def.append(var_id)    
                                #print(var_id)
                                #print(type_c)
                                arg_def.append(type_c)
                            Type_val = type_c     

                        # If the Type cannot be inferred.#
                        if len(arg_def)!=0:
                            if Type_val=="":
                                Type_val="Unknown"
                                # Append the type and arg val.
                                arg_def.append(Type_val)
                        # Avoid adding empty list to the final function definition.    
                        if len(arg_def)!=0:
                            func_list.append(arg_def)
                        print(func_list)
                    
                    # Return object.    
                    if isinstance(bod, ast.Return):
                        return_val = bod.value.id
                        #print("Return object-----")
                        #print(return_val)

                all_func_def_list.append(func_list)        
        return all_func_def_list        

# Read the input file path.
source_filename = sys.argv[1].strip()
print(source_filename)

print(os.path.isfile(source_filename))

if os.path.isfile(source_filename):
    # File path
    print(os.path.basename(source_filename))

    with open(source_filename, "r") as source:
        src_code = source.read()
    node = ast.parse(src_code)
    tree_dump = ast.dump(node, indent=2)
    
    #print(tree_dump)
    #print(node)
    #print("Node Fields")
    #print(node._fields)
    #print("Node Body")
    #print(node.body)
    #print("Visit Node using Visitor")
    #Visitor().visit(node)
    fdef_list=Visitor().function_visitor(node)
    # Final Function definition List.
    print("\n")
    print("Final Function Definition and Type Inference**********************************")
    print("\n")
    print(fdef_list)
    print("\n")
    print("******************************************************************************")
    
else:
    print("Invalid File!!!. Please Provide Valid File Path.")