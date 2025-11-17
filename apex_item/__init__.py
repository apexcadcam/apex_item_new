__version__ = "1.0.0"

# Run setup hook immediately when module is imported
try:
	from pathlib import Path
	import sys
	
	# Find setup_hook.py in the app root (apps/apex_item/)
	app_root = Path(__file__).parent.parent.parent
	setup_hook = app_root / "setup_hook.py"
	
	if setup_hook.exists():
		# Import and run the hook
		sys.path.insert(0, str(app_root))
		from setup_hook import ensure_app_in_apps_txt
		ensure_app_in_apps_txt()
		sys.path.pop(0)
except Exception:
	# Silently fail - this is a helper function
	pass

