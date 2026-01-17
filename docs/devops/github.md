# Github

## Git
### Usual workflow
```bash
git add .
git commit -m "<commit message>"
git push
```
#### Uncommiting file
```bash
git restore --staged <file>
```

#### Removing file from remote repo
```bash
// To remove file locally
git rm <file>

// To keep file locally
git rm --cached <file>
```

#### Changing commit messages
```bash
git rebase -i HEAD~4  // Edit (4) based on how many commits ago
```

## Github Actions
1. Create a directory `.github` in root.
2. 
