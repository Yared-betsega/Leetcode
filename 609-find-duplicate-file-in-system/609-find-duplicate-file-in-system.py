class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        args = defaultdict(list)
        for i, path in enumerate(paths):
            sep = path.split(" ")
            for j in range(1, len(sep)):
                file = sep[j]
                file, arg = file.split("(")
                args[arg[:-1]].append(sep[0] + "/"+ file)
                
        ans = []
        for key, group in args.items():
            if len(args[key]) >=2:
                ans.append(group)
        
        return ans