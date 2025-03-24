files_dir=~/user_files/
echo "file directory is $files_dir"
declare -a files
files=$(ls $files_dir)
for file in "${files[@]}"; do
    echo "Executing : aws s3 cp $files_dir/$file s3://image-upload-test-rc/user_files/$file"
    aws s3 cp $files_dir/$file s3://image-upload-test-rc/user_files/$file
    echo "File has been copied into S3 so deleting from EC2"
    rm $files_dir/$file
done

echo "python3 ~/ec2_connect_rds.py testdb s3_object_details "${files[@]}" s3://image-upload-test-rc/user_files/ $(whoami)"
result=$(python3 ~/ec2_connect_rds.py testdb s3_object_details "${files[@]}" s3://image-upload-test-rc/user_files/ $(whoami))
if ( result == 0 ) then
    echo "Data has been inserted into RDS"
else
  echo "Got some error while inserting data into RDS"
fi