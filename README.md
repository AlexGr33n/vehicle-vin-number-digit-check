# vehicle-vin-number-digit-check
CHECK DIGIT CALCULATOR  A vehicle identification number, VIN, is a unique code used to identify each vehicle produced by the automotive industry. VINs were standardized in 1981 to contain 17 characters, not including the letters i, o, and q. The first few digits identify the world manufacturer. The 4th to 8th digits identify the vehicle attributes. The 10th digit is the model year, the 11th digit is the plant where the vehicle was manufactured and the vehicle serial number is typically the 12th to 17th digit. The ninth digit is reserved for the check digit.  The check digit, found in position 9 of the VIN and compulsory for vehicles in North America, is used to validate a VIN. This is helpful for computers to immediately tell if there is an error or issue with the VIN. The check digit is calculated by removing all of the letters and substituting them with their appropriate number counterparts. You then take those numbers and multiply them against a weight factor table. You then have 16 numbers which you add together and then divide by 11. The remainder is the check digit. If the remainder is 10, then the check digit is “X”. 
reference: https://www.cjponyparts.com/resources/check-digit-calculator
https://www.youtube.com/watch?v=wOb76Q0zTho 
https://www.youtube.com/watch?v=LLtdAWXvpCg

please do not make any change for lt.csv, pw.csv that is my dataframe need to be refered.
vin.csv just an example for you to try, if you wish you can add more raws underneath.
