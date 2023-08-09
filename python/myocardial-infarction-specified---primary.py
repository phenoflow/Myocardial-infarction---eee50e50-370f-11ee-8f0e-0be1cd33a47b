# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"12139","system":"med"},{"code":"13571","system":"med"},{"code":"14658","system":"med"},{"code":"14897","system":"med"},{"code":"14898","system":"med"},{"code":"1677","system":"med"},{"code":"1678","system":"med"},{"code":"17872","system":"med"},{"code":"23892","system":"med"},{"code":"241","system":"med"},{"code":"2491","system":"med"},{"code":"26972","system":"med"},{"code":"26975","system":"med"},{"code":"28736","system":"med"},{"code":"29643","system":"med"},{"code":"29758","system":"med"},{"code":"30330","system":"med"},{"code":"30421","system":"med"},{"code":"32272","system":"med"},{"code":"32854","system":"med"},{"code":"34803","system":"med"},{"code":"3704","system":"med"},{"code":"40429","system":"med"},{"code":"41221","system":"med"},{"code":"41835","system":"med"},{"code":"46017","system":"med"},{"code":"46112","system":"med"},{"code":"46276","system":"med"},{"code":"52705","system":"med"},{"code":"5387","system":"med"},{"code":"55401","system":"med"},{"code":"59032","system":"med"},{"code":"61670","system":"med"},{"code":"62626","system":"med"},{"code":"63467","system":"med"},{"code":"68357","system":"med"},{"code":"68748","system":"med"},{"code":"7783","system":"med"},{"code":"8935","system":"med"},{"code":"9507","system":"med"},{"code":"96838","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('myocardial-infarction-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["myocardial-infarction-specified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["myocardial-infarction-specified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["myocardial-infarction-specified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
