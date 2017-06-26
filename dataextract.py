#Opening:
data = open('data.csv', 'r')
export = open('dataJS.txt', 'w')

data.readline()
export.write("var blooData = [{\n")
for line in data:
    line = line.split(",")
    export.write("\"label\": \"{0}\",\n".format(line[0]))
    export.write("\"value\": \"{0}\",\n".format(line[1])) #size of outer circle
    export.write("\"children\": [{\n")
    export.write("   name: \"Description of {0}\",\n".format(line[0]))
    export.write("   group: \"{0}\",\n".format(line[0]))
    export.write("   size: {0},\n".format(line[1]))
    export.write("}]\n")
    export.write("}, {\n")

#Ending
export.write("}];\n")