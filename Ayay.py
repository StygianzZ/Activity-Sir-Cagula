import dis
import time

def writing(task, delay):
    """Process and write data elements with configurable delay"""
    output_log = []
    for element in task:
        status_msg = f"Processing write operation: {element}"
        output_log.append(status_msg)
        time.sleep(delay)
    return output_log

def reading(task, delay):
    """Retrieve and read data elements with configurable delay"""
    input_buffer = []
    for element in task:
        status_msg = f"Executing read operation: {element}"
        input_buffer.append(status_msg)
        time.sleep(delay)
    return input_buffer

# Custom analysis function for bytecode inspection
def analyze_bytecode(func_name, func_obj):
    """Perform detailed bytecode analysis and return metrics"""
    instructions_list = list(dis.get_instructions(func_obj))
    total_instr_count = len(instructions_list)
    variable_load_count = sum(1 for instr in instructions_list if "LOAD" in instr.opname)
    
    return {
        'function': func_name,
        'instructions': total_instr_count,
        'lookups': variable_load_count
    }

# Main execution
task_data = "3task"
delay_interval = 0.5

writing(task_data, delay_interval)
reading(task_data, delay_interval)

print("\n" + "="*70)
print("CUSTOM BYTECODE ANALYSIS REPORT")
print("="*70)

print("\n--- Writing Function Bytecode Disassembly ---")
dis.dis(writing)

print("\n--- Reading Function Bytecode Disassembly ---")
dis.dis(reading)

# Perform custom analysis
write_metrics = analyze_bytecode("writing", writing)
read_metrics = analyze_bytecode("reading", reading)

print("\n" + "="*70)
print("CUSTOM BYTECODE METRICS")
print("="*70)

print(f"\nWriting Function Analysis:")
print(f"  Total Instructions: {write_metrics['instructions']}")
print(f"  Variable Lookups: {write_metrics['lookups']}")

print(f"\nReading Function Analysis:")
print(f"  Total Instructions: {read_metrics['instructions']}")
print(f"  Variable Lookups: {read_metrics['lookups']}")

combined_instructions = write_metrics['instructions'] + read_metrics['instructions']
combined_lookups = write_metrics['lookups'] + read_metrics['lookups']

print("\n" + "-"*70)
print(f"Combined Total Instructions: {combined_instructions}")
print(f"Combined Total Variable Lookups: {combined_lookups}")
print("-"*70)