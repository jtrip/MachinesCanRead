# MachinesCanRead
Python Machine Readable Code generator

I use this to generate machine readable codes; barcodes (Code39), and soon qr codes and/or data matrix.

Currently you can either edit the hardcoded default codes to genetate svgs.  

OR 

pass the format [svg|emf] and codes as arguments.   
eg  

    $ Python generateMC.py svg LOL OMG WTF BBQ
  
will generate these files:  

    LOL.svg  
    OMG.svg  
    WTF.svg  
    BBQ.svg  


Currently Supports EMF because MS Word is a little silly.  
