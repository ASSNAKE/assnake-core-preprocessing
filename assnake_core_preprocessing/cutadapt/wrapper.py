from snakemake.shell import shell

print('LET"S GPOO')
custom_params = open(snakemake.input.params).read().strip()
cmd = f'''
    cutadapt --cores {{snakemake.threads}} {custom_params} \
         --info-file {{snakemake.output.info}} \
        -o {{snakemake.output.r1}} -p {{snakemake.output.r2}} {{snakemake.input.r1}} {{snakemake.input.r2}} > {{snakemake.log}} 2>&1
'''
print('cmd')

shell(cmd)