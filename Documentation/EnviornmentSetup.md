# ENV Setup
### Step 1:
Download and install the appropriate python3 for your windows machine from `python.org/downloads/windows`
### Step 2:
Install these python libraries using pip

  ```
  pip install PyYaml
  pip install random-word
  ```
  
### Step 3: Clone the repository
  ```
  git clone https://github.com/abladow/BAD-USB.git
  ```

You are ready to make changes to the code without throwing dependency errors!

### Step 4: Enable PnP logging (Windows Only) 

Enable PNP auditing in the Windows Local Security Policy under:
```
Advanced Audit Policy Configuration\Detailed Tracking\Audit PNP Activity
```
Enable Success and Failure.
