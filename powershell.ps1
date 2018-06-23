$CUname = $env:computername+'.'+$env:USERDNSDOMAIN
$CUname | Out-File scripts\username.txt
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http://$env:computername.$env:USERDNSDOMAIN/PowerShell/ -Authentication Kerberos
Import-PSSession $Session
$initial_user = (Get-Mailbox -ResultSize Unlimited).count
$a = Get-Content scripts\user_file_path.txt
Get-Mailboxdatabase | Format-Wide -Property Name -Column 1 | Out-File scripts\databasename.txt
(gc scripts\databasename.txt) | ?{$_.trim() -ne ""} | set-content scripts\databasename.txt
$Mail = (gc scripts\databasename.txt) | Foreach{$_.TrimEnd()}
Import-csv $a |ForEach-Object {New-Mailbox -LastName $_.LastName -FirstName $_.FirstName -Name $_.Name -OrganizationalUnit $EMAILSTUDY -Database $Mail -UserPrincipalName $_.UserPrincipalName -Password(ConvertTo-SecureString $_.Password -AsPlainText -Force)}
Get-Mailbox -ResultSize Unlimited | where{$_.WhenMailboxCreated -gt (get-date).addminutes(-5)} | Set-MailboxRegionalConfiguration -Language en-US -TimeZone "Central Standard Time"
Get-Mailbox -ResultSize Unlimited -Filter{RecipientTypeDetails -eq "UserMailbox"} | Format-Wide -Property Name -Column 1 | Out-File scripts/Available_Users.txt
(gc scripts/Available_Users.txt) | ?{$_.trim() -ne ""} | set-content scripts/Available_Users.txt
$final_user = (Get-Mailbox -ResultSize Unlimited).count
$count = $final_user - $initial_user
$count | Out-File scripts/Users_Created.txt
(gc scripts/Users_Created.txt) | ?{$_.trim() -ne ""} | set-content scripts/Users_Created.txt