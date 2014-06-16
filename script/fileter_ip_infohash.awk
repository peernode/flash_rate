#! /bin/bash
BEGIN{
}

{
    if($4>=30){
        print $1, $2, $4, $5/$4
    }
}

END{
}
