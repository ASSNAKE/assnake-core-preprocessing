fix_base_count(){
    local counts=($(cat))
    echo "${counts[0]} $((${counts[1]} - ${counts[0]}))"
}

echo "gg"
INPUT=$1

gunzip -c $INPUT \
    | awk 'NR % 4 == 2' \
    | wc -cl \
    | fix_base_count
