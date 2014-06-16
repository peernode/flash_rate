BEGIN{
  print date
  FS="[\t +]"
  post_rate_hour_beta=sprintf("./data/post_rate_hour_beta_%s",date)
  post_rate_hour_master=sprintf("./data/post_rate_hour_master_%s",date)
  post_rate_date_beta="./data/post_rate_day_beta"
  post_rate_date_master="./data/post_rate_day_master"
  
  seed_hour_beta=sprintf("./data/seed_hour_beta_%s",date)
  seed_hour_master=sprintf("./data/seed_hour_master_%s",date)
  seed_day_beta="./data/seed_day_beta"
  seed_day_master="./data/seed_day_master"
  
  ip_infohash_beta=sprintf("./data/ip_infohash_post_beta_%s",date)
  ip_infohash_master=sprintf("./data/ip_infohash_post_master_%s",date)
  
  system("rm -rf " post_rate_hour_beta)
  system("rm -rf " post_rate_hour_master)
  system("rm -rf " seed_hour_beta)
  system("rm -rf " seed_hour_master)
  system("rm -rf " ip_infohash_beta)
  system("rm -rf " ip_infohash_master)

  for(i=0;i<24;i++)
  {
    post_beta[i]=1
    succ_beta[i]=0
    fail_beta[i]=0
    
    post_master[i]=1
    succ_master[i]=0
    fail_master[i]=0
    
    post_beta_first[i]=1
    succ_beta_first[i]=0
    fail_beta_first[i]=0

    post_master_first[i]=1
    succ_master_first[i]=0
    fail_master_first[i]=0
   
   	#seed rate
   	succ_mv_beta[i]=1
   	seed_mv_beta[i]=0
   	succ_tv_beta[i]=1
   	seed_tv_beta[i]=0
   	succ_cartoon_beta[i]=1
   	seed_cartoon_beta[i]=0
   	
   	succ_mv_master[i]=1
   	seed_mv_master[i]=0
   	succ_tv_master[i]=1
   	seed_tv_master[i]=0
   	succ_cartoon_master[i]=1
   	seed_cartoon_master[i]=0
  }  
  
  post_sum_beta=1
  succ_sum_beta=0
  fail_sum_beta=0
   
  post_sum_master=1
  succ_sum_master=0
  fail_sum_master=0
  
  post_sum_beta_first=1
  succ_sum_beta_first=0
  fail_sum_beta_first=0

  post_sum_master_first=1
  succ_sum_master_first=0
  fail_sum_master_first=0
 
 	# seed rate
 	suc_sum_mv_beta=1
 	seed_sum_mv_beta=0
 	suc_sum_tv_beta=1
 	seed_sum_tv_beta=0
 	suc_sum_cartoon_beta=1
 	seed_sum_cartoon_beta=0
 	
 	suc_sum_mv_master=1
 	seed_sum_mv_master=0
 	suc_sum_tv_master=1
 	seed_sum_tv_master=0
 	suc_sum_cartoon_master=1
 	seed_sum_cartoon_master=0
 	
 	# ip+infohash connect rate
}


{
  if($4=="124.207.205.1")
  {
    next;
  }
 
  if($6<0)
  {
    next;
  }
 
  time=$3
  hour=(int($3/3600)+8)%24
  ver=$5
  type=$11  #1 mv, 2 tv, 3 cartoon
   
  if(index(ver,"_Beta"))
  {
    post_beta[hour]=post_beta[hour]+$6
    succ_beta[hour]=succ_beta[hour]+$7
    fail_beta[hour]=fail_beta[hour]+$8
    
    post_sum_beta=post_sum_beta+$6
    succ_sum_beta=succ_sum_beta+$7
    fail_sum_beta=fail_sum_beta+$8

    if($13==1){
        post_beta_first[hour]+=$6
        succ_beta_first[hour]+=$7
        fail_beta_first[hour]+=$8
        
        post_sum_beta_first+=$6
        succ_sum_beta_first+=$7
        fail_sum_beta_first+=$8      
    }  
  
    # seed rate
    if(type==1){
    	succ_mv_beta[hour]+=$7;
    	seed_mv_beta[hour]+=$9
    	suc_sum_mv_beta+=$7
    	seed_sum_mv_beta+=$9
    	
    }else if(type==2){
    	succ_tv_beta[hour]+=$7;
    	seed_tv_beta[hour]+=$9
    	suc_sum_tv_beta+=$7
    	seed_sum_tv_beta+=$9
    }else if(type==3){
    	succ_cartoon_beta[hour]+=$7;
    	seed_cartoon_beta[hour]+=$9
    	suc_sum_cartoon_beta+=$7
    	seed_sum_cartoon_beta+=$9
    }    	
    
    # ip+infohash+GUID
    #print $4, $10, $15
    ip_infohash_post_beta[$4, $10, $15]+=$6
    ip_infohash_suc_beta[$4, $10, $15]+=$7
  }
  else
  {
    #print hour, $6, $7, $8
    post_master[hour]=post_master[hour]+$6
    succ_master[hour]=succ_master[hour]+$7
    fail_master[hour]=fail_master[hour]+$8
  
    post_sum_master=post_sum_master+$6
    succ_sum_master=succ_sum_master+$7
    fail_sum_master=fail_sum_master+$8

    if($13==1){
        post_master_first[hour]+=$6
        succ_master_first[hour]+=$7
        fail_master_first[hour]+=$8

        post_sum_master_first+=$6
        succ_sum_master_first+=$7
        fail_sum_master_first+=$8
    }
    
    # seed rate
    if(type==1){
    	succ_mv_master[hour]+=$7;
    	seed_mv_master[hour]+=$9
    	suc_sum_mv_master+=$7
    	seed_sum_mv_master+=$9
    }else if(type==2){
    	succ_tv_master[hour]+=$7;
    	seed_tv_master[hour]+=$9
    	suc_sum_tv_master+=$7
    	seed_sum_tv_master+=$9
    }else if(type==3){
    	succ_cartoon_master[hour]+=$7;
    	seed_cartoon_master[hour]+=$9
    	suc_sum_cartoon_master+=$7
    	seed_sum_cartoon_master+=$9
    }   
    #print $4, $10, $15, $6 
    ip_infohash_post_master[$4, $10, $15]+=$6
    ip_infohash_suc_master[$4, $10, $15]+=$7 
  }
}

END{
  for(i=0;i<24;i++){
  	# beta connect suc rate
    print i,post_beta[i],succ_beta[i],fail_beta[i],post_beta_first[i],succ_beta_first[i],fail_beta_first[i] >> post_rate_hour_beta
    
    # master connect suc rate
    print i,post_master[i],succ_master[i],fail_master[i],post_master_first[i],succ_master_first[i],fail_master_first[i] >> post_rate_hour_master
    
    # beta seed rate
    print i, succ_mv_beta[i], seed_mv_beta[i], succ_tv_beta[i], seed_tv_beta[i], succ_cartoon_beta[i], seed_cartoon_beta[i] >> seed_hour_beta
    
    # master seed rate
    print i, succ_mv_master[i], seed_mv_master[i], succ_tv_master[i], seed_tv_master[i], succ_cartoon_master[i], seed_cartoon_master[i] >> seed_hour_master
  }    

  print date,post_sum_beta,succ_sum_beta,fail_sum_beta,post_sum_beta_first,succ_sum_beta_first,fail_sum_beta_first >> post_rate_date_beta

  print date,post_sum_master,succ_sum_master,fail_sum_master,post_sum_master_first,succ_sum_master_first,fail_sum_master_first >> post_rate_date_master
  
  print date, suc_sum_mv_beta, seed_sum_mv_beta, suc_sum_tv_beta, seed_sum_tv_beta, suc_sum_cartoon_beta, seed_sum_cartoon_beta >> seed_day_beta
  print date, suc_sum_mv_master, seed_sum_mv_master, suc_sum_tv_master, seed_sum_tv_master, suc_sum_cartoon_master, seed_sum_cartoon_master >> seed_day_master
  
  # ip_infohash
  for(m in ip_infohash_post_beta){
  	split(m, idx, SUBSEP)
    print idx[1], idx[2], idx[3], ip_infohash_post_beta[m], ip_infohash_suc_beta[m] >> ip_infohash_beta
  }
  
  for(n in ip_infohash_post_master){
    split(n, nidx, SUBSEP)
  	print nidx[1], nidx[2], nidx[3], ip_infohash_post_master[n], ip_infohash_suc_master[n] >> ip_infohash_master
  }
}



