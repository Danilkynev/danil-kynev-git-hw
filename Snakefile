rule all:
    input:
        "result.txt"

rule generate_star_wars_report:
    output:
        "result.txt"
    shell:
        """
        python scripts/star_wars.py
        """