class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str)-> list[list[str]]:
        output = []
        products.sort()

        for i, c in enumerate(searchWord):
            tmp = []
            for p in products:
                if i < len (p) and c == p[i]:
                    tmp.append(p)
            output.append(tmp[:3])
            products = tmp
        
        return output

def main():
    sample = Solution()
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    print(sample.suggestedProducts(products, "monitor"))


if __name__ == "__main__":
    main()