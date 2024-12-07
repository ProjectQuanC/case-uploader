# Case Uploader

This is the CLI version of case uploader for Quan C Secure Programming Application. To use this script you need to setup your GitHub Personal Access Token. <b> Make sure your GitHub Account registered as admin in Quan C databases.</b>

## How To Get Your Personal Access Token (Easiest Method)
1. Go to your GitHub Account
2. Navigate to Settings > Developer Settings > Personal Access Token > Tokens (classic) > Generate new token.
3. Select the necessary scopes, such as:
    > read:user (required to access user details)
4. Generate and copy the token.
5. Use the Token in the Authorization Header.

<b>The token should be sent as Bearer \<your-token> in the Authorization Header.</b>

Example script can be seen in the <b>sample_command.sh</b> file