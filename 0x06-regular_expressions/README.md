# 0x06. Regular expression
## GENERAL 
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
- All your regex must be built for the Oniguruma library

here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

```
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
```